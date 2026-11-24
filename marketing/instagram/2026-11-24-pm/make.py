# 2026-11-24 저녁 게시: 현지 파트너를 고르는 기준(화요일 · 파트너 이야기). 실행: python3 marketing/instagram/2026-11-24-pm/make.py
import base64, pathlib
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parents[3]; OUT = pathlib.Path(__file__).parent
BG = base64.b64encode((R/"public/brand/hero-tall.jpg").read_bytes()).decode()
C = [
 ("HOW WE CHOOSE A PARTNER", "Before we go,<br>we choose who<br>we go with.", "We never serve alone. Every Oriel trip works with a local volunteer organisation. Here is what we look for.", "현지 파트너를 고르는 기준 — 저장해 두세요"),
 ("CRITERION 1", "Led by local<br>people.", "People who know the community by name, and who will still be there long after a 5-day team flies home.", "그 동네를 잘 알고, 우리가 떠난 뒤에도 남아 있는 현지 사람들이 이끄는 곳"),
 ("CRITERION 2", "A written child<br>protection policy.", "We follow their rules. We meet children only with partner staff present. No volunteer is ever alone with a child. No orphanage visits.", "서면 아동보호 정책이 있는 곳. 아이는 현지 파트너와 함께 있을 때만, 단둘이 없음, 보육원 방문 없음"),
 ("CRITERION 3", "Rooted in faith,<br>open to all.", "We work with Christian volunteer organisations that serve every family, whatever they believe. No pressure, ever.", "기독교 정신으로 세운 단체, 그러나 믿음과 상관없이 모든 가정을 섬기는 곳. 강요 없음"),
 ("WHERE WE ARE", "Still listening.<br>Not yet signed.", "We are talking with candidates in the Philippines. When a partner says yes, we will introduce them here, with their permission. Want to come this winter? Link in profile.", "필리핀 후보 단체들과 이야기 중입니다. 허락받으면 여기서 소개할게요. 겨울 봉사 신청은 프로필 링크"),
]
def html(i, k, h, s, ko):
    return f"""<html><head><style>
*{{margin:0;box-sizing:border-box}} body{{width:1080px;height:1350px;overflow:hidden;font-family:Inter,'Noto Sans CJK KR','Noto Sans KR',sans-serif;color:#161514;position:relative;background:#E8CDBB;word-break:keep-all}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{BG}) center/cover;opacity:.9}}
.wm{{position:absolute;top:72px;left:72px;font:800 44px/1 Inter;letter-spacing:-.04em}}
.n{{position:absolute;top:80px;right:72px;font:700 26px/1 Inter}}
.wrap{{position:absolute;inset:72px;display:flex;flex-direction:column;justify-content:flex-end}}
.k{{font:700 26px/1 Inter;letter-spacing:.06em;margin-bottom:22px}}
.h{{font-weight:800;font-size:{96 if i==0 else 88}px;line-height:1.04;letter-spacing:-.03em}}
.s{{font-size:32px;line-height:1.45;font-weight:500;margin-top:26px;max-width:900px}}
.f{{margin-top:30px;padding-top:20px;border-top:2px solid #161514;font-size:27px;line-height:1.4;font-weight:700}}
</style></head><body><div class="bg"></div><div class="wrap">
<div class="k">{i+1}/5 · {k}</div><div class="h">{h}</div><div class="s">{s}</div><div class="f">{ko}</div></div></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for i, c in enumerate(C):
        pg = b.new_page(viewport={"width":1080,"height":1350}); pg.set_content(html(i,*c)); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT/f"{i+1}.jpg"), type="jpeg", quality=90); pg.close()
    b.close()
print("ok")
