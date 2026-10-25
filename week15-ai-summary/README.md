# ✍️ 한눈요약 — Gemini AI 텍스트 요약 서비스

**15-2주차 Level#3 자유주제 — 클라우드 서비스 구현 및 배포**

- 🌐 **공개 배포 URL:** https://week15-ai-summary.streamlit.app/
- 📁 **GitHub 소스:** https://github.com/kim-dev83/my-first-project/tree/main/week15-ai-summary
- 기술: Python, Streamlit, Google Gemini API
- 실행 방식: 로컬 Streamlit 서버 또는 Streamlit Community Cloud
- 실습 확인일: 2026-10-25

## 주요 기능
1. 텍스트 입력 (25~12,000자 범위 검증)
2. **Gemini AI 실제 요약:** 핵심 3줄 / 한 문장 / 자세히
3. 결과를 TXT 파일로 다운로드
4. 데모 체험 (AI가 아닌 문장 추출, 명확히 표시)
5. API 키 분리 관리 및 사용자 친화적 오류 안내

## 프로젝트 구조
- `app.py`: Streamlit 웹 인터페이스
- `gemini_client.py`: Gemini API 호출 및 입력 검증
- `requirements.txt`: Streamlit 의존성
- `.env.example`: 키 이름과 모델 설정 예시 (실제 키는 포함하지 않음)
- `.gitignore`: `secrets.toml` 등 민감 파일 제외

## 로컬 실행 (Windows)
1. Python 3.11 이상 설치 후 이 폴더를 엽니다.
2. `python -m pip install -r requirements.txt`
3. 실제 AI 요약을 사용하려면 아래 경로에 설정 파일을 만듭니다. (절대 GitHub에 올리지 마세요.)

   **`.streamlit/secrets.toml`**
   ```toml
   GEMINI_API_KEY = "본인의_Gemini_API_키"
   ```

4. `python -m streamlit run app.py`
5. 브라우저에서 `http://localhost:8501`로 접속합니다.

로컬 네트워크 노출을 줄이려면:
```bash
python -m streamlit run app.py --server.address 127.0.0.1
```

## Streamlit Community Cloud 배포
1. https://share.streamlit.io 에서 GitHub 연동 후 `Create app`
2. Repository: `kim-dev83/my-first-project`
3. Branch: `main`
4. Main file path: `week15-ai-summary/app.py`
5. `Advanced settings > Secrets`에 `GEMINI_API_KEY` 등록
6. Deploy 후 공개 URL 접속 및 실제 Gemini AI 요약 테스트

Google AI Studio: https://aistudio.google.com/api-keys

## 실행 결과 및 제출 증빙
2026-10-25에 학습자가 공개 웹서비스와 로컬 서버에서 **Gemini AI 요약 완료 (gemini-3.5-flash-lite)** 메시지 및 요약 출력을 확인했습니다.
제출 ZIP에는 로컬 터미널, 로컬 브라우저, 공개 배포 결과, Secrets 키 가림 화면, AI Studio 무료 등급·API 사용량 화면을 포함합니다.

**중요: `gemini-2.5-flash` 모델로 호출 시 발생하던 HTTP 404 오류를 `gemini-3.5-flash-lite`로 변경해 해결했습니다.**

## API 사용량과 비용 관리
- AI Studio에서 **Default Gemini Project의 '무료 등급'** 표시 및 API 사용량을 확인했습니다.
- **무료 등급 표시만으로 월간 비용 상한을 별도로 설정했다고 주장하지 않습니다.**
- 유료 결제 설정과 상한 적용 여부는 별도 검증되지 않았습니다.
- 공개 앱의 Gemini API 요청은 프로젝트 계정의 한도/비용에 영향을 줄 수 있습니다. 프로젝트 대시보드에서 사용량을 정기적으로 확인하고, 필요 시 앱 접근을 제한합니다.
- API 키는 반드시 Secrets 또는 로컬 비공개 설정에서 관리하며, 캡처와 GitHub/ZIP에 포함하지 않습니다.

## 보안
실제 API 키를 앱 소스, README, 제출 ZIP, 스크린샷에 포함하지 않습니다. 공개에 노출된 키는 폐기한 뒤 새로 발급받아 `Secrets`에 재등록하세요.
