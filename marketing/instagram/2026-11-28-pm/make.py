# 2026-11-28 저녁 게시: 토요일 참여형 "같이 간다면, 무엇을 해보고 싶나요?" (A·B·C·D 고르기 · GivingTuesday D-3). 실행: python3 marketing/instagram/2026-11-28-pm/make.py
import base64, pathlib
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parents[3]; OUT = pathlib.Path(__file__).parent
BG = base64.b64encode((R/"public/brand/hero-tall.jpg").read_bytes()).decode()
C = [
 ("SATURDAY QUESTION · GIVINGTUESDAY D-3", "If you came<br>with us, what<br>would you<br>pick?", "Our first volunteer trip, 5 days in the Philippines, is this winter. Swipe and choose one. Then tell us in the comments.", "같이 간다면, 무엇을 해보고 싶나요? 넘겨 보고 하나만 골라 주세요"),
 ("A or B?", "A. Reading time<br>B. Meals &amp; supplies", "A. Reading and English sessions. B. Sharing meals and carrying supplies. Both alongside what our local partner organisation already runs, with their teachers and staff.", "A. 현지 선생님들과 함께하는 책 읽기·영어 시간 · B. 식사 나눔과 물품 나르기"),
 ("C or D?", "C. Tidy &amp; fix<br>D. Your own skill", "C. Tidying classrooms and small repairs. D. Something you are good at: nursing, music, photography, design. Tell us what.", "C. 교실 정리와 작은 수리 · D. 나만의 재능(간호·음악·사진·디자인 등) — 무엇인지 알려 주세요"),
 ("WHICHEVER YOU PICK", "Never alone<br>with a child.", "We meet children only alongside our local partner and follow their child-protection rules. No orphanage visits. Every volunteer signs our code of conduct first.", "무엇을 고르든: 아이는 현지 파트너와 함께 있을 때만. 단둘이 없음, 보육원 방문 없음"),
 ("YOUR TURN", "Comment<br>A, B, C or D.", "Dates and region are being finalised. Oriel is still in formation and does not accept donations. Want to come? Link in profile, or DM us.", "댓글로 A·B·C·D 한 글자만! 날짜·지역 확정 중 · 함께 가고 싶다면 프로필 링크"),
]
def html(i, k, h, s, ko):
    return f"""<html><head><style>
*{{margin:0;box-sizing:border-box}} body{{width:1080px;height:1350px;overflow:hidden;font-family:Inter,'Noto Sans CJK KR','Noto Sans KR',sans-serif;color:#161514;position:relative;background:#E8CDBB;word-break:keep-all}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{BG}) center/cover;opacity:.9}}
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
