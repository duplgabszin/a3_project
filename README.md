# WhereAreYou AI - AI 소재 파악기

## 1. 서비스 소개
이름과 생년월일을 기반으로 AI가 상대방의 가상 위치와 상태를 분석해주는 엔터테인먼트 서비스입니다.

## 2. 기술 스택
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Backend**: Python (Vercel Serverless Functions)
- **AI**: OpenAI GPT-3.5 API
- **Deployment**: Vercel

## 3. 배포 및 실행 방법
1. GitHub 저장소에 코드를 푸시합니다.
2. Vercel에서 프로젝트를 연결합니다.
3. Vercel 설정(Settings > Environment Variables)에서 `OPENAI_API_KEY`를 추가합니다.
4. 배포된 URL로 접속합니다.

## 4. 환경 변수 설정
- `OPENAI_API_KEY`: OpenAI에서 발급받은 API 키