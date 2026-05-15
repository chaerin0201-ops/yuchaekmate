import re

BASE = r"C:/Users/nsk35/Downloads/yuchaekmate_website (3)/"

def make_item(h4, p, svg_inner, delay=False):
    delay_class = ' reveal-delay-1' if delay else ''
    return f"""    <div class="service-item reveal{delay_class}">
      <div class="service-item-icon">
        <svg viewBox="0 0 24 24">{svg_inner}</svg>
      </div>
      <div>
        <h4>{h4}</h4>
        <p>{p}</p>
      </div>
    </div>"""

def make_section(title, subtitle, items):
    # items: list of (h4, p, svg_inner)
    item_htmls = []
    for i, (h4, p, svg_inner) in enumerate(items):
        # delay on items 2, 4, 6 (0-indexed: 1, 3, 5)
        delay = (i % 2 == 1)
        item_htmls.append(make_item(h4, p, svg_inner, delay))
    grid = "\n".join(item_htmls)
    return f"""
<!-- SERVICE CONTENT -->
<section class="service-content section">
  <div class="section-label reveal">
    <div class="section-label-line"></div>
    <div class="section-label-text">서비스 제공 내용</div>
  </div>
  <h2 class="section-title reveal reveal-delay-1">{title}</h2>
  <p class="section-sub reveal reveal-delay-2">{subtitle}</p>

  <div class="service-grid">
{grid}
  </div>
</section>

"""

# ─── CONTENT DEFINITIONS ────────────────────────────────────────────────────

pages = {}

# 1. yuchaekmate_court.html
pages["yuchaekmate_court.html"] = make_section(
    title="재판 출석 솔루션에<br><em>포함되는 내용</em>",
    subtitle="단순히 출석하는 것이 아니라, 사건을 충분히 이해한 전문가가 의뢰인의 입장에서 전략적으로 대응합니다.",
    items=[
        ("사건 기록 사전 검토",
         "소장, 준비서면, 증거 자료를 충분히 검토하여 출석 전 사건 전체를 파악합니다.",
         '<path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>'),
        ("기일 유형별 맞춤 전략 수립",
         "조정기일, 변론기일, 증인신문기일 등 기일 종류에 따라 최적의 대응 방향을 사전에 설계합니다.",
         '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>'),
        ("조정기일 출석 및 협상 대리",
         "조정위원과의 협상 자리에서 의뢰인의 이익을 최대화하는 방향으로 적극 대응합니다.",
         '<path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>'),
        ("변론기일 출석 및 주장 보완",
         "재판부에 핵심 쟁점을 명확히 전달하고, 필요 시 즉각적인 반박 주장을 전개합니다.",
         '<path d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>'),
        ("기일 후 결과 분석 및 보고",
         "기일 결과를 의뢰인에게 상세히 보고하고, 다음 기일을 위한 전략을 즉시 안내합니다.",
         '<path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>'),
        ("다음 기일 준비 연계 지원",
         "이번 기일 결과를 바탕으로 다음 기일 준비서면 작성 및 증거 보완 방향을 함께 검토합니다.",
         '<path d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>'),
    ]
)

# 2. yuchaekmate_writing.html
pages["yuchaekmate_writing.html"] = make_section(
    title="맞춤형 서면 솔루션에<br><em>포함되는 내용</em>",
    subtitle="서면 하나가 소송의 흐름을 바꿉니다. 사건의 구조와 목표를 반영한 전략적 서면을 작성합니다.",
    items=[
        ("사건 구조 및 주장 방향 설계",
         "서면 작성 전 사건 전체를 분석하여 어떤 주장을 어떤 순서로 전개할지 먼저 설계합니다.",
         '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>'),
        ("소장 및 준비서면 작성",
         "초기 소장부터 각 기일별 준비서면까지, 재판부를 설득하는 논리적 서면을 작성합니다.",
         '<path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>'),
        ("각종 신청서 작성",
         "증거보전 신청, 사실조회 신청, 문서제출명령 신청 등 절차상 필요한 신청서를 작성합니다.",
         '<path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>'),
        ("증거 목록 및 증거 설명서 작성",
         "보유 증거의 목록을 정리하고, 각 증거가 주장을 어떻게 뒷받침하는지 설명하는 서면을 작성합니다.",
         '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>'),
        ("답변서 및 반론서 작성",
         "상대방의 주장을 면밀히 분석하여 허점을 공략하고, 우리 측 입장을 명확히 반박하는 서면을 작성합니다.",
         '<path d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>'),
        ("제출 전 법적 검토 및 최종 수정",
         "완성된 서면을 제출 전 최종 검토하여 논리적 완결성과 법적 정확성을 확인합니다.",
         '<path d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/>'),
    ]
)

# 3. yuchaekmate_settle.html
pages["yuchaekmate_settle.html"] = make_section(
    title="합의 대행 솔루션에<br><em>포함되는 내용</em>",
    subtitle="기록을 남기지 않고 조용하게, 그러나 법적으로 완벽한 합의서로 사건을 완전히 마무리합니다.",
    items=[
        ("합의 전략 및 금액 범위 설계",
         "사건 구조와 증거를 분석하여 현실적으로 수용 가능한 합의 금액 범위와 협상 전략을 설계합니다.",
         '<path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>'),
        ("상대방 측 협상 대리",
         "의뢰인을 대신하여 상대방 또는 상대방 대리인과 직접 협상하여 유리한 조건을 이끌어냅니다.",
         '<path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>'),
        ("합의서 초안 작성",
         "합의 금액, 지급 방법, 이행 조건 등 합의 핵심 내용을 반영한 초안을 작성하여 검토를 진행합니다.",
         '<path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>'),
        ("위약벌·비밀유지 조항 설계",
         "합의 위반 시 자동 이행을 강제하는 위약벌 조항과, 사건이 외부에 알려지지 않도록 하는 비밀유지 조항을 정교하게 설계합니다.",
         '<path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>'),
        ("합의 이행 과정 관리",
         "합의서 체결 이후 이행 현황을 모니터링하고, 이행이 지연되는 경우 즉각적인 대응을 지원합니다.",
         '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>'),
        ("합의서 최종 검토 및 체결 지원",
         "완성된 합의서의 법적 효력을 최종 검토하고, 체결 절차 전반을 지원합니다.",
         '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>'),
    ]
)

# 4. yuchaekmate_notice.html
pages["yuchaekmate_notice.html"] = make_section(
    title="내용증명 솔루션에<br><em>포함되는 내용</em>",
    subtitle="단순한 통보가 아니라, 향후 소송과 연계되는 전략적 내용증명을 설계하고 발송합니다.",
    items=[
        ("발송 목적 및 전략 분석",
         "합의 유도, 경고, 소송 예고 등 의뢰인의 목표에 맞는 내용증명 발송 전략을 먼저 설계합니다.",
         '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>'),
        ("내용증명 초안 작성",
         "법적 요건을 갖춘 내용증명 초안을 작성하고, 의뢰인과 충분히 검토한 뒤 최종본을 완성합니다.",
         '<path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>'),
        ("법적 효력 검토",
         "작성된 내용증명이 법적 효력을 갖추었는지, 향후 소송에서 유리하게 활용될 수 있는지 검토합니다.",
         '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>'),
        ("발송 절차 지원",
         "내용증명 발송 절차 전반을 안내하고, 상대방에게 적법하게 도달될 수 있도록 지원합니다.",
         '<path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>'),
        ("상대방 반응 분석 및 후속 대응",
         "내용증명 수령 후 상대방의 반응을 분석하여, 합의 가능성 또는 소송 진행 여부를 판단합니다.",
         '<path d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>'),
        ("소송 연계 전략 안내",
         "내용증명으로 원하는 결과를 얻지 못한 경우, 소송 전환을 위한 다음 단계 전략을 안내합니다.",
         '<path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>'),
    ]
)

# 5. yuchaekmate_evidence.html
pages["yuchaekmate_evidence.html"] = make_section(
    title="증거 코칭 솔루션에<br><em>포함되는 내용</em>",
    subtitle="어떤 증거를 어떻게 확보하고 활용할지, 법적으로 안전하고 효과적인 방법을 설계합니다.",
    items=[
        ("보유 증거 적법성 검토",
         "현재 확보한 증거가 재판에서 사용 가능한지, 위법수집 증거로 배제될 가능성은 없는지 검토합니다.",
         '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>'),
        ("증거 증명력 평가",
         "각 증거의 법원 인정 가능성과 증명력 수준을 평가하여, 실제 재판에서의 활용 가치를 분석합니다.",
         '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>'),
        ("추가 증거 수집 방향 제시",
         "부족한 증거를 보완하기 위해 어떤 방법으로 추가 증거를 수집할 수 있는지 구체적인 방향을 제시합니다.",
         '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>'),
        ("합법적 증거 확보 방법 안내",
         "사실조회, 금융거래 조회, 통화 내역 조회 등 법원을 통한 합법적 증거 수집 방법을 안내합니다.",
         '<path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>'),
        ("증거보전 신청 전략",
         "상대방이 증거를 인멸할 우려가 있는 경우, 증거보전 신청을 통해 법원 차원에서 증거를 보존하는 방법을 지원합니다.",
         '<path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>'),
        ("소송 시 증거 활용 전략 설계",
         "확보한 증거를 소송에서 어떤 순서로, 어떻게 제출할지 전략적으로 설계하여 최대 효과를 냅니다.",
         '<path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>'),
    ]
)

# 6. yuchaekmate_criminal.html
pages["yuchaekmate_criminal.html"] = make_section(
    title="형사 대응 솔루션에<br><em>포함되는 내용</em>",
    subtitle="상간소송에서 파생되는 형사 이슈를 민사 전략과 연계하여 종합적으로 대응합니다.",
    items=[
        ("형사 쟁점 및 리스크 진단",
         "명예훼손, 정보통신망법위반, 협박, 스토킹 등 사건에서 발생 가능한 형사 이슈를 종합적으로 진단합니다.",
         '<path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>'),
        ("고소장 작성",
         "형사 고소 요건을 갖춘 고소장을 작성하고, 증거 자료와 함께 수사기관에 제출하는 절차를 지원합니다.",
         '<path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>'),
        ("의견서·진술서 작성",
         "수사 과정에서 필요한 의견서, 고소 보충 진술서, 피해 경위서 등을 작성합니다.",
         '<path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>'),
        ("수사기관 출석 동행",
         "경찰·검찰 조사에 변호사가 직접 동행하여 진술 방향을 조율하고 의뢰인의 권리를 보호합니다.",
         '<path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>'),
        ("민사·형사 연계 전략 설계",
         "상간소송(민사)과 형사 고소를 어떻게 연계할지 종합적인 전략을 설계하여 최대 효과를 냅니다.",
         '<path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>'),
        ("사후 재분쟁 방지 설계",
         "형사 사건 종결 후에도 재분쟁 가능성을 최소화하는 사후 장치를 설계합니다.",
         '<path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>'),
    ]
)

# 7. yuchaekmate_plaintiff.html
pages["yuchaekmate_plaintiff.html"] = make_section(
    title="원고 맞춤형 솔루션에<br><em>포함되는 내용</em>",
    subtitle="위자료 극대화와 강력한 책임 추궁을 목표로, 소송 전략부터 판결까지 모든 과정을 설계합니다.",
    items=[
        ("초기 사건 진단 및 전략 수립",
         "사건 구조, 증거 수준, 예상 위자료를 분석하여 승소 가능성을 극대화하는 소송 전략을 수립합니다.",
         '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>'),
        ("증거 확보 및 보강",
         "기존 증거의 증명력을 평가하고, 사실조회·증거보전 등 합법적 방법을 통해 추가 증거를 확보합니다.",
         '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>'),
        ("전 과정 서면 작성",
         "소장, 준비서면, 각종 신청서 등을 필요에 따라 무제한 작성하여 재판부를 설득합니다.",
         '<path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>'),
        ("모든 기일 변호사 직접 출석",
         "조정기일, 변론기일, 증인신문기일 등 모든 기일에 변호사가 직접 출석하여 의뢰인의 이익을 대변합니다.",
         '<path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/>'),
        ("합의·소송 전략 병행",
         "소송 진행 중에도 유리한 합의 조건이 형성되면 즉각 대응하여 최적의 결과를 확보합니다.",
         '<path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>'),
        ("판결 이후 재분쟁 방지 설계",
         "위약벌·비밀유지 조항 설계부터 강제집행 준비까지, 사건이 완전히 마무리될 수 있도록 사후 장치를 구축합니다.",
         '<path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>'),
    ]
)

# 8. yuchaekmate_defendant.html
pages["yuchaekmate_defendant.html"] = make_section(
    title="피고 맞춤형 솔루션에<br><em>포함되는 내용</em>",
    subtitle="원고의 주장을 정밀하게 분석하고 허점을 공략하여, 과도한 위자료 청구로부터 의뢰인을 보호합니다.",
    items=[
        ("원고 주장 분석 및 허점 파악",
         "소장과 제출 증거를 면밀히 검토하여 원고 주장의 논리적 허점과 사실관계 오류를 파악합니다.",
         '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>'),
        ("혼인파탄 선행 여부 검토",
         "상간행위 이전에 이미 혼인 관계가 파탄된 상태였는지 입증하여 위자료 감액 또는 면책을 주장합니다.",
         '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>'),
        ("인지 여부 주장 전략 수립",
         "상대방이 기혼자임을 인지하지 못했다는 주장의 가능성을 검토하고, 이를 뒷받침할 증거를 확보합니다.",
         '<path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>'),
        ("위자료 감액 포인트 정밀 공략",
         "혼인 기간, 유책 정도, 경제 상황 등 위자료를 낮출 수 있는 모든 감액 요소를 정밀하게 공략합니다.",
         '<path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>'),
        ("방어 준비서면 및 답변서 작성",
         "원고의 주장을 조목조목 반박하는 논리적인 답변서와 준비서면을 작성합니다.",
         '<path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>'),
        ("합의 또는 소송 전략 선택 지원",
         "소송을 끝까지 진행할지, 유리한 조건에서 합의할지 상황에 맞는 최적의 전략을 함께 결정합니다.",
         '<path d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>'),
    ]
)

# ─── INSERT INTO FILES ───────────────────────────────────────────────────────

def find_insertion_point(content):
    """
    Find the position right after the closing </section> of the for-whom section
    and before the <!-- PROCESS --> comment / <section class="process-section section">.
    We look for the pattern: </section> followed (with possible whitespace/comments)
    by a line containing 'process-section section'.
    """
    # Find the process-section line
    process_match = re.search(r'<section class="process-section section">', content)
    if not process_match:
        return None, None

    process_start = process_match.start()

    # Look backward from process_start for the last </section> before it
    # Also account for the <!-- PROCESS --> comment that may precede it
    before_process = content[:process_start]

    # Find the last </section> in the text before process-section
    last_section_end = before_process.rfind('</section>')
    if last_section_end == -1:
        return None, None

    # Insertion point is right after that </section>
    insert_pos = last_section_end + len('</section>')
    return insert_pos, process_start

results = []
for filename, html_to_insert in pages.items():
    filepath = BASE + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already inserted
    if 'service-content section' in content:
        results.append(f"SKIP {filename}: already has service-content section")
        continue

    insert_pos, process_start = find_insertion_point(content)
    if insert_pos is None:
        results.append(f"ERROR {filename}: could not find insertion point")
        continue

    new_content = content[:insert_pos] + "\n" + html_to_insert + content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    results.append(f"OK    {filename}: inserted at position {insert_pos}")

print("\n".join(results))
