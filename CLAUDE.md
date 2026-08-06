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

## 홈페이지 디자인 (index.html)

2026-08 기준 다크 테마로 리디자인됨. 참고한 톤: myungryanglaw.com, lawus.co.kr.

- 색: 배경 `--ink` #121212, 포인트 `--burgundy` #8E2237, 액센트 `--gold` #B8976A. 섹션마다 다크 → 라이트(`--paper` #F1F0EE) 교차.
- 섹션별 대형 영문 워터마크(`::before`/`::after`의 `content`): 히어로 YUCHAEKMATE, WHY US, SERVICE, AI PREDICT.
- 히어로 배경은 `hero-video.mp4`(Pexels 8347237, 무료 상업이용). 768px 이하와 데이터 세이버 환경에서는 영상을 아예 받지 않고 `hero-poster.jpg`만 표시한다 (`initHeroVideo()`가 `data-src`를 조건부로 붙임).
- 포스터 이미지는 영상 프레임을 캔버스로 캡처해 만든 것이라, 영상을 바꾸면 포스터도 다시 만들어야 한다.
- 우측 고정 버튼(`.float-btns`)이 콘텐츠를 가리지 않도록 데스크톱은 섹션 `padding-right: 108px`, 모바일은 아이콘만 남긴 46px 레일을 상담바 위에 배치한다.

## 하위 페이지 다크 테마

하위 페이지 17개도 다크로 전환됨. 홈과 달리 밝은 교차 섹션 없이 전체가 어둡다.

- 각 페이지가 `<style>`을 따로 들고 있어서, `:root` 값을 바꾸고 선언을 일괄 치환하는 방식으로 변환했다.
- **변수 이름이 아니라 속성 기준으로 봐야 한다.** 같은 `var(--white)`가 한 줄에서는 카드 배경이고 다음 줄에서는 본문 글자색이다. 그래서 배경 용도는 `--panel`/`--ink`로 바꾸고, 글자 용도의 `--white`·`--charcoal` 계열은 이름을 그대로 두되 `:root`에서 밝은 값으로 재정의했다.
- `--charcoal`은 이제 **밝은 글자색**이다. 배경에 쓰면 안 된다 (`--panel-2` 사용).
- 어두운 배경에서 `#8E2237` 버건디 글자는 안 읽혀서, 글자용은 `--burgundy-on-dark`(#E0A0AC) 로즈로 분리했다. 배경·테두리용 `--burgundy`는 그대로.
- 홈(index.html)은 밝은 섹션(`--paper`)이 있으므로 이 일괄 변환을 돌리면 안 된다. 밝은 배경 위에서는 원래의 진한 버건디가 맞다.

## 참고

- 주요 페이지 파일: `index.html`(랜딩), `yuchaekmate_*.html`(하위 페이지들), `yuchaekmate_admin.html`(관리자용으로 보임 — 다크 전환 대상에서 제외)
- `yuchaekmate_landing.html`은 index.html의 옛 사본. 어디에서도 링크되지 않으며 다크 리디자인도 적용 안 됨.
- 로고·홈 링크는 `yuchaekmate_landing.html`이 아니라 루트(`/`)를 가리킨다.
- `insert_service_content.py`는 콘텐츠 삽입용 스크립트로 보임, 사이트 런타임과 무관
