import sys, os, io, subprocess
from playwright.sync_api import sync_playwright
from PIL import Image
import imageio_ffmpeg
D=os.path.dirname(os.path.abspath(__file__)); OUT=sys.argv[1]; FPS=24
os.makedirs(OUT, exist_ok=True)
frames_dir=os.path.join(D,"frames"); os.makedirs(frames_dir, exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(channel="chrome")
    pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto("file://"+os.path.join(D,"piece1.html")); pg.wait_for_load_state("networkidle")
    pg.evaluate("document.fonts.ready")
    total=pg.evaluate("TOTAL"); n=int(total*FPS)
    for i in range(n):
        pg.evaluate(f"render({i/FPS})")
        pg.screenshot(path=os.path.join(frames_dir,f"{i:05d}.png"))
    b.close()
ff=imageio_ffmpeg.get_ffmpeg_exe()
mp4=os.path.join(OUT,"piece-1-inspiration.mp4")
subprocess.run([ff,"-y","-framerate",str(FPS),"-i",os.path.join(frames_dir,"%05d.png"),"-c:v","libx264","-pix_fmt","yuv420p","-crf","18","-movflags","+faststart",mp4],check=True,capture_output=True)
# GIF: 12fps, 540 wide, merge identical frames
imgs=[]; durs=[]
for i in range(0,n,3):
    im=Image.open(os.path.join(frames_dir,f"{i:05d}.png")).convert("RGB").resize((480,600),Image.LANCZOS)
    if imgs and list(im.getdata())==list(imgs[-1].getdata()): durs[-1]+=125
    else: imgs.append(im); durs.append(125)
pal=[im.quantize(colors=64,method=Image.MEDIANCUT) for im in imgs]
gif=os.path.join(OUT,"piece-1-inspiration.gif")
pal[0].save(gif,save_all=True,append_images=pal[1:],duration=durs,loop=0,optimize=True)
# stills: cover + key frames
for name,t in [("cover",20.5*FPS),("frame-2-vortex",8.8*FPS),("frame-4-climate",17*FPS),("frame-6-question",27*FPS)]:
    Image.open(os.path.join(frames_dir,f"{int(t):05d}.png")).save(os.path.join(OUT,f"piece-1-{name}.png"))
for f in sorted(os.listdir(OUT)): print(f, os.path.getsize(os.path.join(OUT,f))//1024,"KB")
