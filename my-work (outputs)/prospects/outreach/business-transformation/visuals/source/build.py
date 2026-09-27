import os, subprocess, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ["OUT"]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1080, 1350

CSS = """
@page { size: 1080px 1350px; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: #0b0b0b; }
.slide { width: 1080px; height: 1350px; position: relative; overflow: hidden;
  background: #0b0b0b; color: #f4f1ee; page-break-after: always;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }
.inner { position: absolute; left: 96px; right: 130px; top: 120px; bottom: 200px;
  display: flex; flex-direction: column; justify-content: center; }
.eyebrow { position: absolute; left: 96px; top: 96px; color: #d53d72;
  font-size: 22px; font-weight: 700; letter-spacing: 6px; }
.rule { width: 72px; height: 6px; background: #d53d72; margin-bottom: 44px; }
h1 { color: #d53d72; font-weight: 800; line-height: 1.02; letter-spacing: -2px; }
.xl h1 { font-size: 112px; } .l h1 { font-size: 92px; } .m h1 { font-size: 76px; }
.quote h1 { font-weight: 700; font-style: italic; }
p { margin-top: 44px; font-size: 44px; line-height: 1.25; color: #f4f1ee; font-weight: 400; }
p b { color: #fff; font-weight: 700; }
.stats { display: flex; flex-direction: column; gap: 28px; }
.stat { display: flex; align-items: baseline; gap: 28px; }
.num { color: #d53d72; font-size: 160px; font-weight: 800; letter-spacing: -6px; line-height: 1; }
.lbl { font-size: 44px; font-weight: 700; color: #f4f1ee; }
.side { position: absolute; right: 40px; top: 50%; transform: translateY(-50%);
  writing-mode: vertical-rl; color: #6d6a67; font-size: 20px; letter-spacing: 5px; white-space: nowrap; }
.foot { position: absolute; left: 96px; bottom: 90px; color: #bdb8b3; font-size: 26px; letter-spacing: 2px; }
.logoclip { position: absolute; right: 96px; bottom: 66px; width: 250px; height: 118px; overflow: hidden; }
.logo { position: absolute; height: 516px; left: -76px; top: -200px; filter: invert(1); mix-blend-mode: screen; }
.count { position: absolute; right: 96px; top: 92px; color: #6d6a67; font-size: 24px; letter-spacing: 3px; }
.arrow { color: #d53d72; }
"""

def slide(h1, body="", size="l", extra="", count=None, stats=None, quote=False):
    cls = f"slide {size}" + (" quote" if quote else "")
    content = ""
    if stats:
        content = '<div class="stats">' + "".join(
            f'<div class="stat"><span class="num">{n}</span><span class="lbl">{l}</span></div>' for n, l in stats) + "</div>"
    if h1:
        content += f"<h1>{h1}</h1>"
    if body:
        content += f"<p>{body}</p>"
    cnt = f'<div class="count">{count}</div>' if count else ""
    return f"""<section class="{cls}">
  <div class="eyebrow">COMMERCIAL EXCELLENCE</div>{cnt}
  <div class="inner"><div class="rule"></div>{content}</div>
  <div class="side">@KATEBURDA.COM</div>
  <div class="foot">kateburda.com</div>
  <div class="logoclip"><img class="logo" src="kb_Logo_5.Black_Primary.png"></div>
</section>"""

POSTS = {
 "post-1-revenue-problem": [
   slide("Your transformation has a revenue problem.", "", "xl", count="1 / 5"),
   slide("New systems. New structure. New operating model.", "Same sales playbook.", "l", count="2 / 5"),
   slide("Revenue doesn't transform because the org chart did.", "", "l", count="3 / 5"),
   slide("The commercial team is where strategy meets the customer.",
         "If they aren't transformed too, that's where the whole thing stalls.", "m", count="4 / 5"),
   slide("Transform the business. Direct the commercial team through it.",
         "<b>Same time.</b>", "m", count="5 / 5"),
 ],
 "post-2-who-told-sales": [
   slide("Six months in the War Room. 45 minutes for sales.",
         "Then we wonder why revenue didn't move.", "l"),
 ],
 "post-3-2019-playbook": [
   slide("&ldquo;If we want 2019 results, we'll do what we did in 2019.&rdquo;",
         "The weather changed. <b>Did your playbook?</b>", "m", quote=True),
 ],
 "post-4-busy-with-a-budget": [
   slide("", "Per month. That's not transformation. <b>That's a report about one.</b>", "m",
         stats=[("2 hrs", "reporting"), ("15 min", "coaching")]),
 ],
 "post-5-silent-saboteur": [
   slide("The silent saboteur has a quota.", "", "xl", count="1 / 4"),
   slide("Transformations don't fail in the plan.", "They fail in the handoff.", "l", count="2 / 4"),
   slide("The handoff runs through your commercial team.",
         "They take the strategy to the customer. <b>Who built the bridge for them?</b>", "m", count="3 / 4"),
   slide("Do less. Make it mean more.",
         "Start with the team that brings in the revenue.", "l", count="4 / 4"),
 ],
}

def page(sections):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(sections)}</body></html>'

def chrome(args):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--no-pdf-header-footer"] + args,
                   check=True, capture_output=True)

os.makedirs(OUT, exist_ok=True)
for name, sections in POSTS.items():
    for i, s in enumerate(sections, 1):
        f = os.path.join(HERE, f"{name}-{i}.html")
        open(f, "w").write(page([s]))
        png = os.path.join(OUT, f"{name}-slide-{i}.png" if len(sections) > 1 else f"{name}.png")
        chrome([f"--window-size={W},{H}", f"--screenshot={png}", "file://" + f])
        print(png)
    if len(sections) > 1:
        f = os.path.join(HERE, f"{name}-all.html")
        open(f, "w").write(page(sections))
        pdf = os.path.join(OUT, f"{name}-carousel.pdf")
        chrome([f"--print-to-pdf={pdf}", "file://" + f])
        print(pdf)
