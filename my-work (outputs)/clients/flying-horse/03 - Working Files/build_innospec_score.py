"""Original cinematic score for the Innospec film. One chord per shot, builds to a resolve on the end card."""
import numpy as np, wave, sys

SR = 44100
TOTAL = 34.5
N = int(SR * TOTAL)
rng = np.random.default_rng(7)

def hz(m): return 440.0 * 2 ** ((m - 69) / 12)
# MIDI: D2=38, D3=50, D4=62
CH = {  # (bass, [voicing])
    "D":  (38, [50, 57, 62, 66, 69]),
    "Bm": (35, [47, 54, 59, 62, 66]),
    "G":  (31, [43, 50, 55, 59, 62]),
    "Em": (40, [52, 55, 59, 64, 67]),
    "A":  (33, [45, 52, 57, 61, 64]),
    "Dhi": (38, [50, 57, 62, 66, 69, 74, 78]),
}
TIMES = [0.0, 4.6, 8.6, 12.4, 15.8, 18.8, 21.8, 25.4, 29.4, TOTAL]
PROG = ["D", "Bm", "G", "D", "Bm", "G", "Em", "A", "Dhi"]
# overall intensity per section (0..1)
LEVEL = [0.30, 0.36, 0.44, 0.50, 0.56, 0.62, 0.70, 0.86, 1.00]

t = np.arange(N) / SR
L = np.zeros(N); R = np.zeros(N)

def env_seg(a, b, att, rel, n):
    """smooth envelope for [a,b] with crossfade tails"""
    e = np.zeros(n)
    i0, i1 = int(a * SR), min(n, int((b + rel) * SR))
    tt = np.arange(i1 - i0) / SR
    up = np.clip(tt / att, 0, 1); up = 0.5 - 0.5 * np.cos(np.pi * up)
    dn = np.clip(((b + rel) - (a + tt)) / rel, 0, 1); dn = 0.5 - 0.5 * np.cos(np.pi * dn)
    e[i0:i1] = up * dn
    return e

def string(freq, dur_idx, detune):
    """band-limited saw ensemble (3 detuned voices) with vibrato"""
    out = np.zeros(dur_idx.size)
    tt = t[dur_idx]
    for d in (-detune, 0, detune):
        f = freq * (1 + d) * (1 + 0.0025 * np.sin(2 * np.pi * 5.1 * tt + rng.random() * 6))
        ph = 2 * np.pi * np.cumsum(f) / SR + rng.random() * 6
        nh = max(1, min(14, int(6000 / freq)))
        for h in range(1, nh + 1):
            out += np.sin(h * ph) / h * (0.92 ** h)
    return out / 3

for k, name in enumerate(PROG):
    a, b = TIMES[k], TIMES[k + 1]
    last = k == len(PROG) - 1
    rel = 3.5 if last else 1.4
    e = env_seg(a, b if not last else TOTAL - 0.8, 1.2 if k else 2.5, rel if not last else 0.8, N)
    idx = np.nonzero(e)[0]
    if idx.size == 0: continue
    bass, voices = CH[name]
    lvl = LEVEL[k]
    # strings pad
    for j, m in enumerate(voices):
        s = string(hz(m), idx, 0.004) * e[idx] * (0.055 + 0.02 * lvl)
        pan = 0.3 + 0.4 * (j / max(1, len(voices) - 1))
        L[idx] += s * (1 - pan) * lvl * 1.6; R[idx] += s * pan * lvl * 1.6
    # low strings / bass
    sb = (string(hz(bass + 12), idx, 0.003) * 0.6 + np.sin(2 * np.pi * hz(bass) * t[idx]) * 0.8) * e[idx] * 0.09 * (0.5 + lvl)
    L[idx] += sb; R[idx] += sb
    # horn-like line on the upper chord tone from shot 3 on, swelling
    if k >= 2:
        m = voices[-1] if not last else 74
        ph = 2 * np.pi * hz(m) * t[idx]
        horn = (np.sin(ph) + 0.45 * np.sin(2 * ph) + 0.25 * np.sin(3 * ph) + 0.12 * np.sin(4 * ph))
        he = env_seg(a + 0.3, (b if not last else TOTAL - 1.0) - 0.2, 1.6, 1.2, N)[idx]
        L[idx] += horn * he * 0.035 * lvl; R[idx] += horn * he * 0.045 * lvl
    # soft piano-like arpeggio pulse (eighths at ~84 bpm) for motion, sections 1..7
    if 1 <= k <= 7:
        step = 60 / 84 / 2
        notes = voices[1:4] + voices[2:3]
        n_i = 0; tt0 = a + 0.1
        while tt0 < b - 0.1:
            m = notes[n_i % len(notes)] + 12
            i0 = int(tt0 * SR); ln = int(1.6 * SR); i1 = min(N, i0 + ln)
            x = np.arange(i1 - i0) / SR
            tone = (np.sin(2 * np.pi * hz(m) * x) + 0.3 * np.sin(4 * np.pi * hz(m) * x)) * np.exp(-x * 3.2) * np.clip(x / 0.004, 0, 1)
            amp = 0.028 * (0.6 + lvl * 0.5)
            p = 0.35 if n_i % 2 else 0.65
            L[i0:i1] += tone * amp * (1 - p); R[i0:i1] += tone * amp * p
            n_i += 1; tt0 += step

def drum(at, amp, f0=55, decay=2.2, noise=0.25):
    i0 = int(at * SR); ln = int(3.0 * SR); i1 = min(N, i0 + ln)
    x = np.arange(i1 - i0) / SR
    f = f0 * (1 + 0.6 * np.exp(-x * 25))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * decay)
    nz = rng.standard_normal(x.size) * np.exp(-x * 18) * noise
    s = (body + nz) * amp
    L[i0:i1] += s; R[i0:i1] += s

# timpani roll building into the resolve, then the big hit on the end card
roll_t = np.arange(26.8, 29.35, 0.09)
for i, tt0 in enumerate(roll_t):
    drum(tt0, 0.02 + 0.10 * (i / len(roll_t)) ** 2, f0=73.4, decay=6, noise=0.15)
for at, amp in [(0.02, 0.12), (12.4, 0.08), (25.4, 0.14), (29.4, 0.38)]:
    drum(at, amp, f0=73.4 if at < 29 else 36.7 * 2, decay=1.6 if at >= 29 else 2.5)
# cymbal swell into the resolve
i0, i1 = int(27.4 * SR), int(29.45 * SR)
x = np.linspace(0, 1, i1 - i0)
sw = rng.standard_normal(i1 - i0)
sw = np.diff(np.concatenate([[0], sw]))  # brighten
L[i0:i1] += sw * x ** 3 * 0.018; R[i0:i1] += sw * x ** 3 * 0.018

# reverb: stereo convolution with decaying noise IR
def reverb(sig, seed):
    r = np.random.default_rng(seed)
    ln = int(2.8 * SR); xx = np.arange(ln) / SR
    ir = r.standard_normal(ln) * np.exp(-xx * 2.3)
    ir[:int(0.02 * SR)] = 0; ir /= np.sqrt(np.sum(ir ** 2))
    nfft = 1 << int(np.ceil(np.log2(sig.size + ln)))
    wet = np.fft.irfft(np.fft.rfft(sig, nfft) * np.fft.rfft(ir, nfft), nfft)[:sig.size]
    return sig * 0.72 + wet * 0.38
L, R = reverb(L, 1), reverb(R, 2)

# gentle master: fade in/out, soft clip, normalize
fade = np.minimum(np.clip(t / 1.2, 0, 1), np.clip((TOTAL - t) / 2.2, 0, 1))
L *= fade; R *= fade
peak = np.percentile(np.abs(np.concatenate([L, R])), 99.95)
L, R = np.tanh(L / peak * 1.3) / np.tanh(1.3) * 0.89, np.tanh(R / peak * 1.3) / np.tanh(1.3) * 0.89
st = np.stack([L, R], 1)
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes())
print("wrote", sys.argv[1])
