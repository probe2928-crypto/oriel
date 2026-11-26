# 2026-11-26 저녁 게시: 봉사자 안내 Q&A(목요일 · GivingTuesday D-5). 실행: python3 marketing/instagram/2026-11-26-pm/make.py
import base64, pathlib
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parents[3]; OUT = pathlib.Path(__file__).parent
BG = base64.b64encode((R/"public/brand/hero-tall.jpg").read_bytes()).decode()
C = [
 ("VOLUNTEER GUIDE · GIVINGTUESDAY D-5", "5 days in the<br>Philippines.<br>What would<br>you actually do?", "Our first volunteer trip is this winter. Here are honest answers to the questions people ask us most.", "5일 봉사, 실제로 무엇을 하나요? — 봉사자 안내, 저장해 두세요"),
 ("Q. WHAT WILL I DO?", "Help with what<br>our local partner<br>already runs.", "Reading and English sessions alongside their teachers. Sharing meals. Carrying supplies. Tidying classrooms and small repairs. Listening and learning.", "현지 단체가 이미 하는 일을 돕습니다. 선생님들과 책 읽기·영어 시간, 식사 나눔, 물품 나르기, 교실 정리·작은 수리"),
 ("Q. HOW ARE CHILDREN KEPT SAFE?", "Never alone<br>with a child.", "We meet children only alongside partner staff and follow their child-protection rules. No orphanage visits. Every volunteer reads our safeguarding policy and signs our code of conduct before the trip.", "아이는 현지 파트너와 함께 있을 때만. 단둘이 있는 일 없음, 보육원 방문 없음. 출발 전 아동보호 정책을 읽고 행동강령에 서명"),
 ("Q. WHO CAN COME?", "Anyone with<br>a warm heart.", "No experience needed. Teachers, students, parents, nurses, builders. People of faith or not. Costs, age requirements and what to pack will come with the trip details.", "경험 없어도 괜찮아요. 신앙이 있든 없든 환영. 비용·참가 나이·준비물은 일정 확정 때 함께 안내"),
 ("Q. WHEN, AND HOW DO I JOIN?", "This winter.<br>Dates being<br>finalised.", "On GivingTuesday, Dec 1, we are not asking for money. We are asking for time. Tell us you are interested in one minute. Link in profile.", "12/1 나눔의 날, 오리엘은 돈 대신 시간을 부탁해요. 날짜·지역 확정 중 — 프로필 링크에서 1분 신청"),
]
def html(i, k, h, s, ko):
    return f"""<html><head><style>
*{{margin:0;box-sizing:border-box}} body{{width:1080px;height:1350px;overflow:hidden;font-family:Inter,'Noto Sans CJK KR','Noto Sans KR',sans-serif;color:#161514;position:relative;background:#E8CDBB;word-break:keep-all}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{BG}) center/cover;opacity:.9}}
.wm{{position:absolute;top:72px;left:72px;font:800 44px/1 Inter;letter-spacing:-.04em}}
.n{{position:absolute;top:80px;right:72px;font:700 26px/1 Inter}}
.wrap{{position:absolute;inset:72px;display:flex;flex-direction:column;justify-content:flex-end}}
.k{{font:700 26px/1 Inter;letter-spacing:.06em;margin-bottom:22px}}
.h{{font-weight:800;font-size:{92 if i==0 else 88}px;line-height:1.04;letter-spacing:-.03em}}
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
