# 2026-11-27 아침 게시: 회의 결정 ② '기억해 둘 숫자 하나' +20% (GivingTuesday D-4). 실행: python3 marketing/instagram/2026-11-27-am/make.py
import base64, pathlib
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parents[3]; OUT = pathlib.Path(__file__).parent
BG = base64.b64encode((R/"public/brand/hero-tall.jpg").read_bytes()).decode()
def html(w, h, big, fs):
    return f"""<html><head><style>
*{{margin:0;box-sizing:border-box}} body{{width:{w}px;height:{h}px;overflow:hidden;font-family:Inter,'Noto Sans CJK KR','Noto Sans KR',sans-serif;color:#161514;position:relative;background:#E8CDBB;word-break:keep-all}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{BG}) center/cover;opacity:.9}}
.wrap{{position:absolute;inset:{64 if w>h else 72}px;display:flex;flex-direction:column;justify-content:flex-end}}
.k{{font:700 {22 if w>h else 26}px/1 Inter;letter-spacing:.06em;margin-bottom:18px}}
.big{{font-weight:800;font-size:{big}px;line-height:.95;letter-spacing:-.05em}}
.s{{font-size:{fs}px;line-height:1.35;font-weight:700;margin-top:20px;max-width:{w-160}px}}
.f{{margin-top:22px;padding-top:16px;border-top:2px solid #161514;font-size:{fs-6}px;line-height:1.4;font-weight:600}}
</style></head><body><div class="bg"></div><div class="wrap">
<div class="k">GOOD MORNING · GIVINGTUESDAY D-4 · DEC 1</div>
<div class="big">+20%</div>
<div class="s">작년 GivingTuesday 자원봉사 참여, 전년보다 20% 늘었어요.<br>Volunteering on GivingTuesday grew 20% last year.</div>
<div class="f">출처 Source: GivingTuesday 2025 results · oriel</div></div></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, w, h, big, fs in [("01-portrait.jpg",1080,1350,300,38),("02-wide.jpg",1200,675,220,30)]:
        pg = b.new_page(viewport={"width":w,"height":h}); pg.set_content(html(w,h,big,fs)); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT/name), type="jpeg", quality=90); pg.close()
    b.close()
print("ok")
