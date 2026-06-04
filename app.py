import streamlit as st
import streamlit.components.v1 as components
import datetime

# 1. 노션 특유의 미니멀하고 깔끔한 화이트 테마 기반 설정
st.set_page_config(
    page_title="💰 [Notion] 2026 자산 최적화 프로젝트", 
    page_icon="📝",
    layout="centered" # 노션처럼 가운데로 깔끔하게 모이도록 설정
)

# 2. ⚡ 부장님 감지 패닉 버튼 (스페이스바 연타 시 사내 ERP 데이터 시트로 대피)
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
    st.error("🔒 [보안] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026_전사_리소스_최적화_KPI_Data")
    st.dataframe({
        "Index": [1, 2, 3],
        "Task": ["Next-Gen ERP 구축", "Data Pipeline v3 안정화", "Core Sandbox 기획"],
        "Progress": ["94.2%", "81.2%", "45.0%"]
    }, use_container_width=True)
    if st.button("🔄 Notion 세션 새로고침"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# 🟢 AREA B: 노션 페이지로 완벽 위장한 껄무새 계산기
else:
    # 📊 고정 과거 데이터베이스 (실제 2026년 시세 반영)
    HISTORICAL_STOCK_DATA = {
        "삼성전자 (005930.KS)": {"current_price": 358250, "yearly_prices": [358250, 285000, 72500, 63100, 75500]},
        "SK하이닉스 (000660.KS)": {"current_price": 168000, "yearly_prices": [168000, 142000, 115000, 92000, 121000]},
        "엔비디아 (NVDA)": {"current_price": 125, "yearly_prices": [125, 85, 38, 16, 22]},
        "비트코인 (BTC-USD)": {"current_price": 68000, "yearly_prices": [68000, 52000, 28000, 39000, 46000]}
    }

    # --- 노션 특유의 상단 엠블럼 & 타이틀 UI 연출 ---
    st.markdown("""
        <div style="font-size: 75px; margin-bottom: 5px;">🦜</div>
        <h1 style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji'; font-weight: 700; color: #37352f; margin-top: 0; margin-bottom: 8px;">
            [개인] 일상 매몰비용의 자산 전환 시뮬레이터
        </h1>
        <div style="color: rgba(55, 53, 47, 0.6); font-size: 14px; margin-bottom: 20px;">
            <span>📁 개인 아카이브</span> • <span>👤 schan1232</span> • <span>📅 최종 수정일: 2026년 6월 4일</span>
        </div>
    """, unsafe_allow_html=True)

    # 노션의 Callout(콜아웃) 박스 스타일 구현
    st.markdown("""
        <div style="background-color: #f1f1ef; padding: 16px; border-radius: 4px; display: flex; gap: 12px; margin-bottom: 25px;">
            <div style="font-size: 20px;">💡</div>
            <div style="color: #37352f; font-size: 14px; line-height: 1.5;">
                <b>안내 및 보안 지침</b><br>
                본 페이지는 일상적인 고정 지출(담배, 커피 등)을 특정 자산에 적립식으로 투자했을 때의 실제 과거 주가 추이 기반 가치를 실시간으로 역산합니다.<br>
                <span style="color: #eb5757; font-weight: bold;">[🚨 월급루팡 전용 가드]</span> 뒤에 부장님이 접근 시 <b>[스페이스바 연속 2번]</b>을 누르면 즉시 사내 ERP 데이터셋으로 화면이 강제 전환됩니다.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚙️ 1. 데이터 추출 조건 설정")
    
    # 노션 서식처럼 깔끔하게 정돈된 입력 양식
    with st.form("notion_form"):
        col1, col2 = st.columns(2)
        with col1:
            habit = st.selectbox("🛍️ 소비성 경비 항목 선택", ["담배 (1갑 4,500원)", "스타벅스 아메리카노 (1잔 4,500원)", "배달음식 (1회 22,000원)"])
            count = st.slider("📊 주간 평균 소비 빈도 (회/갑)", 1, 14, 5)
        with col2:
            target_asset = st.selectbox("📈 연동 대상 주식/자산", ["삼성전자 (005930.KS)", "SK하이닉스 (000660.KS)", "엔비디아 (NVDA)", "비트코인 (BTC-USD)"])
            years = st.slider("⏳ 타임머신 추적 기간 (개년)", 1, 5, 3)
            
        submitted = st.form_submit_button("🔗 변경 데이터 반영하기 (Enter)")

    # --- 데이터 연산 및 노션식 결과 출력 ---
    if submitted:
        # 1. 시뮬레이션 연산 로직 (v5 완벽 계승)
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

        st.write("")
        st.markdown("### 📊 2. 실시간 연산 결과 테이블")
        
        # 노션의 보드(Board) 뷰 혹은 데이터베이스 요약 카드 스타일로 연출
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.markdown(f"""
                <div style="border: 1px solid #e9e9e6; padding: 15px; border-radius: 4px; background: #fff;">
                    <div style="font-size: 12px; color: #7c7b77; font-weight: 500;">🪙 길바닥 매몰 원금</div>
                    <div style="font-size: 22px; font-weight: 600; color: #37352f; margin-top: 5px;">{int(total_seed):,} 원</div>
                </div>
            """, unsafe_allow_html=True)
        with res_col2:
            st.markdown(f"""
                <div style="border: 1px solid #e9e9e6; padding: 15px; border-radius: 4px; background: #fff;">
                    <div style="font-size: 12px; color: #238356; font-weight: 500;">📈 현재 자산 가치</div>
                    <div style="font-size: 22px; font-weight: 600; color: #238356; margin-top: 5px;">{int(final_value):,} 원</div>
                    <div style="font-size: 11px; color: #7c7b77; margin-top: 2px;">(시세: {current_price:,}{price_unit} / {round(total_shares,2)}주)</div>
                </div>
            """, unsafe_allow_html=True)
        with res_col3:
            card_color = "#d4402a" if missed_money > 0 else "#2563eb"
            status_text = "🚨 놓친 기회비용" if missed_money > 0 else "🛡️ 방어한 자산"
            st.markdown(f"""
                <div style="border: 1px solid #e9e9e6; padding: 15px; border-radius: 4px; background: #fff;">
                    <div style="font-size: 12px; color: {card_color}; font-weight: 500;">{status_text}</div>
                    <div style="font-size: 22px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div>
                </div>
            """, unsafe_allow_html=True)

        # 노션의 인용구 블록(>)을 활용한 껄무새 팩폭 코멘트
        st.write("")
        st.markdown("### 💬 3. 데이터 분석 총평")
        
        if missed_money > 0:
            st.markdown(f"""
                <blockquote>
                    <b>🚨 [경고] 자산 파괴적 지출 패턴 감지됨</b><br>
                    과거 실제 차트 데이터를 매핑해 본 결과, 당신이 {years}년 동안 매주 {count}번씩 주둥이에 털어 넣은 돈을 <b>{target_asset}</b>에 적립했다면 오늘 날짜 기준으로 순수하게 더 벌 수 있었던 기회비용만 <b>{int(missed_money/10000):,}만 원</b>입니다. 이 돈이면 지금 회사에서 상사 눈치 보며 노션 켜놓는 대신 하와이 해변에서 칵테일 마시고 있었습니다. 당장 지출 관리 페이지를 생성하십시오.
                </blockquote>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <blockquote>
                    <b>😎 [양호] 합리적인 니코틴/카페인 소비 입증됨</b><br>
                    리스크 데이터 시뮬레이션 결과, 해당 기간 <b>{target_asset}</b>의 시장 성과가 매우 저조하여 주식을 샀다면 오히려 -{int(abs(missed_money/10000)):,}만 원의 원금 손실을 입었을 것입니다. 귀하가 담배와 커피를 맛있게 흡입하여 업무 스트레스를 방어한 것은 결과적으로 자산 손실을 완벽하게 헷지(Hedge)한 천재적인 재테크였습니다. 계속해서 맛있게 소비하십시오.
                </blockquote>
            """, unsafe_allow_html=True)
