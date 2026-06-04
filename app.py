import streamlit as st
import streamlit.components.v1 as components
import datetime

# 1. 아웃룩/지메일 감성의 화이트 오피스 테마 페이지 설정
st.set_page_config(
    page_title="Microsoft Outlook - 받은 메일함", 
    page_icon="📩",
    layout="wide"
)

# 2. ⚡ 부장님 감지 패닉 버튼 (스페이스바 연타 시 진짜 엑셀 데이터 시트로 도망)
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
is_boss_mode = st.query_params.get("boss_mode", "false") == "true"

# 🔴 AREA A: 진짜 대외비 업무 데이터 화면 (부장님 방어막)
if is_boss_mode:
    st.error("🔒 [보안 네트워크] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026년 전사 인프라 리소스 최적화 정량 지표 데이터셋")
    st.dataframe({
        "부서코드": ["DE-01", "DE-02", "MK-04", "HR-02"],
        "프로젝트명": ["Next-Gen ERP", "Data Pipeline v3", "Global Viral", "OKR Auto"],
        "가동률": ["94.2%", "81.2%", "45.0%", "100.0%"]
    }, use_container_width=True)
    if st.button("🔄 메일 시스템 세션 재연결"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# 🟢 AREA B: 메일 창으로 위장한 껄무새 계산기
else:
    # 📊 고정 과거 데이터베이스 (v5 로직 계승)
    HISTORICAL_STOCK_DATA = {
        "삼성전자 (005930.KS)": {"current_price": 358250, "yearly_prices": [358250, 285000, 72500, 63100, 75500]},
        "SK하이닉스 (000660.KS)": {"current_price": 168000, "yearly_prices": [168000, 142000, 115000, 92000, 121000]},
        "엔비디아 (NVDA)": {"current_price": 125, "yearly_prices": [125, 85, 38, 16, 22]},
        "비트코인 (BTC-USD)": {"current_price": 68000, "yearly_prices": [68000, 52000, 28000, 39000, 46000]}
    }

    # --- UI 상단 오피스 네비게이션 바 연출 ---
    st.markdown("""
        <div style="background-color: #0078d4; padding: 12px; border-radius: 5px; margin-bottom: 20px;">
            <h3 style="color: white; margin: 0; font-family: sans-serif;">✉️ Outlook Web Mail - 인트라넷 시스템</h3>
        </div>
    """, unsafe_allow_html=True)

    # --- 좌측 사이드바: 메일함 메뉴 구성 ---
    with st.sidebar:
        st.markdown("### 📁 폴더 바로가기")
        st.write("📥 **받은메일함 (3)**")
        st.text("📤 보낸메일함")
        st.text("📝 임시보관함 (12)")
        st.text("🗑️ 지운메일함")
        st.write("---")
        st.info("💡 **[긴급 보안]** 부장님이 다가오면 언제든 **[스페이스바 2번]** 연타하세요. 즉시 대외비 서버 데이터 화면으로 전환됩니다.")

    # --- 중앙 화면: 메일 리스트 및 입력창 설계 ---
    st.markdown("### 📥 받은메일함 (최근 보관 파일)")
    
    with st.form("mail_form"):
        st.markdown("⚠️ **시스템 안내:** 개인 자산 진단 및 지출 패턴 메일 보고서를 생성하려면 아래 옵션을 선택 후 조회하십시오.")
        
        col1, col2 = st.columns(2)
        with col1:
            habit = st.selectbox("📌 [발신인: 재무기획팀] 지출성 경비 분류", ["담배 (1갑 4,500원)", "스타벅스 아메리카노 (1잔 4,500원)", "배달음식 (1회 22,000원)"])
            count = st.slider("📊 [빈도 체크] 주간 평균 소비 횟수", 1, 14, 5)
        with col2:
            target_asset = st.selectbox("📈 [대체 자산] 연동할 목적 투자 종목", ["삼성전자 (005930.KS)", "SK하이닉스 (000660.KS)", "엔비디아 (NVDA)", "비트코인 (BTC-USD)"])
            years = st.slider("⏳ [기간 설정] 데이터 추적 연한 (년)", 1, 5, 3)
            
        submitted = st.form_submit_button("📬 메일 본문 읽기 (컴파일)")

    # --- 메일 본문 (정산 결과) 연출 ---
    if submitted:
        # 계산 로직 (v5 완벽 계승)
        unit_price = 4500 if habit != "배달음식 (1회 22,000원)" else 22000
        weekly_expense = unit_price * count
        yearly_budget = weekly_expense * 52
        total_seed = yearly_budget * years
        
        asset_info = HISTORICAL_STOCK_DATA[target_asset]
        current_price = asset_info["current_price"]
        prices_history = asset_info["yearly_prices"][:years+1]
        
        total_shares = 0.0
        for i in range(years):
            past_price = prices_history[years - i]
            total_shares += yearly_budget / past_price
            
        is_foreign = "NVDA" in target_asset or "BTC-USD" in target_asset
        exchange_rate = 1350 if is_foreign else 1
        final_value = total_shares * current_price * exchange_rate
        price_unit = "$" if is_foreign else "원"
        missed_money = final_value - total_seed

        # 📨 지메일/아웃룩 본문 스타일로 결과 화면 꾸미기
        st.write("---")
        st.markdown(f"""
            <div style="background-color: #f3f2f1; padding: 20px; border-left: 5px solid #0078d4; border-radius: 4px;">
                <p style="margin: 0; color: #605e5c;"><b>발신인:</b> 재무관리본부 리스크관리팀 (audit@company.com)</p>
                <p style="margin: 5px 0; color: #605e5c;"><b>수신인:</b> 사내 임직원 귀하</p>
                <p style="margin: 5px 0; color: #201f1e;"><b>제목:</b> 📢 [엄중 경고] 귀하가 {years}년간 버린 지출에 대한 리스크 실시간 감사 결과보고</p>
                <hr style="border-top: 1px solid #edebe9;">
                <p style="color: #323130; line-height: 1.6;">
                    본 메일은 사내 임직원의 일상 소비 자금(담배/커피/배달)을 <b>{target_asset}</b> 자산으로 대체 적립했을 경우의 시뮬레이션 가치를 실시간으로 진단한 결과 문서입니다.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        
        # 메일 첨부파일 표 형태의 계정 스코어보드
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.metric(label="📁 누적 손실 원금 (매몰 비용)", value=f"{int(total_seed):,} 원")
        with res_col2:
            st.metric(label="📈 미매수 주식 평가 금액 (현재가 기준)", value=f"{int(final_value):,} 원", delta=f"{round(total_shares, 2)} 주 보유 분")
        with res_col3:
            if missed_money > 0:
                st.metric(label="🚨 기회비용 최종 손실액", value=f"- {int(missed_money):,} 원", delta="기회 상실", delta_color="inverse")
            else:
                st.metric(label="🛡️ 리스크 방어 이득액", value=f"+ {int(abs(missed_money)):,} 원", delta="손실 방어")

        # 메일 하단 껄무새 감사평 (말투를 약간 직장 선배 톤으로 위장하되 팩폭 유지)
        st.write("---")
        st.markdown("### 📋 감사실 종합 의견")
        if missed_money > 0:
            st.warning(f"**[종합 의견: 심각]**")
            st.markdown(f"귀하가 매주 {count}회씩 영혼 없이 소비한 자금을 **{target_asset}**에 적립식으로 던졌다면, 금일 기준 손에 쥘 수 있었던 순수 초과 수익만 **{int(missed_money/10000):,}만 원**에 달합니다. 감사실 판단하에 귀하는 지금 회사에서 부장님 눈치를 보는 대신 한강 뷰 아파트에서 연봉 협상을 하고 있었어야 마땅합니다. 조속히 지출 구조를 개혁하십시오.")
        else:
            st.success(f"**[종합 의견: 양호]**")
            st.markdown(f"리스크 관리팀 추적 결과, 해당 기간 **{target_asset}** 시장 수익률이 처참하여 주식을 샀다면 오히려 원금을 까먹고 -{int(abs(missed_money/10000)):,}만 원의 자산 손실을 입었을 것으로 판단됩니다. 담배와 스타벅스를 맛있게 흡입하여 사내 스트레스를 방어한 귀하의 행동은 결과적으로 '인생 최고의 재테크 헷지'였음을 인정합니다. 현상 유지를 권장합니다.")
