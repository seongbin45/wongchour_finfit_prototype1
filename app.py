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

components.html(HTML, height=950, scrolling=True)
