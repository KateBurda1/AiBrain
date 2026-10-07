"""~34s brand film for Innospec: Ken Burns photo moves, crossfades, Flying Horse brand type."""
import subprocess, sys, os, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

S = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
VW, VH, FPS = 1920, 1080, 30
XF = 0.8  # crossfade seconds

AV = "/System/Library/Fonts/Avenir Next.ttc"
def av(size, idx): return ImageFont.truetype(AV, size, index=idx)
SERIF_I = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf", 46)
COPPER = (150, 106, 77); TAN = (217, 184, 156); WHITE = (255, 255, 255)

# (image, start, end, zoom_from, zoom_to, pan (dx,dy) as fraction, focus (fx,fy), text spec)
SHOTS = [
    ("062", 0.0, 4.6, 1.00, 1.10, (0.00, -0.02), (0.5, 0.5), ("FOR 18 YEARS", "You have played", "for America's heroes.")),
    ("001", 4.6, 8.6, 1.12, 1.02, (0.03, 0.00), (0.5, 0.45), ("THIS YEAR, PLAY WHERE THEY SERVE", "Within sight of the", "U.S. Air Force Academy.")),
    ("034", 8.6, 12.4, 1.00, 1.12, (0.00, 0.02), (0.5, 0.55), ("FOR THE GAME", "Championship golf", "beneath Pikes Peak.")),
    ("121", 12.4, 15.8, 1.10, 1.00, (-0.03, 0.00), (0.5, 0.5), ("FOR YOUR SPONSORS", "A Four Diamond resort,", "all yours.")),
    ("098", 15.8, 18.8, 1.00, 1.10, (0.02, 0.00), (0.5, 0.5), ("FOR THEIR GUESTS", "A weekend", "of their own.")),
    ("020", 18.8, 21.8, 1.10, 1.00, (0.00, 0.00), (0.5, 0.5), ("FOR THE STORIES", "Long dinners.", "Mountain sunsets.")),
    ("140", 21.8, 25.4, 1.00, 1.08, (0.00, -0.02), (0.5, 0.4), ("FOR CONNECTION", "Where Belonging &", "Connection Meet.")),
    ("030", 25.4, 29.4, 1.08, 1.00, (0.02, 0.00), (0.5, 0.45), ("FOR OUR HEROES", "95\u00a2 of every dollar", "goes straight to them.")),
    ("065", 29.4, 34.5, 1.00, 1.10, (0.00, 0.00), (0.5, 0.5), "END"),
]
TOTAL = SHOTS[-1][2]

def load(n):
    im = Image.open(os.path.join(S, "hi", f"{n}.jpg")).convert("RGB")
    # ensure cover at 16:9 with zoom headroom
    iw, ih = im.size
    scale = max(VW * 1.18 / iw, VH * 1.18 / ih, 1.0)
    if scale > 1.0:
        im = im.resize((int(iw * scale), int(ih * scale)), Image.LANCZOS)
    return im

IMGS = {s[0]: load(s[0]) for s in SHOTS}

def ease(t): return 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, t)))

def frame_for(shot, t):
    n, a, b, z0, z1, pan, foc, _ = shot
    im = IMGS[n]; iw, ih = im.size
    u = (t - a) / (b - a + XF)
    u = max(0.0, min(1.0, u))
    z = z0 + (z1 - z0) * u
    # base crop: largest 16:9 box, then divide by zoom
    bw = min(iw, ih * VW / VH); bh = bw * VH / VW
    cw, ch = bw / z, bh / z
    cx = iw * foc[0] + pan[0] * iw * (u - 0.5)
    cy = ih * foc[1] + pan[1] * ih * (u - 0.5)
    cx = min(max(cx, cw / 2), iw - cw / 2); cy = min(max(cy, ch / 2), ih - ch / 2)
    box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
    return im.resize((VW, VH), Image.BICUBIC, box=box)

# Bottom-left gradient for legibility
grad = Image.new("L", (VW, VH), 0)
g = np.zeros((VH, VW), dtype=np.float32)
ys = np.linspace(0, 1, VH)[:, None]; xs = np.linspace(0, 1, VW)[None, :]
g = np.clip((ys - 0.35) / 0.65, 0, 1) ** 1.3 * 0.78 + np.clip((0.6 - xs) / 0.6, 0, 1) * 0.25
GRAD = Image.fromarray((np.clip(g, 0, 0.85) * 255).astype(np.uint8))
BLACK = Image.new("RGB", (VW, VH), (0, 0, 0))

def spaced(draw, xy, txt, font, fill, spacing):
    x, y = xy
    for ch in txt:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + spacing
    return x

def text_layer(spec):
    L = Image.new("RGBA", (VW, VH), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    eb, l1, l2 = spec
    x, y = 130, 720 if l2 else 790
    d.rectangle([x, y + 4, x + 6, y + 4 + (230 if l2 else 160)], fill=COPPER + (255,))
    spaced(d, (x + 36, y), eb, av(26, 2), TAN + (255,), 5)
    f = av(74, 0)
    d.text((x + 34, y + 44), l1, font=f, fill=WHITE + (255,))
    if l2: d.text((x + 34, y + 134), l2, font=f, fill=WHITE + (255,))
    return L

def end_layer():
    L = Image.new("RGBA", (VW, VH), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    logo = Image.open(os.path.join(S, "logo_white.png")).convert("RGBA")
    lw = 560; logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    L.alpha_composite(logo, ((VW - lw) // 2, 190))
    def ctr(txt, y, font, fill, sp=0):
        w = sum(d.textlength(c, font=font) + sp for c in txt) - sp
        spaced(d, ((VW - w) / 2, y), txt, font, fill, sp)
    ctr("HONORING THOSE WHO SERVE", 610, av(30, 2), TAN + (255,), 7)
    ctr("The Innospec Charity Golf Tournament", 665, av(62, 0), WHITE + (255,))
    d.rectangle([VW / 2 - 50, 765, VW / 2 + 50, 769], fill=COPPER + (255,))
    ctr("August 2027  ·  Colorado Springs, Colorado", 800, SERIF_I, WHITE + (255,))
    return L

LAYERS = [end_layer() if s[7] == "END" else text_layer(s[7]) for s in SHOTS]

def render(t):
    # which shots are visible
    base = None
    for i, sh in enumerate(SHOTS):
        a, b = sh[1], sh[2]
        if a <= t < b + (XF if i < len(SHOTS) - 1 else 0):
            fr = frame_for(sh, t)
            if base is None:
                base = fr; idx = i
            else:
                w = ease((t - a) / XF)
                base = Image.blend(base, fr, w); idx = i
    if base is None: base = frame_for(SHOTS[-1], t); idx = len(SHOTS) - 1
    # darken + gradient
    is_end = SHOTS[idx][7] == "END"
    if is_end:
        dk = ease((t - SHOTS[idx][1]) / 1.2) * 0.55
        base = Image.blend(base, BLACK, dk)
    else:
        base = Image.composite(BLACK, base, GRAD)
    out = base.convert("RGBA")
    # text: never overlaps a crossfade. In over [a+0.3, a+0.75], out over [b-0.4, b]
    for i, sh in enumerate(SHOTS):
        a, b = sh[1], sh[2]
        last = i == len(SHOTS) - 1
        i0, i1 = (a + 1.0, a + 1.6) if last else (a + 0.3, a + 0.75)
        o0, o1 = (TOTAL - 1.4, TOTAL - 0.9) if last else (b - 0.4, b)
        if i0 <= t <= o1:
            al = min(ease((t - i0) / (i1 - i0)), ease((o1 - t) / (o1 - o0)))
            if al > 0:
                lay = LAYERS[i]
                if al < 1:
                    lay = lay.copy(); lay.putalpha(lay.split()[3].point(lambda v: int(v * al)))
                dy = int((1 - al) * 18)
                out.alpha_composite(lay, (0, dy))
    # global fade from/to black
    fade = min(ease(t / 0.8), ease((TOTAL - t) / 1.0))
    out = out.convert("RGB")
    if fade < 1: out = Image.blend(BLACK, out, fade)
    return out

ff = imageio_ffmpeg.get_ffmpeg_exe()
p = subprocess.Popen([ff, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}", "-r", str(FPS), "-i", "-",
                      "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", OUT],
                     stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
N = int(TOTAL * FPS)
for k in range(N):
    t = k / FPS
    p.stdin.write(render(t).tobytes())
    if k in (int(3 * FPS), int(10 * FPS), int(21.9 * FPS), int(32 * FPS)):
        render(t).save(os.path.join(S, f"vid_still_{k:04d}.jpg"), quality=80)
p.stdin.close(); p.wait()
print("done", OUT, N, "frames", TOTAL, "s")
