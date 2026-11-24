# SNS 홍보 키트: 팔로우 안내 + 봉사 모집 카드. 실행: python3 marketing/sns-kit/make.py
import base64, pathlib
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parents[2]; OUT = R/"marketing/sns-kit"
b64 = lambda f: base64.b64encode((R/"public/brand"/f).read_bytes()).decode()
TALL, WIDE = b64("hero-tall.jpg"), b64("hero-wide.jpg")
CH = [("Instagram","@orielfoundation"),("Telegram","t.me/oriel_foundation"),("LinkedIn","Oriel Foundation"),("Facebook","Oriel Foundation")]
T = {
 "follow": {
  "en": ("FOLLOW ORIEL", "Watch a small window<br>open, step by step.", "Every step of building Oriel, shared in public.", "orielfoundation.org/follow"),
  "ko": ("오리엘 소식 받기", "작은 창이 열리는 과정,<br>함께 지켜봐 주세요.", "재단을 만드는 모든 걸음을 공개로 나눕니다.", "orielfoundation.org/ko/follow")},
 "volunteer": {
  "en": ("VOLUNTEER TRIP · PHILIPPINES", "Come with us<br>this winter.", "5 days with a local Christian volunteer organisation. Reading, meals, small repairs, and a lot of listening. Thailand and Vietnam next.", "Apply in 1 minute → orielfoundation.org/volunteer"),
  "ko": ("봉사 여행 · 필리핀", "이번 겨울,<br>같이 가요.", "현지 기독교 봉사 단체와 함께하는 5일. 책 읽기, 식사 나눔, 작은 수리, 그리고 많이 듣기. 다음은 태국·베트남.", "1분 신청 → orielfoundation.org/ko/volunteer")},
}
def html(kind, lang, w, h):
    kick, head, sub, foot = T[kind][lang]
    big = h >= 1350
    bg = TALL if h > w else WIDE
    chans = "".join(f'<div class="c"><b>{n}</b><span>{x}</span></div>' for n,x in CH) if kind=="follow" else ""
    hs = (96 if h==1920 else 84) if big else 54
    return f"""<html><head><style>
*{{margin:0;box-sizing:border-box}} body{{width:{w}px;height:{h}px;overflow:hidden;font-family:Inter,'Noto Sans CJK KR','Noto Sans KR',sans-serif;color:#161514;position:relative;background:#E8CDBB;word-break:keep-all}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{bg}) center/cover;opacity:.9}}
.wrap{{position:absolute;inset:{'72px' if big else '48px'};display:flex;flex-direction:column;justify-content:flex-end}}
.wm{{position:absolute;top:0;left:0;font:800 {64 if big else 40}px/1 Inter;letter-spacing:-.04em}}
.k{{font:700 {26 if big else 18}px/1 Inter;letter-spacing:.06em;margin-bottom:{22 if big else 14}px}}
.h{{font-weight:800;font-size:{hs}px;line-height:1.05;letter-spacing:{'-.02em' if lang=='ko' else '-.03em'}}}
.s{{font-size:{30 if big else 20}px;line-height:1.45;font-weight:500;margin-top:{24 if big else 14}px;max-width:{900 if big else 760}px}}
.cs{{margin-top:{34 if big else 18}px;display:grid;grid-template-columns:1fr 1fr;gap:{14 if big else 8}px}}
.c{{border:2px solid #161514;padding:{18 if big else 10}px {20 if big else 12}px;background:rgba(255,255,255,.35)}}
.c b{{display:block;font-size:{28 if big else 18}px}} .c span{{font-size:{22 if big else 15}px;opacity:.8}}
.f{{margin-top:{30 if big else 18}px;padding-top:{20 if big else 12}px;border-top:2px solid #161514;font:700 {28 if big else 19}px/1.2 Inter}}
</style></head><body><div class="bg"></div><div class="wrap">
<div class="k">{kick}</div><div class="h">{head}</div><div class="s">{sub}</div>{f'<div class="cs">{chans}</div>' if chans else ''}<div class="f">{foot}</div></div></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for kind in T:
        for lang in ("en","ko"):
            for tag,(w,h) in {"portrait":(1080,1350),"story":(1080,1920),"wide":(1200,675)}.items():
                pg = b.new_page(viewport={"width":w,"height":h}); pg.set_content(html(kind,lang,w,h)); pg.wait_for_timeout(200)
                pg.screenshot(path=str(OUT/f"{kind}-{lang}-{tag}.jpg"), type="jpeg", quality=90); pg.close()
    b.close()
print("ok")
