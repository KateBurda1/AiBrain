import os
from playwright.sync_api import sync_playwright

# renders both coin faces to transparent PNGs, then prints the report to PDF plus page previews
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(D)
PDF = os.path.join(OUT, "Right, or Just Lucky - Kate Burda & Co.pdf")

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1100, "height": 1100}, device_scale_factor=2)
    for side in ["right", "lucky"]:
        pg.goto(f"file://{D}/coin.html?side={side}"); pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=os.path.join(D, f"coin-{side}.png"), omit_background=True)
    pg = b.new_page()
    pg.goto(f"file://{D}/report.html"); pg.wait_for_load_state("networkidle")
    pg.evaluate("document.fonts.ready")
    pg.pdf(path=PDF, width="8.5in", height="11in", print_background=True, prefer_css_page_size=True)
    b.close()
print(PDF, os.path.getsize(PDF) // 1024, "KB")
