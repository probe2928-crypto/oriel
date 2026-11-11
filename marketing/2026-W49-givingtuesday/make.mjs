// GivingTuesday(12/1) 창 이미지 — 링크드인·인스타 세로(1080×1350), 텔레그램·X 가로(1200×675)
// 실행: NODE_PATH=$(npm root -g) node marketing/2026-W49-givingtuesday/make.mjs
// 먼저 node scripts/build.mjs (워드마크를 dist/index.html 에서 가져옴)
// 필요: ~/.fonts 의 FamiljenGrotesk[wght].ttf · NotoSansKR[wght].ttf · NotoSansTC[wght].ttf (scripts/og.mjs 와 같음)
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "../..");
const { chromium } = createRequire(import.meta.url)("playwright");
const FD = path.join(os.homedir(), ".fonts");
const face = (fam, file) => fs.existsSync(path.join(FD, file)) ? `@font-face{font-family:"${fam}";src:url(data:font/ttf;base64,${fs.readFileSync(path.join(FD, file)).toString("base64")});font-weight:100 900}` : "";
const FONTS = face("Familjen Grotesk", "FamiljenGrotesk[wght].ttf") + face("Noto Sans KR", "NotoSansKR[wght].ttf") + face("Noto Sans TC", "NotoSansTC[wght].ttf");
const WM = fs.readFileSync(path.join(ROOT, "dist", "index.html"), "utf8").match(/<svg class="brand-wm"[\s\S]*?<\/svg>/)[0].replace('class="brand-wm"', 'class="wm"');
const img = (f) => fs.readFileSync(path.join(ROOT, "public", "brand", f)).toString("base64");

const TEXT = {
  en: { kick: "GivingTuesday · 1 December 2026", head: "Today we are not asking for money.", sub: "We are asking you to watch the window: every gift on the record, from the first one, once we are registered.", zh: "今天我們不募款，只請你一起看著這扇窗。", foot: "Oriel Foundation · In formation · Not taking donations yet" },
  ko: { kick: "GivingTuesday · 2026년 12월 1일", head: "오늘 오리엘은 돈을 요청하지 않습니다.", sub: "대신 이 창을 함께 지켜봐 주세요. 등록 후 첫 기부부터 모든 기록을 공개합니다.", zh: "今天我們不募款，只請你一起看著這扇窗。", foot: "오리엘 재단 · 설립 준비 중 · 아직 기부를 받지 않습니다" },
};

function html(lang, w, h) {
  const t = TEXT[lang], tall = h > w;
  const fam = lang === "ko" ? '"Noto Sans KR","Familjen Grotesk"' : '"Familjen Grotesk","Noto Sans KR"';
  return `<!doctype html><meta charset="utf-8"><style>${FONTS}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:${w}px;height:${h}px;overflow:hidden}
body{word-break:${lang === "ko" ? "keep-all" : "normal"};background:#E3CAB6;color:#161514;font-family:${fam},sans-serif;-webkit-font-smoothing:antialiased}
${tall ? `.bg{position:absolute;inset:0;background:url(data:image/jpeg;base64,${img("hero-tall.jpg")}) center 30%/cover}` : `.bg{position:absolute;top:0;right:0;width:440px;height:${h}px;background:url(data:image/jpeg;base64,${img("path-learn.jpg")}) center 62%/cover}.bg::before{content:"";position:absolute;inset:0 auto 0 0;width:90px;background:linear-gradient(90deg,#E3CAB6,rgba(227,202,182,0))}.wm{position:absolute;left:64px;top:52px;width:130px;height:auto;fill:#161514}`}
.box{position:absolute;left:${tall ? 72 : 64}px;right:${tall ? 72 : 520}px;bottom:${tall ? 132 : 110}px}
.kick{font-weight:600;font-size:${tall ? 30 : 24}px;margin-bottom:${tall ? 26 : 18}px}
.head{font-weight:700;font-size:${tall ? 76 : 46}px;line-height:1.06;letter-spacing:${lang === "ko" ? "-.02em" : "-.025em"};text-wrap:balance}
.sub{margin-top:${tall ? 28 : 18}px;font-size:${tall ? 32 : 22}px;line-height:1.38;font-weight:500;text-wrap:pretty}
.zh{margin-top:${tall ? 22 : 14}px;font-family:"Noto Sans TC",sans-serif;font-size:${tall ? 28 : 20}px;font-weight:500}
.foot{position:absolute;left:${tall ? 72 : 64}px;right:${tall ? 72 : 520}px;bottom:${tall ? 56 : 40}px;padding-top:16px;border-top:1.5px solid rgba(22,21,20,.4);font-weight:600;font-size:${tall ? 24 : 18}px}
</style><div class="bg"></div>${tall ? "" : WM}<div class="box"><div class="kick">${t.kick}</div><div class="head">${t.head}</div><div class="sub">${t.sub}</div><div class="zh">${t.zh}</div></div><div class="foot">${t.foot}</div>`;
}

const browser = await chromium.launch();
for (const lang of ["en", "ko"]) for (const [w, h, tag] of [[1080, 1350, "portrait"], [1200, 675, "wide"]]) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  await page.setContent(html(lang, w, h));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(HERE, `givingtuesday-${lang}-${tag}.jpg`), type: "jpeg", quality: 88 });
  await page.close();
}
await browser.close();
console.log("givingtuesday images → " + HERE);
