// 카카오톡 상담 링크를 Firestore(settings/kakao)에서 실시간으로 읽어온다.
//
// 예전에는 localStorage에 저장해서 관리자 본인 브라우저에서만 링크가 살아
// 있었고, 방문자는 "링크가 설정되지 않았습니다" 알림만 봤다. 이제 관리자가
// 저장하면 모든 방문자에게 곧바로 반영된다.
//
// 이 파일은 페이지에 Firebase가 이미 있든 없든 동작한다 (getApps로 중복 초기화 방지).

import { initializeApp, getApps, getApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getFirestore, doc, onSnapshot } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyBaiWWlPqhp4UqwVAZMustQih0ASdQ2Beg",
  authDomain: "uckeckmate-9c10c.firebaseapp.com",
  projectId: "uckeckmate-9c10c",
  storageBucket: "uckeckmate-9c10c.firebasestorage.app",
  messagingSenderId: "760016514105",
  appId: "1:760016514105:web:f176adf6c39de06fdbb1e8"
};

const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
const db = getFirestore(app);

function applyUrl(url) {
  window.__kakaoUrl = url || '';
  document.querySelectorAll('#kakao-link').forEach(function (el) {
    if (url) el.href = url;
  });
}

// 클릭은 위임으로 처리한다. 이 모듈이 늦게 로드돼도, 버튼이 나중에 그려져도
// 동작하고, 페이지마다 인라인 onclick을 두지 않아도 된다.
document.addEventListener('click', function (e) {
  var el = e.target.closest('#kakao-link, #float-kakao');
  if (!el) return;
  e.preventDefault();
  var url = window.__kakaoUrl || localStorage.getItem('ycm_kakao_url') || '';
  if (url && url !== '#') {
    window.open(url, '_blank');
  } else {
    alert('카카오톡 상담 링크가 아직 설정되지 않았습니다.');
  }
});

onSnapshot(
  doc(db, 'settings', 'kakao'),
  function (snap) {
    applyUrl(snap.exists() ? (snap.data().url || '') : '');
  },
  function (err) {
    console.warn('카카오 링크 로드 실패:', err.message);
  }
);
