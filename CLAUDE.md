# 유책메이트 웹사이트

정적 HTML/CSS 사이트. 프레임워크나 빌드 과정 없이 루트의 `.html`/`.css` 파일을 그대로 배포한다.

## 배포 방식

- GitHub 저장소: `chaerin0201-ops/yuchaekmate` (origin, main 브랜치)
- Vercel 프로젝트: `yuchaekmate` (`.vercel/project.json`에 링크됨)
- 프로덕션 도메인: https://www.yucheckmate.com/
- **`main` 브랜치에 push하면 Vercel이 GitHub 연동을 통해 자동으로 빌드 없이 배포한다.** 별도의 `vercel deploy` 명령이 필요 없다.

## 작업 흐름

1. 사용자가 수정사항을 요청하면 해당 `.html`/`.css`/이미지 파일을 수정한다.
2. 로컬에서 확인이 필요하면 `.claude/launch.json`의 "Static File Server (Python)" 설정으로 미리보기한다 (포트 3456).
3. 수정이 끝나면 변경 파일을 커밋한다.
4. **push하기 전에 항상 사용자에게 확인을 받는다** (사용자가 명시적으로 선택한 방식 — 자동 push 금지). 확인 후 `git push origin main`을 실행하면 몇 분 내로 실제 사이트에 반영된다.

## 참고

- 주요 페이지 파일: `index.html`(랜딩), `yuchaekmate_*.html`(하위 페이지들), `yuchaekmate_admin.html`(관리자용으로 보임 — 수정 시 주의)
- `insert_service_content.py`는 콘텐츠 삽입용 스크립트로 보임, 사이트 런타임과 무관
