import os
from playwright.sync_api import sync_playwright
# prints report.html to PDF, plus page previews for checking
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(D)
PDF = os.path.join(OUT, "Thoughtware Before Software - Kate Burda & Co.pdf")
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page()
    pg.goto(f"file://{D}/report.html"); pg.wait_for_load_state("networkidle")
    pg.evaluate("document.fonts.ready")
    pg.pdf(path=PDF, width="8.5in", height="11in", print_background=True, prefer_css_page_size=True)
    pv = b.new_page(viewport={"width": 816, "height": 1056}, device_scale_factor=1)
    pv.goto(f"file://{D}/report.html"); pv.wait_for_load_state("networkidle"); pv.evaluate("document.fonts.ready")
    n = pv.evaluate("document.querySelectorAll('.page').length")
    for i in range(n):
        el = pv.query_selector_all(".page")[i]
        el.screenshot(path=os.path.join(D, f"preview-{i+1}.png"))
    b.close()
print(PDF, os.path.getsize(PDF)//1024, "KB", n, "pages")
