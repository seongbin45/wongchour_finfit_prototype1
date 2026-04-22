import streamlit as st
import streamlit.components.v1 as components
import os  # 추가

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

# ✅ 이 부분만 수정 — 절대 경로로 변경
html_path = os.path.join(os.path.dirname(__file__), "finfit.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# HTML 내용 끝에 자동 높이 조절 스크립트 삽입
auto_resize = """
<script>
    // iframe 높이를 콘텐츠에 맞게 자동 조절
    window.onload = function() {
        const height = document.body.scrollHeight;
        window.parent.postMessage({type: 'streamlit:setFrameHeight', height: height}, '*');
    };
    // 화면 전환 시에도 재조절
    const observer = new MutationObserver(() => {
        const height = document.body.scrollHeight;
        window.parent.postMessage({type: 'streamlit:setFrameHeight', height: height}, '*');
    });
    observer.observe(document.body, {childList: true, subtree: true});
</script>
"""

components.html(HTML + auto_resize, height=1050, scrolling=False)
