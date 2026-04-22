import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="핀핏 FinFit",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    section[data-testid="stMain"] > div { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>핀핏 FinFit</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:-apple-system,'Apple SD Gothic Neo','Noto Sans KR',sans-serif;background:linear-gradient(135deg,#e8edf8,#dde3f5);display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:24px 16px;}
.phone{width:390px;max-width:100%;background:#f0f4ff;border-radius:40px;overflow:hidden;box-shadow:0 20px 60px rgba(59,91,219,.25);min-height:844px;display:flex;flex-direction:column;position:relative;}
.status-bar{background:#1a2a6c;height:12px;flex-shrink:0;}
.screen{display:none;flex-direction:column;flex:1;overflow:hidden;}
.screen.active{display:flex;}
.scroll-body{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch;}
/* buttons */
.btn-p{background:linear-gradient(135deg,#3b5bdb,#5c7cfa);color:#fff;border:none;border-radius:14px;padding:15px;font-size:16px;font-weight:700;cursor:pointer;width:100%;transition:opacity .2s;}
.btn-p:hover{opacity:.88;}
.btn-o{background:#fff;color:#3b5bdb;border:2px solid #3b5bdb;border-radius:14px;padding:12px;font-size:14px;font-weight:600;cursor:pointer;width:100%;margin-top:10px;}
/* cards */
.card{background:#fff;border-radius:18px;padding:18px;margin-bottom:12px;box-shadow:0 2px 12px rgba(59,91,219,.08);}
/* chips */
.chip{border:1.5px solid #dde3f5;border-radius:22px;padding:8px 15px;font-size:13px;cursor:pointer;background:#fff;color:#444;transition:all .15s;display:inline-block;margin:4px;}
.chip.on{background:#3b5bdb;color:#fff;border-color:#3b5bdb;font-weight:700;}
/* progress */
.prog-bar{height:4px;background:#e8edf8;border-radius:10px;margin-bottom:24px;}
.prog-fill{height:100%;border-radius:10px;background:linear-gradient(90deg,#3b5bdb,#5c7cfa);transition:width .4s;}
/* section title */
.sec-title{font-size:15px;font-weight:800;margin-bottom:10px;color:#1a1a2e;}
/* bottom nav */
.bnav{background:#fff;display:flex;justify-content:space-around;padding:10px 0 16px;border-top:1px solid #e8edf8;flex-shrink:0;}
.ni{display:flex;flex-direction:column;align-items:center;gap:3px;cursor:pointer;flex:1;}
.ni .ico{font-size:22px;}
.ni .lbl{font-size:10px;color:#aaa;font-weight:600;}
.ni.on .lbl{color:#3b5bdb;}
/* tooltip */
.tip{position:fixed;bottom:100px;left:50%;transform:translateX(-50%);background:#1a1a2e;color:#fff;padding:10px 20px;border-radius:20px;font-size:13px;opacity:0;transition:opacity .3s;pointer-events:none;z-index:999;white-space:nowrap;}
.tip.show{opacity:1;}
/* badge */
.badge{display:inline-block;background:#ff6b6b;color:#fff;font-size:10px;font-weight:700;padding:2px 7px;border-radius:10px;margin-left:6px;}
.tag{display:inline-block;font-size:11px;font-weight:700;padding:3px 9px;border-radius:12px;}
/* range input */
input[type=range]{-webkit-appearance:none;width:100%;height:6px;border-radius:3px;background:linear-gradient(90deg,#3b5bdb 50%,#dde3f5 50%);outline:none;}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:22px;height:22px;border-radius:50%;background:#3b5bdb;cursor:pointer;box-shadow:0 2px 6px rgba(59,91,219,.4);}
/* budget bar */
.bbar-wrap{height:8px;background:#f1f3f9;border-radius:6px;margin:6px 0;overflow:hidden;}
.bbar-fill{height:100%;border-radius:6px;transition:width .5s;}
/* tx item */
.tx{display:flex;justify-content:space-between;align-items:center;padding:11px 0;border-bottom:1px solid #f8f9ff;}
.tx:last-child{border-bottom:none;}
.tx-l{display:flex;gap:10px;align-items:center;}
.tx-ico{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}
.tx-name{font-size:13px;font-weight:600;}
.tx-date{font-size:11px;color:#aaa;}
.tx-amt{font-size:13px;font-weight:700;}
.minus{color:#e03131;}
.plus{color:#3b5bdb;}
/* modal */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:500;justify-content:center;align-items:flex-end;}
.modal-bg.show{display:flex;}
.modal{background:#fff;border-radius:24px 24px 0 0;padding:24px 20px 32px;width:100%;max-width:390px;max-height:80vh;overflow-y:auto;}
.modal-handle{width:40px;height:4px;background:#dde3f5;border-radius:2px;margin:0 auto 18px;}
/* benefit card */
.bc{background:#fff;border-radius:16px;padding:14px 16px;margin-bottom:10px;box-shadow:0 2px 10px rgba(59,91,219,.07);display:flex;gap:12px;align-items:flex-start;cursor:pointer;}
.bc-ico{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;}
.bc h4{font-size:13px;font-weight:700;margin-bottom:3px;}
.bc p{font-size:11px;color:#888;line-height:1.5;}
.bc .dl{font-size:10px;color:#e03131;font-weight:700;margin-top:4px;}
/* level card */
.lv-card{border-radius:12px;padding:14px 16px;margin-bottom:10px;border-left:5px solid;}
/* ai bubble */
.ai-bub{background:linear-gradient(135deg,#3b5bdb,#5c7cfa);color:#fff;border-radius:16px 16px 16px 4px;padding:12px 14px;font-size:12px;line-height:1.7;margin-bottom:12px;}
/* input */
.inp{border:1.5px solid #dde3f5;border-radius:12px;padding:11px 14px;font-size:14px;width:100%;outline:none;background:#fff;}
.inp:focus{border-color:#3b5bdb;}
/* tabs */
.tabs{display:flex;background:#fff;border-bottom:1px solid #e8edf8;flex-shrink:0;}
.tab{flex:1;padding:12px 0;text-align:center;font-size:12px;font-weight:600;color:#aaa;cursor:pointer;border-bottom:2px solid transparent;}
.tab.on{color:#3b5bdb;border-bottom-color:#3b5bdb;}
/* summary metric */
.metric{background:#fff;border-radius:14px;padding:14px;text-align:center;flex:1;}
.metric .mv{font-size:18px;font-weight:800;}
.metric .ml{font-size:11px;color:#888;margin-top:2px;}
/* glossary */
.glos-item{padding:14px 0;border-bottom:1px solid #f1f3f9;}
.glos-item:last-child{border-bottom:none;}
.glos-term{font-size:14px;font-weight:700;color:#3b5bdb;margin-bottom:4px;}
.glos-def{font-size:12px;color:#555;line-height:1.6;}
/* match tag */
.match-tag{font-size:10px;padding:2px 8px;border-radius:10px;font-weight:700;margin-left:6px;}
.match-y{background:#ebfbee;color:#087f5b;}
.match-n{background:#fff0f0;color:#e03131;}
/* score ring */
.score-ring{width:90px;height:90px;position:relative;margin:0 auto;}
.score-ring svg{transform:rotate(-90deg);}
.score-ring .sv{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:22px;font-weight:800;color:#3b5bdb;}
/* chart bars css */
.chart-bar-wrap{display:flex;align-items:flex-end;gap:6px;height:80px;margin-top:8px;}
.chart-bar{flex:1;border-radius:4px 4px 0 0;min-width:8px;transition:height .4s;}
.chart-lbl{display:flex;gap:6px;margin-top:4px;}
.chart-lbl span{flex:1;font-size:8px;color:#aaa;text-align:center;}
</style>
</head>
<body>
<div class="phone">
<div class="status-bar"></div>

<!-- ══════════════ SPLASH ══════════════ -->
<div id="s-splash" class="screen active" style="background:linear-gradient(160deg,#1a2a6c 0%,#3b5bdb 60%,#5c7cfa 100%);align-items:center;justify-content:center;text-align:center;padding:40px 28px;">
  <div style="width:100px;height:100px;border:3px solid rgba(255,255,255,.4);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 24px;font-size:42px;">💰</div>
  <h1 style="color:#fff;font-size:36px;font-weight:800;letter-spacing:-1px;">핀핏</h1>
  <p style="color:rgba(255,255,255,.7);font-size:14px;margin:10px 0 8px;line-height:1.6;">사회초년생을 위한 AI 금융 통합 플랫폼<br>군산시 청년 맞춤 혜택까지 한번에</p>
  <p style="color:rgba(255,255,255,.45);font-size:11px;margin-bottom:40px;">공공 API × AI × 청년 특화 UX</p>
  <button class="btn-p" style="width:80%;margin:0 auto;" onclick="go('s-ob1')">시작하기 →</button>
  <p style="color:rgba(255,255,255,.45);font-size:12px;margin-top:16px;cursor:pointer;" onclick="skipOnboard()">이미 계정이 있다면 로그인</p>
</div>

<!-- ══════════════ ONBOARD 1: 기본정보 ══════════════ -->
<div id="s-ob1" class="screen" style="background:#fff;overflow-y:auto;padding:28px 24px 30px;">
  <div class="prog-bar"><div class="prog-fill" style="width:25%"></div></div>
  <h2 style="font-size:22px;font-weight:800;line-height:1.4;">나이와 현재 상태를<br>알려주세요 👤</h2>
  <p style="color:#999;font-size:13px;margin:6px 0 22px;">맞춤 혜택 매칭의 첫 번째 단계예요</p>

  <label style="font-size:12px;font-weight:700;color:#555;display:block;margin-bottom:8px;">만 나이</label>
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:22px;">
    <input type="range" id="age-range" min="18" max="45" value="25" style="flex:1;" oninput="document.getElementById('age-val').textContent=this.value+'세'">
    <div id="age-val" style="font-size:18px;font-weight:800;color:#3b5bdb;min-width:48px;text-align:right;">25세</div>
  </div>

  <label style="font-size:12px;font-weight:700;color:#555;display:block;margin-bottom:10px;">현재 상태</label>
  <div id="status-grp" style="display:flex;flex-wrap:wrap;gap:0;margin-bottom:24px;">
    <span class="chip" onclick="sel(this,'status-grp')">🎓 재학생</span>
    <span class="chip on" onclick="sel(this,'status-grp')">📚 취업준비생</span>
    <span class="chip" onclick="sel(this,'status-grp')">💼 사회초년생</span>
    <span class="chip" onclick="sel(this,'status-grp')">🏢 직장인</span>
    <span class="chip" onclick="sel(this,'status-grp')">🌱 창업자</span>
    <span class="chip" onclick="sel(this,'status-grp')">🌾 농업종사</span>
  </div>

  <label style="font-size:12px;font-weight:700;color:#555;display:block;margin-bottom:10px;">주택 소유 여부</label>
  <div id="house-grp" style="display:flex;flex-wrap:wrap;margin-bottom:28px;">
    <span class="chip on" onclick="sel(this,'house-grp')">🏠 무주택</span>
    <span class="chip" onclick="sel(this,'house-grp')">🏡 유주택</span>
  </div>
  <button class="btn-p" onclick="go('s-ob2')">다음 →</button>
</div>

<!-- ══════════════ ONBOARD 2: 소득 ══════════════ -->
<div id="s-ob2" class="screen" style="background:#fff;overflow-y:auto;padding:28px 24px 30px;">
  <div class="prog-bar"><div class="prog-fill" style="width:50%"></div></div>
  <h2 style="font-size:22px;font-weight:800;line-height:1.4;">소득 정보를<br>입력해주세요 💰</h2>
  <p style="color:#999;font-size:13px;margin:6px 0 22px;">혜택 자격 기준을 정확히 매칭하기 위해 필요해요</p>

  <label style="font-size:12px;font-weight:700;color:#555;display:block;margin-bottom:8px;">월 소득 / 용돈</label>
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
    <input type="range" id="inc-range" min="0" max="500" step="10" value="200" style="flex:1;" oninput="updateIncome(this.value)">
    <div id="inc-val" style="font-size:16px;font-weight:800;color:#3b5bdb;min-width:80px;text-align:right;">200만원</div>
  </div>
  <p style="font-size:11px;color:#aaa;margin-bottom:22px;">0 = 없음 / 슬라이더로 설정</p>

  <label style="font-size:12px;font-weight:700;color:#555;display:block;margin-bottom:10px;">가구 소득 수준 (기준 중위소득)</label>
  <div id="inc-grp" style="display:flex;flex-wrap:wrap;margin-bottom:24px;">
    <span class="chip" onclick="sel(this,'inc-grp')">60% 이하</span>
    <span class="chip" onclick="sel(this,'inc-grp')">100% 이하</span>
    <span class="chip on" onclick="sel(this,'inc-grp')">140% 이하</span>
    <span class="chip" onclick="sel(this,'inc-grp')">150% 이하</span>
    <span class="chip" onclick="sel(this,'inc-grp')">180% 이하</span>
    <span class="chip" onclick="sel(this,'inc-grp')">소득 기준 초과</span>
  </div>

  <div style="background:#f0f4ff;border-radius:12px;padding:14px;margin-bottom:24px;">
    <p style="font-size:12px;color:#3b5bdb;font-weight:700;margin-bottom:6px;">💡 중위소득이 뭔가요?</p>
    <p style="font-size:11px;color:#555;line-height:1.6;">우리나라 모든 가구를 소득 순으로 줄 세웠을 때 딱 중간에 있는 가구의 소득이에요. 정부가 지원 대상을 정할 때 쓰는 기준이랍니다!</p>
  </div>
  <button class="btn-p" onclick="go('s-ob3')">다음 →</button>
  <button class="btn-o" onclick="go('s-ob1')">← 이전</button>
</div>

<!-- ══════════════ ONBOARD 3: 관심사 ══════════════ -->
<div id="s-ob3" class="screen" style="background:#fff;overflow-y:auto;padding:28px 24px 30px;">
  <div class="prog-bar"><div class="prog-fill" style="width:75%"></div></div>
  <h2 style="font-size:22px;font-weight:800;line-height:1.4;">관심 분야를<br>선택해주세요 🎯</h2>
  <p style="color:#999;font-size:13px;margin:6px 0 22px;">복수 선택 가능해요!</p>

  <div id="int-grp" style="display:flex;flex-wrap:wrap;margin-bottom:24px;">
    <span class="chip on" onclick="tog(this)">🏦 청년 금융상품</span>
    <span class="chip on" onclick="tog(this)">🏠 주거 지원</span>
    <span class="chip" onclick="tog(this)">💼 취업·구직</span>
    <span class="chip" onclick="tog(this)">📖 교육비 지원</span>
    <span class="chip on" onclick="tog(this)">💰 자산 형성</span>
    <span class="chip" onclick="tog(this)">🧠 심리·복지</span>
    <span class="chip" onclick="tog(this)">🚌 교통·생활</span>
    <span class="chip" onclick="tog(this)">🌾 농업·창업</span>
  </div>

  <label style="font-size:12px;font-weight:700;color:#555;display:block;margin-bottom:10px;">저축 강도 목표 (1~10단계)</label>
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
    <input type="range" id="lv-range" min="1" max="10" value="5" style="flex:1;" oninput="updateLevel(this.value)">
    <div id="lv-val" style="font-size:16px;font-weight:800;color:#3b5bdb;min-width:36px;text-align:right;">5</div>
  </div>
  <div id="lv-desc" style="background:#FFC10722;border-left:4px solid #FFC107;border-radius:8px;padding:10px 14px;margin-bottom:24px;font-size:12px;">
    <b>5단계 · 균형형</b> — 저축 25% | 고정비 55% | 여가 20%
  </div>
  <button class="btn-p" onclick="finishOnboard()">맞춤 혜택 보러가기 🚀</button>
  <button class="btn-o" onclick="go('s-ob2')">← 이전</button>
</div>

<!-- ══════════════ HOME ══════════════ -->
<div id="s-home" class="screen">
  <div style="background:linear-gradient(135deg,#1a2a6c,#3b5bdb);padding:24px 20px 20px;color:#fff;flex-shrink:0;">
    <div style="font-size:12px;opacity:.75;" id="home-greeting">안녕하세요 👋</div>
    <h2 style="font-size:20px;font-weight:800;margin:4px 0 14px;" id="home-title">맞춤 혜택을 찾았어요!</h2>
    <div style="background:rgba(255,255,255,.15);border-radius:14px;padding:14px 16px;display:flex;justify-content:space-between;align-items:center;">
      <div>
        <div style="font-size:11px;opacity:.75;">혜택 활용 점수</div>
        <div style="font-size:28px;font-weight:800;" id="home-score">72<span style="font-size:14px;opacity:.7">/100</span></div>
      </div>
      <div style="text-align:right;">
        <div style="background:rgba(255,255,255,.2);border-radius:10px;padding:6px 12px;font-size:12px;font-weight:700;">🔥 더 받을 수 있어요!</div>
        <div style="font-size:11px;opacity:.65;margin-top:4px;" id="home-monthly">월 소득: 200만원</div>
      </div>
    </div>
  </div>

  <div class="tabs" id="home-tabs">
    <div class="tab on" onclick="homeTab(0)">🏆 맞춤혜택</div>
    <div class="tab" onclick="homeTab(1)">📊 예산현황</div>
    <div class="tab" onclick="homeTab(2)">📈 군산데이터</div>
  </div>

  <div class="scroll-body" id="home-body" style="padding:16px 16px 80px;">
    <!-- TAB 0: 맞춤혜택 -->
    <div id="htab-0">
      <div class="sec-title">⭐ 나에게 맞는 혜택</div>
      <div id="benefit-cards"><!-- JS inject --></div>
      <button class="btn-o" onclick="go('s-benefit')" style="margin-top:4px;">전체 혜택 보기 →</button>
    </div>
    <!-- TAB 1: 예산 -->
    <div id="htab-1" style="display:none;">
      <div class="sec-title">💰 이번달 예산 배분</div>
      <div id="budget-summary-home"><!-- JS --></div>
      <div class="sec-title" style="margin-top:16px;">📊 저축 단계</div>
      <div id="lv-home-card"><!-- JS --></div>
      <button class="btn-o" onclick="go('s-budget')" style="margin-top:4px;">가계부 보기 →</button>
    </div>
    <!-- TAB 2: 데이터 -->
    <div id="htab-2" style="display:none;">
      <div class="sec-title">📊 군산시 청년 현황 (2024 KOSIS)</div>
      <div class="card">
        <div style="font-size:13px;font-weight:700;margin-bottom:12px;">👥 청년 인구 비중</div>
        <div style="display:flex;align-items:center;gap:14px;">
          <div style="flex:1;">
            <div style="display:flex;justify-content:space-between;font-size:11px;color:#888;margin-bottom:4px;"><span>청년(18~39세)</span><span>21.7%</span></div>
            <div class="bbar-wrap"><div class="bbar-fill" style="width:22%;background:#3b5bdb;"></div></div>
            <div style="display:flex;justify-content:space-between;font-size:11px;color:#888;margin-bottom:4px;margin-top:8px;"><span>그 외</span><span>78.3%</span></div>
            <div class="bbar-wrap"><div class="bbar-fill" style="width:78%;background:#dde3f5;"></div></div>
          </div>
          <div style="text-align:center;">
            <div style="font-size:22px;font-weight:800;color:#3b5bdb;">56,117</div>
            <div style="font-size:10px;color:#888;">명 (전체 259,000명)</div>
          </div>
        </div>
      </div>
      <div class="card">
        <div style="font-size:13px;font-weight:700;margin-bottom:12px;">🏠 연령대별 주택 소유 비율</div>
        <div id="house-chart"><!-- CSS bars --></div>
      </div>
      <div class="card">
        <div style="font-size:13px;font-weight:700;margin-bottom:10px;">🎯 취업의 어려움 (군산시 2022)</div>
        <div id="job-chart"><!-- CSS bars --></div>
        <p style="font-size:10px;color:#aaa;margin-top:8px;">출처: KOSIS 전북 사회조사</p>
      </div>
    </div>
  </div>

  <div class="bnav">
    <div class="ni on" onclick="navTo('s-home')"><div class="ico">🏠</div><div class="lbl">홈</div></div>
    <div class="ni" onclick="navTo('s-benefit')"><div class="ico">🎁</div><div class="lbl">혜택</div></div>
    <div class="ni" onclick="navTo('s-ai')"><div class="ico">🤖</div><div class="lbl">AI요약</div></div>
    <div class="ni" onclick="navTo('s-budget')"><div class="ico">📒</div><div class="lbl">가계부</div></div>
    <div class="ni" onclick="navTo('s-more')"><div class="ico">⋯</div><div class="lbl">더보기</div></div>
  </div>
</div>

<!-- ══════════════ BENEFIT MATCHER ══════════════ -->
<div id="s-benefit" class="screen">
  <div style="background:linear-gradient(135deg,#0f3460,#3b5bdb);padding:24px 20px 16px;color:#fff;flex-shrink:0;">
    <div style="font-size:12px;opacity:.75;">군산시 청년 맞춤</div>
    <h2 style="font-size:20px;font-weight:800;margin:2px 0;">혜택 매칭 결과 🎁</h2>
    <p style="font-size:11px;opacity:.7;margin-top:4px;">프로필 기반으로 자동 매칭했어요</p>
  </div>
  <div class="tabs">
    <div class="tab on" onclick="benTab(0)">💰 자산형성</div>
    <div class="tab" onclick="benTab(1)">🏠 주거</div>
    <div class="tab" onclick="benTab(2)">💼 취업</div>
    <div class="tab" onclick="benTab(3)">🧠 생활</div>
  </div>
  <div class="scroll-body" style="padding:16px 16px 80px;" id="benefit-body">
    <!-- JS inject -->
  </div>
  <div class="bnav">
    <div class="ni" onclick="navTo('s-home')"><div class="ico">🏠</div><div class="lbl">홈</div></div>
    <div class="ni on" onclick="navTo('s-benefit')"><div class="ico">🎁</div><div class="lbl">혜택</div></div>
    <div class="ni" onclick="navTo('s-ai')"><div class="ico">🤖</div><div class="lbl">AI요약</div></div>
    <div class="ni" onclick="navTo('s-budget')"><div class="ico">📒</div><div class="lbl">가계부</div></div>
    <div class="ni" onclick="navTo('s-more')"><div class="ico">⋯</div><div class="lbl">더보기</div></div>
  </div>
</div>

<!-- ══════════════ AI SUMMARY ══════════════ -->
<div id="s-ai" class="screen">
  <div style="background:linear-gradient(135deg,#0f3460,#3b5bdb);padding:24px 20px 16px;color:#fff;flex-shrink:0;">
    <h2 style="font-size:20px;font-weight:800;">🤖 AI 금융 정책 요약</h2>
    <p style="font-size:11px;opacity:.75;margin-top:4px;">공공 API → 카테고리 분류 → GPT 쉬운말 요약</p>
  </div>
  <div class="scroll-body" style="padding:16px 16px 80px;">
    <div class="ai-bub">안녕하세요! 프로필을 기반으로 <b>금융상품, 주거, 취업</b> 카테고리 정책을 요약했어요. 아래 카드를 확인해보세요 👇</div>

    <div class="card" style="margin-bottom:12px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <span style="background:#fff0f6;color:#c2255c;font-size:11px;font-weight:700;padding:3px 10px;border-radius:12px;">🏦 청년금융</span>
        <span style="background:#e7f5ff;color:#1971c2;font-size:10px;padding:2px 8px;border-radius:8px;">STEP 1 → 분류완료</span>
      </div>
      <h4 style="font-size:14px;font-weight:800;margin-bottom:8px;">청년도약계좌, 쉽게 이해하기</h4>
      <div style="font-size:12px;color:#444;line-height:1.7;">
        ✅ <b>대상:</b> 만 19~34세, 개인소득 7,500만원 이하<br>
        ✅ <b>혜택:</b> 월 최대 70만원 납입 → 정부 기여금 월 최대 2.4만원<br>
        ✅ <b>금리:</b> 최대 6% (소득에 따라 차등)<br>
        ✅ <b>비과세:</b> 5년 만기 시 이자 전액 비과세<br><br>
        💡 <b>한줄 요약:</b> "5년 꾸준히 넣으면 정부가 보태줘서 약 5천만원 만드는 통장"
      </div>
      <button style="margin-top:10px;background:#eef2ff;color:#3b5bdb;border:none;border-radius:10px;padding:8px 14px;font-size:12px;font-weight:700;cursor:pointer;" onclick="tip('신청 페이지로 이동합니다')">신청하러 가기 →</button>
    </div>

    <div class="card" style="margin-bottom:12px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <span style="background:#ebfbee;color:#087f5b;font-size:11px;font-weight:700;padding:3px 10px;border-radius:12px;">🏠 주거지원</span>
        <span style="background:#e7f5ff;color:#1971c2;font-size:10px;padding:2px 8px;border-radius:8px;">STEP 1 → 분류완료</span>
      </div>
      <h4 style="font-size:14px;font-weight:800;margin-bottom:8px;">주택드림청약, 지금 시작해야 하는 이유</h4>
      <div style="font-size:12px;color:#444;line-height:1.7;">
        ✅ <b>대상:</b> 만 19~34세 무주택자<br>
        ✅ <b>금리:</b> 연 4.5% (일반 대비 +1.5%p)<br>
        ✅ <b>비과세:</b> 연 500만원 이자 소득 비과세<br><br>
        💡 <b>한줄 요약:</b> "일반보다 금리 높고 세금도 덜 내는 청년 전용 청약통장"
      </div>
      <button style="margin-top:10px;background:#eef2ff;color:#3b5bdb;border:none;border-radius:10px;padding:8px 14px;font-size:12px;font-weight:700;cursor:pointer;" onclick="tip('신청 페이지로 이동합니다')">신청하러 가기 →</button>
    </div>

    <div class="card" style="margin-bottom:12px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <span style="background:#fff9db;color:#e67700;font-size:11px;font-weight:700;padding:3px 10px;border-radius:12px;">💼 취업지원</span>
      </div>
      <h4 style="font-size:14px;font-weight:800;margin-bottom:8px;">전북형 청년활력수당</h4>
      <div style="font-size:12px;color:#444;line-height:1.7;">
        ✅ <b>대상:</b> 군산 거주 만 18~39세 미취업 청년, 중위소득 150% 이하<br>
        ✅ <b>혜택:</b> 월 50만원 × 6개월 = 총 300만원<br>
        ✅ <b>신청:</b> 군산시청 일자리경제과<br><br>
        💡 <b>한줄 요약:</b> "취업 준비 중 생활비를 군산시가 월 50만원씩 지원"
      </div>
      <button style="margin-top:10px;background:#eef2ff;color:#3b5bdb;border:none;border-radius:10px;padding:8px 14px;font-size:12px;font-weight:700;cursor:pointer;" onclick="tip('신청 페이지로 이동합니다')">신청하러 가기 →</button>
    </div>

    <div class="card">
      <div style="font-size:12px;font-weight:700;color:#555;margin-bottom:10px;">🔬 AI 분류 파이프라인</div>
      <div style="display:flex;gap:6px;align-items:center;">
        <div style="flex:1;background:#f0f4ff;border-radius:10px;padding:10px;text-align:center;font-size:10px;font-weight:700;color:#3b5bdb;">📡<br>공공API<br>수신</div>
        <div style="color:#aaa;font-size:16px;">→</div>
        <div style="flex:1;background:#fff9db;border-radius:10px;padding:10px;text-align:center;font-size:10px;font-weight:700;color:#e67700;">🏷️<br>카테고리<br>태깅</div>
        <div style="color:#aaa;font-size:16px;">→</div>
        <div style="flex:1;background:#ebfbee;border-radius:10px;padding:10px;text-align:center;font-size:10px;font-weight:700;color:#087f5b;">🤖<br>GPT<br>요약</div>
      </div>
    </div>
  </div>
  <div class="bnav">
    <div class="ni" onclick="navTo('s-home')"><div class="ico">🏠</div><div class="lbl">홈</div></div>
    <div class="ni" onclick="navTo('s-benefit')"><div class="ico">🎁</div><div class="lbl">혜택</div></div>
    <div class="ni on" onclick="navTo('s-ai')"><div class="ico">🤖</div><div class="lbl">AI요약</div></div>
    <div class="ni" onclick="navTo('s-budget')"><div class="ico">📒</div><div class="lbl">가계부</div></div>
    <div class="ni" onclick="navTo('s-more')"><div class="ico">⋯</div><div class="lbl">더보기</div></div>
  </div>
</div>

<!-- ══════════════ BUDGET ══════════════ -->
<div id="s-budget" class="screen">
  <div style="background:linear-gradient(135deg,#087f5b,#20c997);padding:24px 20px 16px;color:#fff;flex-shrink:0;">
    <h2 style="font-size:20px;font-weight:800;">📒 가계부</h2>
    <p style="font-size:11px;opacity:.75;margin-top:4px;" id="budget-month-label">2026년 4월</p>
  </div>
  <div class="tabs">
    <div class="tab on" onclick="budTab(0)">📊 요약</div>
    <div class="tab" onclick="budTab(1)">➕ 입력</div>
    <div class="tab" onclick="budTab(2)">🎚️ 저축단계</div>
  </div>
  <div class="scroll-body" style="padding:16px 16px 80px;">
    <!-- TAB 0: 요약 -->
    <div id="btab-0">
      <div style="display:flex;gap:8px;margin-bottom:12px;" id="bud-metrics"><!-- JS --></div>
      <div id="bud-bar-section"><!-- JS --></div>
      <div class="sec-title" style="margin-top:4px;">최근 거래 내역</div>
      <div class="card" style="padding:8px 16px;" id="tx-list"><!-- JS --></div>
    </div>
    <!-- TAB 1: 입력 -->
    <div id="btab-1" style="display:none;">
      <div class="card">
        <div class="sec-title">지출 추가</div>
        <div style="margin-bottom:12px;">
          <label style="font-size:12px;color:#555;font-weight:600;display:block;margin-bottom:6px;">대분류</label>
          <select id="cat-main" class="inp" style="padding:10px 12px;" onchange="updateSubCat()">
            <option>고정비</option><option>식비</option><option>여가</option><option>저축</option><option>기타</option>
          </select>
        </div>
        <div style="margin-bottom:12px;">
          <label style="font-size:12px;color:#555;font-weight:600;display:block;margin-bottom:6px;">소분류</label>
          <select id="cat-sub" class="inp" style="padding:10px 12px;"></select>
        </div>
        <div style="margin-bottom:12px;">
          <label style="font-size:12px;color:#555;font-weight:600;display:block;margin-bottom:6px;">금액 (원)</label>
          <input type="number" id="exp-amount" class="inp" placeholder="0" min="0" step="1000">
        </div>
        <div style="margin-bottom:16px;">
          <label style="font-size:12px;color:#555;font-weight:600;display:block;margin-bottom:6px;">메모</label>
          <input type="text" id="exp-memo" class="inp" placeholder="선택사항">
        </div>
        <button class="btn-p" onclick="addExpense()">추가하기</button>
      </div>
    </div>
    <!-- TAB 2: 저축단계 -->
    <div id="btab-2" style="display:none;">
      <div class="sec-title">🎚️ 저축 강도 선택</div>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <input type="range" id="lv-bud" min="1" max="10" value="5" style="flex:1;" oninput="updateBudLevel(this.value)">
        <span id="lv-bud-val" style="font-size:18px;font-weight:800;color:#3b5bdb;">5</span>
      </div>
      <div id="lv-bud-card" style="margin-bottom:16px;"><!-- JS --></div>
      <div class="sec-title">📊 전체 단계 비교</div>
      <div class="card" id="level-compare"><!-- JS bars --></div>
      <div class="sec-title" style="margin-top:4px;">📈 저축 시뮬레이션</div>
      <div class="card" id="sim-card"><!-- JS --></div>
    </div>
  </div>
  <div class="bnav">
    <div class="ni" onclick="navTo('s-home')"><div class="ico">🏠</div><div class="lbl">홈</div></div>
    <div class="ni" onclick="navTo('s-benefit')"><div class="ico">🎁</div><div class="lbl">혜택</div></div>
    <div class="ni" onclick="navTo('s-ai')"><div class="ico">🤖</div><div class="lbl">AI요약</div></div>
    <div class="ni on" onclick="navTo('s-budget')"><div class="ico">📒</div><div class="lbl">가계부</div></div>
    <div class="ni" onclick="navTo('s-more')"><div class="ico">⋯</div><div class="lbl">더보기</div></div>
  </div>
</div>

<!-- ══════════════ MORE (용어사전 + 설정) ══════════════ -->
<div id="s-more" class="screen">
  <div style="background:linear-gradient(135deg,#495057,#343a40);padding:24px 20px 16px;color:#fff;flex-shrink:0;">
    <h2 style="font-size:20px;font-weight:800;">⋯ 더보기</h2>
    <p style="font-size:11px;opacity:.75;margin-top:4px;">금융 용어사전 · 설정</p>
  </div>
  <div class="tabs">
    <div class="tab on" onclick="moreTab(0)">📚 용어사전</div>
    <div class="tab" onclick="moreTab(1)">👤 내 프로필</div>
    <div class="tab" onclick="moreTab(2)">ℹ️ 서비스 소개</div>
  </div>
  <div class="scroll-body" style="padding:16px 16px 80px;">
    <!-- TAB 0: 용어 -->
    <div id="mtab-0">
      <div class="card">
        <div class="glos-item">
          <div class="glos-term">기준 중위소득</div>
          <div class="glos-def">우리나라 모든 가구를 소득 순으로 줄 세웠을 때 딱 중간인 50등 가구의 소득이에요. '60% 이하'는 그 중간보다 소득이 적은 분들을 정부가 우선 지원하겠다는 기준이에요!</div>
        </div>
        <div class="glos-item">
          <div class="glos-term">비과세 (세금 안 뗌!)</div>
          <div class="glos-def">원래 은행 이자를 받으면 15.4% 세금을 내야 하지만, 비과세 상품은 세금을 한 푼도 안 떼고 이자를 통째로 받아요. 청년도약계좌의 핵심 혜택!</div>
        </div>
        <div class="glos-item">
          <div class="glos-term">매칭 지원 (1+1 저축)</div>
          <div class="glos-def">내가 10만원 저축하면 나라나 군산시가 똑같이 10만원을 공짜로 얹어주는 방식이에요. 전북청년 함께 두배적금이 대표적인 예시예요!</div>
        </div>
        <div class="glos-item">
          <div class="glos-term">바우처 (지정 이용권)</div>
          <div class="glos-def">현금 대신 주는 것으로, 정해진 곳에서만 쓸 수 있는 특별한 쿠폰이에요. 심리상담 바우처, 문화예술패스 등이 있어요.</div>
        </div>
        <div class="glos-item">
          <div class="glos-term">임차보증금 (전세보증금)</div>
          <div class="glos-def">집을 빌릴 때 "나중에 나갈 때 돌려받을게요!" 하고 집주인에게 맡겨두는 큰 돈이에요. 전세금 또는 월세 보증금을 말해요.</div>
        </div>
        <div class="glos-item">
          <div class="glos-term">반환보증</div>
          <div class="glos-def">나중에 보증금을 안전하게 돌려받을 수 있게 나라나 보험사가 보장해주는 전세금 안전장치예요. 전세 사기 예방의 핵심!</div>
        </div>
        <div class="glos-item">
          <div class="glos-term">CMA 통장</div>
          <div class="glos-def">입출금이 자유롭지만 일반 통장보다 높은 이자를 주는 통장이에요. 비상금이나 잠깐 돈을 모아두기 좋아요 (연 3~4% 수준).</div>
        </div>
        <div class="glos-item">
          <div class="glos-term">청년가구 / 원가구</div>
          <div class="glos-def">청년가구는 부모님과 떨어져 청년이 중심이 되어 사는 집, 원가구는 독립 전 부모님과 함께 살던 원래 가족을 말해요. 소득 기준 심사 시 둘 다 확인해요.</div>
        </div>
      </div>
    </div>
    <!-- TAB 1: 프로필 -->
    <div id="mtab-1" style="display:none;">
      <div class="card" id="profile-card"><!-- JS --></div>
      <button class="btn-o" onclick="go('s-ob1');tip('온보딩을 다시 시작합니다')">프로필 수정하기</button>
    </div>
    <!-- TAB 2: 서비스 소개 -->
    <div id="mtab-2" style="display:none;">
      <div class="card">
        <div style="font-size:15px;font-weight:800;margin-bottom:12px;">💰 핀핏 FinFit</div>
        <div style="font-size:12px;color:#555;line-height:1.8;">
          공공 API와 AI로 여는 <b>'금융 정보 격차 해소'</b>의 시작<br><br>
          <b>핵심 차별점</b><br>
          ✅ 군산시 KOSIS 실제 데이터 기반<br>
          ✅ 공공API → GPT 자동 요약<br>
          ✅ 나이·소득·상태별 혜택 자동 매칭<br>
          ✅ 저축 1~10단계 맞춤 예산 설계<br>
          ✅ 토스식 단순 UX (3초 이해)<br><br>
          <b>로드맵</b><br>
          2026.4~5 → UI/UX 설계<br>
          2026.5~7 → MVP + API 연동<br>
          2026.9 → B2C 정식 출시<br>
          2027 상반기 → B2B 파트너십 확장
        </div>
      </div>
      <div class="card">
        <div style="font-size:13px;font-weight:700;margin-bottom:8px;">📋 피드백 반영 사항</div>
        <div style="font-size:12px;color:#555;line-height:1.8;">
          ✅ 온보딩 프로필 입력 (나이·소득·상태)<br>
          ✅ 개인화 혜택 필터링<br>
          ✅ UI 단순화 (토스 벤치마킹)<br>
          ✅ AI 분류 로직 시각화<br>
          ✅ 자동 저축 기능<br>
          ✅ 보안: 계좌 직접 연동 없이 직접 입력
        </div>
      </div>
    </div>
  </div>
  <div class="bnav">
    <div class="ni" onclick="navTo('s-home')"><div class="ico">🏠</div><div class="lbl">홈</div></div>
    <div class="ni" onclick="navTo('s-benefit')"><div class="ico">🎁</div><div class="lbl">혜택</div></div>
    <div class="ni" onclick="navTo('s-ai')"><div class="ico">🤖</div><div class="lbl">AI요약</div></div>
    <div class="ni" onclick="navTo('s-budget')"><div class="ico">📒</div><div class="lbl">가계부</div></div>
    <div class="ni on" onclick="navTo('s-more')"><div class="ico">⋯</div><div class="lbl">더보기</div></div>
  </div>
</div>

<div class="tip" id="tipEl"></div>

<!-- ══════════════ JAVASCRIPT ══════════════ -->
<script>
// ── STATE ──
var ST = {
  age: 25, status: '취업준비생', house: '무주택',
  income: 200, incLevel: '140% 이하',
  interests: ['청년 금융상품','주거 지원','자산 형성'],
  level: 5,
  expenses: [
    {date:'04.22',cat:'식비',sub:'외식',amt:12000,memo:'점심'},
    {date:'04.22',cat:'고정비',sub:'교통비',amt:1400,memo:'버스'},
    {date:'04.21',cat:'저축',sub:'적금',amt:700000,memo:'청년도약계좌'},
    {date:'04.20',cat:'고정비',sub:'통신비',amt:55000,memo:''},
    {date:'04.19',cat:'여가',sub:'취미·문화',amt:30000,memo:'영화'},
    {date:'04.18',cat:'식비',sub:'카페·음료',amt:5500,memo:''},
  ]
};

var LEVELS = {
  1:{name:'여가 최우선',save:.05,fix:.45,lei:.50,color:'#4CAF50',tips:['소비 패턴 파악하는 시기','남는 돈은 CMA 자동이체','친구 모임 충분히 즐기기']},
  2:{name:'여가 중심',save:.10,fix:.50,lei:.40,color:'#8BC34A',tips:['적금 1개 자동이체 설정','여가비 예산 세우기','지출 앱으로 소비 기록']},
  3:{name:'균형 여가형',save:.15,fix:.55,lei:.30,color:'#CDDC39',tips:['청년희망적금 가입 검토','외식 횟수 주 2회로','구독 서비스 정리']},
  4:{name:'생활 균형형',save:.20,fix:.55,lei:.25,color:'#FFEB3B',tips:['비상금 3개월치 먼저','교통비 할인카드 발급','식비는 식료품 위주']},
  5:{name:'균형형',save:.25,fix:.55,lei:.20,color:'#FFC107',tips:['청년도약계좌 적극 활용','점심은 도시락/구내식당','무료·저가 문화활동']},
  6:{name:'저축 균형형',save:.30,fix:.55,lei:.15,color:'#FF9800',tips:['청년월세지원 신청','체크카드 위주 사용','월말 잔액 추가 저축']},
  7:{name:'저축 집중형',save:.40,fix:.50,lei:.10,color:'#FF5722',tips:['고정비 전면 재검토','알뜰폰 전환 (월 1~2만원)','여가 한달 1~2회만']},
  8:{name:'고강도 저축',save:.50,fix:.45,lei:.05,color:'#F44336',tips:['월세 부담 낮추기','직접 요리 위주','절약 챌린지 참여']},
  9:{name:'극한 저축',save:.65,fix:.35,lei:.00,color:'#E91E63',tips:['단기 목돈 목표 설정','불필요 지출 전면 제거','정부 식품바우처 활용']},
  10:{name:'생존형 저축',save:.80,fix:.20,lei:.00,color:'#9C27B0',tips:['생활비 최저 생계비 수준','무료 와이파이 적극 이용','번아웃 주의: 단기 목표로']}
};

var SUBCATS = {
  '고정비':['월세/관리비','통신비','보험료','교통비','구독서비스'],
  '식비':['식료품','외식','카페·음료'],
  '여가':['취미·문화','여행','친구 모임','쇼핑'],
  '저축':['적금','비상금','투자'],
  '기타':['의료비','교육·자기계발','기타']
};

// 혜택 DB
var BENEFITS = {
  asset:[
    {ico:'🏦',bg:'#fff0f6',name:'청년도약계좌',org:'중앙정부',
     cond:'만 19~34세, 소득 중위 180% 이하',
     desc:'월 최대 70만원 납입 시 정부기여금+비과세. 5년 만기 약 5,000만원',
     dl:'상시 모집',
     check: s => s.age>=19 && s.age<=34 && s.incLevel!='소득 기준 초과'},
    {ico:'💎',bg:'#f3f0ff',name:'청년미래적금',org:'중앙정부 2026 신설',
     cond:'만 19~34세, 개인소득 6,000만원 이하',
     desc:'월 50만원×3년. 정부기여금+비과세로 최대 2,200만원(우대형)',
     dl:'2026년 신설',
     check: s => s.age>=19 && s.age<=34 && s.incLevel!='소득 기준 초과'},
    {ico:'💰',bg:'#ebfbee',name:'전북청년 함께 두배적금',org:'전북/군산시',
     cond:'만 18~39세 근로·창업 중인 청년',
     desc:'월 10만원 저축 시 지자체가 10만원 1:1 매칭. 2년 후 두배!',
     dl:'상시 모집',
     check: s => s.age>=18 && s.age<=39 && s.status!='취업준비생' && s.incLevel!='소득 기준 초과'},
    {ico:'💳',bg:'#fff9db',name:'청년 우대형 CMA',org:'시중은행',
     cond:'만 19~34세',
     desc:'연 4.1% 금리. 입출금 자유. 자동이체 연동 가능. 사회초년생 추천',
     dl:'상시',
     check: s => s.age>=19 && s.age<=34}
  ],
  housing:[
    {ico:'🏠',bg:'#ebfbee',name:'청년월세 한시 특별지원',org:'중앙정부',
     cond:'만 19~34세 독립거주, 중위소득 60% 이하',
     desc:'월 최대 20만원 × 최장 24개월 = 총 480만원 현금 지원',
     dl:'복지로 신청',
     check: s => s.age>=19 && s.age<=34 && s.house=='무주택' && s.incLevel=='60% 이하'},
    {ico:'🔒',bg:'#e7f5ff',name:'전세보증금 반환보증 보증료 지원',org:'중앙정부',
     cond:'만 19~39세 무주택, 연소득 5,000만원 이하',
     desc:'이미 납부한 전세보증금 반환보증 보증료 최대 40만원 환급',
     dl:'HUG/HF 신청',
     check: s => s.age>=19 && s.age<=39 && s.house=='무주택' && s.incLevel!='소득 기준 초과'},
    {ico:'🏢',bg:'#fff0f6',name:'군산 STAY 주거지원사업',org:'군산시',
     cond:'만 19~49세 취업자 또는 창업자',
     desc:'최대 24개월 임대주택 보증금 350만원 + 월 임차료 10만원 지원',
     dl:'군산시청 신청',
     check: s => s.age>=19 && s.age<=49 && s.house=='무주택' && (s.status=='직장인'||s.status=='창업자')},
    {ico:'💸',bg:'#fff9db',name:'청년 전세자금 대출이자 지원',org:'군산시',
     cond:'만 18~39세, 중위소득 180% 이하',
     desc:'전세보증금 대출 잔액의 최대 2% 이자 지원 (연 최대 200만원)',
     dl:'군산시청 신청',
     check: s => s.age>=18 && s.age<=39 && s.house=='무주택' && s.incLevel!='소득 기준 초과'}
  ],
  job:[
    {ico:'🏃',bg:'#e7f5ff',name:'국민취업지원제도 1유형',org:'중앙정부',
     cond:'만 18~34세 미취업, 중위소득 120% 이하',
     desc:'구직촉진수당 월 60만원 × 6개월 + 취업지원 서비스',
     dl:'워크넷 신청',
     check: s => s.status=='취업준비생' && s.age>=18 && s.age<=34 && ['60% 이하','100% 이하','140% 이하'].includes(s.incLevel)},
    {ico:'💼',bg:'#ebfbee',name:'전북형 청년활력수당',org:'전북/군산시',
     cond:'군산 거주 만 18~39세 미취업, 중위소득 150% 이하',
     desc:'월 50만원 × 6개월 = 총 300만원 구직활동 지원',
     dl:'군산시청 신청',
     check: s => s.status=='취업준비생' && s.age>=18 && s.age<=39 && s.incLevel!='소득 기준 초과'},
    {ico:'🚀',bg:'#fff9db',name:'모두의 창업 프로젝트',org:'중앙정부 2026 신설',
     cond:'연령·학력 제한 없음 (비수도권 우선)',
     desc:'아이디어만 있으면 최대 10억원 사업화 자금 + AI 솔루션 지원',
     dl:'2026년 신설',
     check: s => true},
    {ico:'📚',bg:'#f3f0ff',name:'국민내일배움카드',org:'중앙정부',
     cond:'만 15세 이상 누구나',
     desc:'5년간 300~500만원 직업훈련비 지원. HRD-Net에서 신청',
     dl:'HRD-Net 신청',
     check: s => true}
  ],
  life:[
    {ico:'🧠',bg:'#f3f0ff',name:'전국민 마음투자 지원사업',org:'중앙정부',
     cond:'만 18~39세',
     desc:'전문 심리상담 바우처 총 8회 제공. 보건소/복지로 신청 가능',
     dl:'보건소 신청',
     check: s => s.age>=18 && s.age<=39},
    {ico:'🚌',bg:'#e7f5ff',name:'K-패스 청년 무제한 정액권',org:'중앙정부 2026 확대',
     cond:'만 18~39세',
     desc:'월 5.5만원으로 전국 대중교통 월 20만원 한도 무제한 이용',
     dl:'카드사 신청',
     check: s => s.age>=18 && s.age<=39},
    {ico:'🎨',bg:'#fff9db',name:'청년문화예술패스',org:'중앙정부',
     cond:'만 19~20세',
     desc:'순수예술 관람 연 최대 20만원 포인트 지급 (2026년 영화 추가)',
     dl:'문화포털 신청',
     check: s => s.age>=19 && s.age<=20},
    {ico:'🏥',bg:'#ebfbee',name:'청년 정신건강검진 확대',org:'중앙정부 2026',
     cond:'만 20~34세',
     desc:'정신건강 검진 주기 10년→2년 단축, 조현병·조울증 검사 추가',
     dl:'건강검진 대상자',
     check: s => s.age>=20 && s.age<=34}
  ]
};

var curBenTab = 0;
var curBudTab = 0;
var curHomeTab = 0;
var curMoreTab = 0;

// ── NAVIGATION ──
function go(id){
  document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  document.getElementById(id).scrollTop=0;
}
function navTo(id){
  go(id);
  if(id=='s-home') renderHome();
  if(id=='s-benefit') renderBenefits(curBenTab);
  if(id=='s-budget') renderBudget(curBudTab);
  if(id=='s-more') renderMore(curMoreTab);
}
function skipOnboard(){
  finishOnboard();
}

// ── CHIP helpers ──
function sel(el,grp){
  document.querySelectorAll('#'+grp+' .chip').forEach(c=>c.classList.remove('on'));
  el.classList.add('on');
  // update ST
  if(grp=='status-grp') ST.status=el.textContent.trim().replace(/^./,'');
  if(grp=='house-grp') ST.house=el.textContent.trim().replace(/^./,'');
  if(grp=='inc-grp') ST.incLevel=el.textContent.trim();
}
function tog(el){
  el.classList.toggle('on');
  ST.interests=[];
  document.querySelectorAll('#int-grp .chip.on').forEach(c=>ST.interests.push(c.textContent.trim().replace(/^./,'')));
}

// ── RANGE helpers ──
function updateIncome(v){
  document.getElementById('inc-val').textContent=v==0?'없음':v+'만원';
  ST.income=parseInt(v);
}
function updateLevel(v){
  var lv=LEVELS[v];
  document.getElementById('lv-val').textContent=v;
  document.getElementById('lv-desc').innerHTML='<b>'+v+'단계 · '+lv.name+'</b> — 저축 '+Math.round(lv.save*100)+'% | 고정비 '+Math.round(lv.fix*100)+'% | 여가 '+Math.round(lv.lei*100)+'%';
  document.getElementById('lv-desc').style.background=lv.color+'22';
  document.getElementById('lv-desc').style.borderLeftColor=lv.color;
  ST.level=parseInt(v);
}

// ── ONBOARD FINISH ──
function finishOnboard(){
  // read age
  ST.age=parseInt(document.getElementById('age-range').value);
  ST.level=parseInt(document.getElementById('lv-range').value);
  renderHome();
  navTo('s-home');
  tip('프로필 저장 완료! 맞춤 혜택을 불러왔어요 🎉');
}

// ── HOME ──
function homeTab(n){
  curHomeTab=n;
  ['htab-0','htab-1','htab-2'].forEach((id,i)=>document.getElementById(id).style.display=i==n?'block':'none');
  document.querySelectorAll('#home-tabs .tab').forEach((t,i)=>t.classList.toggle('on',i==n));
  if(n==0) renderBenefitCards();
  if(n==1) renderBudgetHome();
}
function renderHome(){
  var statusEmoji={'취업준비생':'📚','사회초년생':'💼','재학생':'🎓','직장인':'🏢','창업자':'🌱','농업종사':'🌾'};
  document.getElementById('home-greeting').textContent=(statusEmoji[ST.status]||'👋')+' '+ST.status+' 회원님';
  document.getElementById('home-monthly').textContent='월 소득: '+ST.income+'만원';
  var cnt=BENEFITS.asset.filter(b=>b.check(ST)).length+BENEFITS.housing.filter(b=>b.check(ST)).length;
  document.getElementById('home-title').textContent='맞춤 혜택 '+cnt+'건을 찾았어요!';
  renderBenefitCards();
  renderHouseChart();
  renderJobChart();
}
function renderBenefitCards(){
  var all=[...BENEFITS.asset,...BENEFITS.housing,...BENEFITS.job,...BENEFITS.life];
  var matched=all.filter(b=>b.check(ST)).slice(0,4);
  var html='';
  matched.forEach(b=>{
    html+='<div class="bc" onclick="navTo(\\'s-benefit\\')">'
      +'<div class="bc-ico" style="background:'+b.bg+'">'+b.ico+'</div>'
      +'<div><h4>'+b.name+' <span class="badge">매칭</span></h4>'
      +'<p>'+b.desc+'</p>'
      +'<div class="dl">📌 '+b.org+'</div></div></div>';
  });
  document.getElementById('benefit-cards').innerHTML=html||'<p style="font-size:13px;color:#aaa;padding:10px 0;">조건에 맞는 혜택을 찾는 중...</p>';
}
function renderBudgetHome(){
  var inc=ST.income*10000;
  var lv=LEVELS[ST.level];
  var saveTarget=Math.round(inc*lv.save);
  var fixTarget=Math.round(inc*lv.fix);
  var leiTarget=Math.round(inc*lv.lei);
  var totalExp=ST.expenses.filter(e=>e.cat!='저축').reduce((a,e)=>a+e.amt,0);
  var totalSave=ST.expenses.filter(e=>e.cat=='저축').reduce((a,e)=>a+e.amt,0);
  document.getElementById('budget-summary-home').innerHTML=
    '<div style="display:flex;gap:8px;margin-bottom:12px;">'
    +'<div class="metric" style="border-top:3px solid #3b5bdb;"><div class="mv plus">'+fmt(inc)+'</div><div class="ml">수입</div></div>'
    +'<div class="metric" style="border-top:3px solid #e03131;"><div class="mv minus">'+fmt(totalExp)+'</div><div class="ml">지출</div></div>'
    +'<div class="metric" style="border-top:3px solid #087f5b;"><div class="mv" style="color:#087f5b;">'+fmt(totalSave)+'</div><div class="ml">저축</div></div>'
    +'</div>';
  document.getElementById('lv-home-card').innerHTML=
    '<div class="lv-card" style="background:'+lv.color+'18;border-left-color:'+lv.color+';">'
    +'<b style="font-size:14px;">'+ST.level+'단계 · '+lv.name+'</b><br>'
    +'<span style="font-size:12px;color:#555;">저축 '+Math.round(lv.save*100)+'% ('+(saveTarget/10000).toFixed(0)+'만원) | 고정비 '+Math.round(lv.fix*100)+'% | 여가 '+Math.round(lv.lei*100)+'%</span>'
    +'</div>';
}
function renderHouseChart(){
  var data=[['18~29세',18],['30~39세',31],['40~49세',52],['50~59세',67],['60세+',73]];
  var html='<div style="font-size:11px;color:#555;margin-bottom:8px;">연령대별 주택 소유 비율 (%)</div>';
  data.forEach(d=>{
    html+='<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">'
      +'<span style="font-size:11px;color:#888;min-width:50px;">'+d[0]+'</span>'
      +'<div style="flex:1;background:#f1f3f9;border-radius:4px;height:14px;overflow:hidden;">'
      +'<div style="width:'+d[1]+'%;background:'+(['#5c7cfa','#74c0fc','#63e6be','#ffd43b','#ff8787'][data.indexOf(d)])+';height:100%;border-radius:4px;"></div></div>'
      +'<span style="font-size:11px;font-weight:700;min-width:28px;">'+d[1]+'%</span></div>';
  });
  document.getElementById('house-chart').innerHTML=html;
}
function renderJobChart(){
  var data=[['일자리 부족',48.2],['능력·경험 부족',22.1],['임금 불만족',13.4],['취업 정보 부족',9.8],['기타',6.5]];
  var html='<div style="font-size:11px;color:#555;margin-bottom:8px;">어려움 요인 (%)</div>';
  data.forEach(d=>{
    html+='<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">'
      +'<span style="font-size:10px;color:#888;min-width:70px;">'+d[0]+'</span>'
      +'<div style="flex:1;background:#f1f3f9;border-radius:4px;height:14px;overflow:hidden;">'
      +'<div style="width:'+(d[1]/50*100)+'%;background:#3b5bdb;height:100%;border-radius:4px;"></div></div>'
      +'<span style="font-size:11px;font-weight:700;min-width:36px;">'+d[1]+'%</span></div>';
  });
  document.getElementById('job-chart').innerHTML=html;
}

// ── BENEFIT ──
function benTab(n){
  curBenTab=n;
  document.querySelectorAll('#s-benefit .tab').forEach((t,i)=>t.classList.toggle('on',i==n));
  renderBenefits(n);
}
function renderBenefits(n){
  var cats=['asset','housing','job','life'];
  var data=BENEFITS[cats[n]];
  var html='';
  data.forEach(b=>{
    var ok=b.check(ST);
    html+='<div class="bc" style="border-left:3px solid '+(ok?'#3b5bdb':'#ddd')+';opacity:'+(ok?1:.6)+';">'
      +'<div class="bc-ico" style="background:'+b.bg+'">'+b.ico+'</div>'
      +'<div style="flex:1;">'
      +'<h4>'+b.name+'<span class="match-tag '+(ok?'match-y':'match-n')+'">'+(ok?'✅ 해당':'✗ 미해당')+'</span></h4>'
      +'<p style="font-size:11px;color:#777;margin:2px 0;">'+b.org+'</p>'
      +'<p style="font-size:11px;color:#555;line-height:1.5;margin-top:4px;">'+b.cond+'</p>'
      +'<p style="font-size:12px;color:#333;line-height:1.5;margin-top:4px;">'+b.desc+'</p>'
      +(ok?'<div class="dl">📌 '+b.dl+'</div>':'')
      +'</div></div>';
  });
  document.getElementById('benefit-body').innerHTML=html;
}

// ── BUDGET ──
function budTab(n){
  curBudTab=n;
  ['btab-0','btab-1','btab-2'].forEach((id,i)=>document.getElementById(id).style.display=i==n?'block':'none');
  document.querySelectorAll('#s-budget .tab').forEach((t,i)=>t.classList.toggle('on',i==n));
  if(n==0) renderBudgetSummary();
  if(n==2) renderLevelTab();
}
function renderBudget(n){
  budTab(n);
}
function renderBudgetSummary(){
  var inc=ST.income*10000;
  var lv=LEVELS[ST.level];
  var totalExp=ST.expenses.filter(e=>e.cat!='저축').reduce((a,e)=>a+e.amt,0);
  var totalSave=ST.expenses.filter(e=>e.cat=='저축').reduce((a,e)=>a+e.amt,0);
  var remain=inc-totalExp-totalSave;
  var pct=Math.round((totalExp+totalSave)/inc*100);
  document.getElementById('bud-metrics').innerHTML=
    '<div class="metric" style="border-top:3px solid #3b5bdb;"><div class="mv plus">'+fmt(inc)+'</div><div class="ml">수입</div></div>'
    +'<div class="metric" style="border-top:3px solid #e03131;"><div class="mv minus">'+fmt(totalExp)+'</div><div class="ml">지출</div></div>'
    +'<div class="metric" style="border-top:3px solid #087f5b;"><div class="mv" style="color:#087f5b;">'+fmt(remain)+'</div><div class="ml">잔여</div></div>';
  document.getElementById('bud-bar-section').innerHTML=
    '<div class="card" style="margin-bottom:12px;">'
    +'<div style="display:flex;justify-content:space-between;font-size:12px;color:#888;margin-bottom:4px;">'
    +'<span>예산 사용 '+pct+'%</span><span>저축 '+fmt(totalSave)+'</span></div>'
    +'<div class="bbar-wrap" style="height:10px;"><div class="bbar-fill" style="width:'+Math.min(pct,100)+'%;background:linear-gradient(90deg,#5c7cfa,'+(pct>80?'#e03131':'#3b5bdb')+');"></div></div>'
    +'<div style="font-size:11px;color:#aaa;margin-top:4px;">'+ST.level+'단계 목표 저축: '+fmt(Math.round(inc*lv.save))+'</div>'
    +'</div>';
  // tx list
  var txHtml='';
  ST.expenses.forEach(e=>{
    var col=e.cat=='저축'?'#3b5bdb':e.cat=='고정비'?'#e8edf8':'#fff9db';
    txHtml+='<div class="tx">'
      +'<div class="tx-l"><div class="tx-ico" style="background:'+col+'">'+catIco(e.cat)+'</div>'
      +'<div><div class="tx-name">'+e.sub+(e.memo?' ('+e.memo+')':'')+'</div><div class="tx-date">'+e.date+'</div></div></div>'
      +'<div class="tx-amt '+(e.cat=='저축'?'plus':'minus')+'">'+( e.cat=='저축'?'+':'-')+fmt(e.amt)+'</div>'
      +'</div>';
  });
  document.getElementById('tx-list').innerHTML=txHtml;
}
function catIco(cat){
  return {고정비:'🏠',식비:'🍔',여가:'🎉',저축:'💎',기타:'📌'}[cat]||'📌';
}
function updateSubCat(){
  var main=document.getElementById('cat-main').value;
  var subs=SUBCATS[main]||[];
  document.getElementById('cat-sub').innerHTML=subs.map(s=>'<option>'+s+'</option>').join('');
}
function addExpense(){
  var amt=parseInt(document.getElementById('exp-amount').value);
  if(!amt||amt<=0){tip('금액을 입력해주세요!');return;}
  ST.expenses.unshift({
    date:'04.'+new Date().getDate(),
    cat:document.getElementById('cat-main').value,
    sub:document.getElementById('cat-sub').value,
    amt:amt,
    memo:document.getElementById('exp-memo').value
  });
  document.getElementById('exp-amount').value='';
  document.getElementById('exp-memo').value='';
  renderBudgetSummary();
  budTab(0);
  tip('✅ 저장됐어요!');
}
function renderLevelTab(){
  var lv=LEVELS[ST.level];
  var inc=ST.income*10000;
  // level card
  document.getElementById('lv-bud').value=ST.level;
  document.getElementById('lv-bud-val').textContent=ST.level;
  updateBudLevel(ST.level);
  // compare bars
  var html='<div style="font-size:11px;color:#888;margin-bottom:8px;">각 단계별 저축/고정비/여가 비율</div>';
  for(var i=1;i<=10;i++){
    var l=LEVELS[i];
    html+='<div style="margin-bottom:6px;">'
      +'<div style="font-size:10px;color:#888;margin-bottom:2px;">'+i+'단계 '+l.name+'</div>'
      +'<div style="display:flex;height:10px;border-radius:5px;overflow:hidden;">'
      +'<div style="flex:'+l.save+';background:#9C27B0;"></div>'
      +'<div style="flex:'+l.fix+';background:#2196F3;"></div>'
      +'<div style="flex:'+l.lei+';background:#4CAF50;"></div>'
      +'</div></div>';
  }
  html+='<div style="display:flex;gap:10px;margin-top:8px;font-size:10px;"><span><span style="display:inline-block;width:10px;height:10px;background:#9C27B0;border-radius:2px;margin-right:3px;"></span>저축</span>'
    +'<span><span style="display:inline-block;width:10px;height:10px;background:#2196F3;border-radius:2px;margin-right:3px;"></span>고정비</span>'
    +'<span><span style="display:inline-block;width:10px;height:10px;background:#4CAF50;border-radius:2px;margin-right:3px;"></span>여가</span></div>';
  document.getElementById('level-compare').innerHTML=html;
  // sim
  renderSim();
}
function updateBudLevel(v){
  ST.level=parseInt(v);
  document.getElementById('lv-bud-val').textContent=v;
  var lv=LEVELS[v];
  document.getElementById('lv-bud-card').innerHTML=
    '<div class="lv-card" style="background:'+lv.color+'18;border-left-color:'+lv.color+';">'
    +'<b>'+v+'단계 · '+lv.name+'</b><br>'
    +'<span style="font-size:12px;">저축 '+Math.round(lv.save*100)+'% | 고정비 '+Math.round(lv.fix*100)+'% | 여가 '+Math.round(lv.lei*100)+'%</span>'
    +'<ul style="margin-top:8px;padding-left:16px;font-size:11px;color:#555;">'
    +lv.tips.map(t=>'<li>'+t+'</li>').join('')
    +'</ul></div>';
  renderSim();
}
function renderSim(){
  var lv=LEVELS[ST.level];
  var inc=ST.income*10000;
  var ms=Math.round(inc*lv.save);
  var html='<div style="font-size:13px;font-weight:700;margin-bottom:10px;">📈 저축 시뮬레이션</div>';
  [6,12,24,36].forEach(m=>{
    html+='<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f1f3f9;">'
      +'<span style="font-size:12px;color:#555;">'+m+'개월 후</span>'
      +'<span style="font-size:13px;font-weight:700;color:#3b5bdb;">'+fmt(ms*m)+'</span>'
      +'</div>';
  });
  document.getElementById('sim-card').innerHTML=html;
}

// ── MORE ──
function moreTab(n){
  curMoreTab=n;
  ['mtab-0','mtab-1','mtab-2'].forEach((id,i)=>document.getElementById(id).style.display=i==n?'block':'none');
  document.querySelectorAll('#s-more .tab').forEach((t,i)=>t.classList.toggle('on',i==n));
  if(n==1) renderProfile();
}
function renderMore(n){moreTab(n);}
function renderProfile(){
  var lv=LEVELS[ST.level];
  document.getElementById('profile-card').innerHTML=
    '<div style="text-align:center;padding:10px 0 16px;">'
    +'<div style="font-size:48px;margin-bottom:8px;">'+(ST.status=='취업준비생'?'📚':ST.status=='사회초년생'?'💼':ST.status=='직장인'?'🏢':'👤')+'</div>'
    +'<div style="font-size:18px;font-weight:800;">'+ST.status+'</div>'
    +'<div style="font-size:13px;color:#888;margin-top:4px;">만 '+ST.age+'세 · '+ST.house+'</div>'
    +'</div>'
    +'<div style="border-top:1px solid #f1f3f9;padding-top:14px;">'
    +'<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f8f9ff;"><span style="font-size:13px;color:#555;">월 소득</span><span style="font-size:13px;font-weight:700;">'+ST.income+'만원</span></div>'
    +'<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f8f9ff;"><span style="font-size:13px;color:#555;">소득 수준</span><span style="font-size:13px;font-weight:700;">'+ST.incLevel+'</span></div>'
    +'<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f8f9ff;"><span style="font-size:13px;color:#555;">저축 단계</span><span style="font-size:13px;font-weight:700;">'+ST.level+'단계 · '+lv.name+'</span></div>'
    +'<div style="display:flex;justify-content:space-between;padding:8px 0;"><span style="font-size:13px;color:#555;">관심 분야</span><span style="font-size:12px;font-weight:700;text-align:right;max-width:180px;">'+ST.interests.join(', ')+'</span></div>'
    +'</div>';
}

// ── UTILS ──
function fmt(n){
  if(n>=10000) return (n/10000).toFixed(0)+'만원';
  return n.toLocaleString()+'원';
}
function tip(msg){
  var el=document.getElementById('tipEl');
  el.textContent=msg; el.classList.add('show');
  setTimeout(()=>el.classList.remove('show'),2500);
}

// ── INIT ──
window.onload=function(){
  updateSubCat();
};
</script>

<script>
    function syncHeight() {
        const h = document.body.scrollHeight;
        window.parent.postMessage({type:'streamlit:setFrameHeight', height:h}, '*');
    }
    window.onload = syncHeight;
    new MutationObserver(syncHeight).observe(document.body, {childList:true, subtree:true});
</script>
</body>
</html>"""

components.html(HTML, height=1050, scrolling=False)
