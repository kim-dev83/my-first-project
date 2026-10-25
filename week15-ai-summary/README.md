# ✍️ 한눈요약 — AI 텍스트 요약 서비스

15-2주차 Level#3 자유주제 클라우드 서비스 프로젝트입니다. Android Studio가 아닌 **Streamlit 웹브라우저 앱**입니다.

## 기능
텍스트 입력, Gemini AI 요약(핵심 3줄 / 한 문장 / 자세히), 결과 TXT 저장, 데모 모드(실제 AI 아님).

## Streamlit Community Cloud 배포
1. https://share.streamlit.io 접속 후 GitHub로 로그인 → Create app
2. Repository: **kim-dev83/my-first-project**, Branch: **main**
3. Main file path: **week15-ai-summary/app.py**
4. Advanced settings → Secrets에 다음 내용 입력 (실제 키는 GitHub에 올리지 마세요):

    GEMINI_API_KEY = "본인이_발급받은_실제_키"

5. Deploy 후 발급된 공개 URL에서 **Gemini AI 실제 요약** 모드로 테스트합니다.
6. 공개 URL, 실제 AI 응답 화면, 배포 화면, 키를 가린 설정 및 비용 관리 캡처를 제출합니다.

API 키 발급: https://aistudio.google.com/api-keys

## 로컬 실행
python -m pip install -r requirements.txt
python -m streamlit run app.py

키를 환경변수 GEMINI_API_KEY로 등록하면 실제 AI 요약이 가능합니다. 키가 없으면 데모만 작동합니다.

**상태:** 코드는 업로드되었으나, 실제 공개 배포와 API 호출은 별도로 확인해야 합니다. Google AI Studio 사용량·결제 한도를 점검하세요.
