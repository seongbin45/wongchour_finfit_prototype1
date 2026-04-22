import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="핀핏 FinFit",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 여백 최소화 스타일
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    section[data-testid="stMain"] > div { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# HTML 파일 읽기
with open("finfit.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 전체 화면으로 렌더링
components.html(html_content, height=900, scrolling=False)
