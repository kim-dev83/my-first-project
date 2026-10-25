import os
from datetime import date
import streamlit as st
from gemini_client import MAX_INPUT_CHARS, SummaryError, summarize

st.set_page_config(page_title="한눈요약 | AI 요약 서비스",page_icon="✍️",layout="centered")
st.title("✍️ 한눈요약")
st.write("텍스트를 입력하면 Gemini AI가 핵심 내용을 요약합니다.")

def read_key():
    key = os.getenv("GEMINI_API_KEY","").strip()
    if key:
        return key
    try:
        return str(st.secrets.get("GEMINI_API_KEY","")).strip()
    except (FileNotFoundError, KeyError):
        return ""

key=read_key()
st.caption("Gemini API 연결: " + ("설정됨" if key else "미설정"))
st.warning("공개 앱 방문자의 Gemini API 사용량은 소유자 계정에 발생할 수 있습니다. 개인·기밀 정보는 입력하지 마세요.")
example=("생성형 인공지능은 문서 작성과 정보 탐색에 활용됩니다. "
         "반복 작업을 줄이고 생산성을 높일 수 있지만, 결과의 정확성을 검증해야 합니다. "
         "또한 개인 정보 보호와 비용 관리가 중요합니다.")
if "source_text" not in st.session_state:
    st.session_state.source_text=""
if st.button("예시 불러오기"):
    st.session_state.source_text=example
    st.rerun()
source=st.text_area("원문",key="source_text",height=220,placeholder="25자 이상 입력하세요.")
st.caption(f"입력 길이: {len(source):,} / {MAX_INPUT_CHARS:,}자")
style=st.selectbox("요약 방식",["핵심 3줄","한 문장","자세히"])
mode_label=st.radio("실행 모드",["Gemini AI 실제 요약","데모 체험 (AI 아님)"],horizontal=True)
mode="gemini" if mode_label.startswith("Gemini") else "mock"
if mode=="gemini" and not key:
    st.info("실제 요약에는 Streamlit Secrets의 GEMINI_API_KEY 등록이 필요합니다.")
if mode=="mock":
    st.info("데모는 문장 추출만 수행하고 실제 AI 요약을 하지 않습니다.")
if st.button("✨ 요약하기",type="primary",disabled=not source.strip() or (mode=="gemini" and not key)):
    try:
        with st.spinner("요약 중입니다..."):
            st.session_state.result=summarize(source,style=style,mode=mode,api_key=key)
    except SummaryError as exc:
        st.error(str(exc))
        st.session_state.result=None
    except Exception:
        st.error("요약 요청에 실패했습니다. 앱 설정과 로그를 확인하세요.")
        st.session_state.result=None
result=st.session_state.get("result")
if result:
    st.subheader("요약 결과")
    if result.provider=="gemini":
        st.success(f"Gemini AI 요약 완료 ({result.model})")
    else:
        st.info("데모 결과: 실제 AI 생성 아님")
    st.text_area("결과",result.text,height=180)
    st.download_button("TXT 저장",result.text,file_name=f"summary_{date.today().isoformat()}.txt",mime="text/plain")
st.caption("Week 15-2 · Level#3 자유주제 · Streamlit Community Cloud")
