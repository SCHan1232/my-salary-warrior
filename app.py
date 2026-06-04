import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="업무 효율화 도구 (통계 분석 시스템)", layout="wide"
)

# 2. ⚡ 부장님 감지 단축키 (Space바 연속 2번) 자바스크립트 주입
js_panic_script = """
<script>
    let lastKeyTime = 0;
    window.parent.document.addEventListener('keydown', function(e) {
        if (e.code === 'Space') {
            const currentTime = new Date().getTime();
            const keyGap = currentTime - lastKeyTime;
            if (keyGap < 300) {  
                const url = new URL(window.parent.location.href);
                url.searchParams.set('boss_mode', 'true');
                window.parent.location.href = url.href;
            }
            lastKeyTime = currentTime;
        }
    });
</script>
"""
components.html(js_panic_script, height=0, width=0)

# 3. 최신 Streamlit 규격에 맞춘 쿼리 파라미터 읽기 (에러 완벽 방지)
is_boss_mode = st.query_params.get("boss_mode", "false") == "true"

# -----------------------------------------------------------------------------
# 🔴 AREA A: 부장님 모드 (진짜 일하는 척하는 ERP 화면)
# -----------------------------------------------------------------------------
if is_boss_mode:
    st.error(
        "🔒 [보안 네트워크] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다."
    )
    st.title("📊 2026년 상반기 전사 리소스 효율성 및 정량 지표 분석 보고서")
    st.caption("작성자: 디지털혁신본부 | 보안등급: 대외비 (Class A)")

    col1, col2, col3 = st.columns(3)
    col1.metric(
        label="전사 인프라 가동률 (Overall OEE)",
        value="94.28%",
        delta="0.45% (상승)",
    )
    col2.metric(
        label="클라우드 비용 최적화 지수 (FinOps)",
        value="81.20",
        delta="-1.5% (절감 필요)",
    )
    col3.metric(
        label="API 호출 레이턴시 (p99)", value="12.4 ms", delta="-2.1 ms (개선)"
    )

    st.subheader("📝 분기별 데이터 트렌드 요약 데이터셋")
    st.dataframe(
        {
            "부서코드": ["DE-01", "DE-02", "MK-04", "HR-02", "ST-09"],
            "프로젝트명": [
                "Next-Gen ERP",
                "Data Pipeline v3",
                "Global Viral Target",
                "OKR Automator",
                "Core Sandbox",
            ],
            "예산 집행률": ["87.5%", "92.1%", "45.0%", "100.0%", "12.3%"],
            "진척도 (KPI)": ["완료", "검증 중", "지연", "정상", "기획단계"],
        },
        use_container_width=True,
    )

    # 안전 구역 복구 버튼 수정
    if st.button("🔄 시스템 세션 재연결 (안전 구역으로 돌아가기)"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# -----------------------------------------------------------------------------
# 🟢 AREA B: 원래 놀던 모드 (껄무새 영끌 타임머신 계산기)
# -----------------------------------------------------------------------------
else:
    st.title("💸 껄무새의 영끌 청산 타임머신 🦜")
    st.subheader(
        "과거의 배달 고기 값을 엔비디아나 비트코인에 태웠다면 내 인생은 어떻게 변했을까?"
    )
    st.info(
        "🚨 [경고] 뒤에 상사나 부장님이 접근하면 즉시 [스페이스바를 탁! 탁!] 두 번 연타하세요. 완벽한 일잘러 화면으로 순간이동합니다."
    )

    st.write("---")

    with st.form("ggul_form"):
        col1, col2 = st.columns(2)
        with col1:
            asset = st.selectbox(
                "당시 영끌하고 싶었던 자산 선택",
                [
                    "엔비디아 (NVDA)",
                    "테슬라 (TSLA)",
                    "비트코인 (BTC)",
                    "삼성전자 (005930)",
                ],
            )
            period = st.slider("몇 년 전으로 돌아가시겠습니까? (타임머신 작동)", 1, 5, 3)
        with col2:
            seed_money = st.number_input(
                "그때 아낀 배달비 및 영끌 자금 (만원 단위)",
                min_value=10,
                max_value=5000,
                value=500,
                step=50,
            )
            leverage = st.checkbox("신용 대출 / 레버리지 영끌 포함 (위험도 200%)")

        submitted = st.form_submit_with_button("🚀 타임머신 가동 및 정산하기")

    if submitted:
        multiplier = {
            "엔비디아 (NVDA)": 12.5,
            "테슬라 (TSLA)": 0.8,
            "비트코인 (BTC)": 4.2,
            "삼성전자 (005930)": 0.95,
        }
        rate = multiplier[asset]
        if leverage:
            rate = rate * 2.5

        final_asset = seed_money * rate
        profit = final_asset - seed_money

        st.success("🤖 타임머신 분석이 완료되었습니다!")

        m_col1, m_col2 = st.columns(2)
        m_col1.metric(label="현재 내 통장 잔고여야 했을 금액", value=f"{int(final_asset):,} 만원")
        m_col2.metric(
            label="날려버린 내 조기 퇴사의 기회비용",
            value=f"{int(profit):,} 만원",
            delta=f"{int(rate*100)}%",
        )

        if profit > 0:
            st.warning(
                f"🦜 껄... 껄... 그때 {asset}에 대가리 깨져도 박았어야 했는데... 당신은 지금 회사에서 부장님 눈치를 보는 대신 한강 뷰 아파트에서 샴페인을 터뜨리고 있었을 것입니다."
            )
        else:
            st.error(
                f"🦜 오히려 좋아! 그때 하필 {asset}에 영끌했다가 청산당하고 지금 진짜 한강에 있을 뻔했습니다. 부장님께 감사하며 주간 보고서를 더 열심히 쓰십시오."
            )
