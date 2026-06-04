import streamlit as st
import streamlit.components.v1 as components
import datetime

# 1. 제미나이 검색 및 다크모드 환경에 최적화된 설정
st.set_page_config(
    page_title="✨ Gemini - 자산 최적화 시뮬레이션 v6", 
    page_icon="✨",
    layout="centered" 
)

# 2. ⚡ 부장님 감지 패닉 버튼 (스페이스바 연타 시 사내 ERP 화면으로 대피)
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

# 🔴 AREA A: 부장님 방어막 (사내 ERP 화면)
if is_boss_mode:
    st.error("🔒 [보안] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026_전사_리소스_최적화_KPI_Data")
    st.dataframe({
        "Index": [1, 2, 3],
        "Task": ["Next-Gen ERP 구축", "Data Pipeline v3 안정화", "Core Sandbox 기획"],
        "Progress": ["94.2%", "81.2%", "45.0%"]
    }, use_container_width=True)
    if st.button("🔄 Gemini 세션 새로고침"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# 🟢 AREA B: 제미나이 검색창으로 위장한 초정밀 팩폭 계산기
else:
    # 📊 고정 과거 데이터베이스 (반도체 벨트 라인업)
    HISTORICAL_STOCK_DATA = {
        "삼성전자 (005930.KS)": {"current_price": 358250, "yearly_prices": [358250, 285000, 72500, 63100, 75500]},
        "SK하이닉스 (000660.KS)": {"current_price": 168000, "yearly_prices": [168000, 142000, 115000, 92000, 121000]},
        "한미반도체 (042700.KS)": {"current_price": 142500, "yearly_prices": [142500, 118000, 61000, 14500, 18500]},
        "엔비디아 (NVDA)": {"current_price": 125, "yearly_prices": [125, 85, 38, 16, 22]},
        "마이크론 (MU)": {"current_price": 132, "yearly_prices": [132, 110, 68, 55, 74]},
        "샌디스크/웨스턴디지털 (WDC)": {"current_price": 72, "yearly_prices": [72, 64, 42, 38, 52]}
    }

    # --- 제미나이 특유의 미니멀 로고 및 프롬프트 타이틀 디자인 ---
    st.markdown("""
        <div style="margin-bottom: 10px;">
            <span style="font-size: 32px; font-weight: 700; background: linear-gradient(45deg, #4285F4, #9B51E0, #E91E63); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                ✨ Gemini
            </span>
        </div>
        <h2 style="font-family: sans-serif; font-weight: 400; color: #FFFFFF; margin-top: 0; margin-bottom: 25px; font-size: 24px;">
            무엇을 도와드릴까요? 일상 소비 효율성 및 미래 자산을 예측합니다.
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("##### 🔍 시뮬레이션 프롬프트 설정")
    
    with st.form("gemini_form"):
        col1, col2 = st.columns(2)
        with col1:
            habit = st.selectbox(
                "🛍️ 매달 '흐린 눈'으로 지출 중인 항목", 
                [
                    "탕후루/마라탕 쿨타임 (1회 18,000원)",
                    "스타벅스 바닐라라떼+디저트 (1회 11,000원)", 
                    "올리브영 세일 '구경만' 하기 (1회 45,000원)",
                    "불금 배달 엽떡+치킨 (1회 32,000원)",
                    "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)",
                    "한 달에 한 번 속눈썹/네일 정기권 (1회 55,000원)"
                ]
            )
            count = st.slider("📊 주간 평균 소비 빈도", 1, 14, 3)
        with col2:
            target_asset = st.selectbox(
                "📈 연동할 목적 자산 (반도체/AI 벨트)", 
                [
                    "삼성전자 (005930.KS)", 
                    "SK하이닉스 (000660.KS)", 
                    "한미반도체 (042700.KS)",
                    "엔비디아 (NVDA)", 
                    "마이크론 (MU)", 
                    "샌디스크/웨스턴디지털 (WDC)"
                ]
            )
            years = st.slider("⏳ 타임머신 추적 기간 (년)", 1, 5, 3)
            
        submitted = st.form_submit_button("✨ 제미나이 타임머신 및 미래 예측 가동 (Enter)")

    # --- 데이터 연산 및 결과 출력 ---
    if submitted:
        price_dict = {
            "탕후루/마라탕 쿨타임 (1회 18,000원)": 18000,
            "스타벅스 바닐라라떼+디저트 (1회 11,000원)": 11000,
            "올리브영 세일 '구경만' 하기 (1회 45,000원)": 45000,
            "불금 배달 엽떡+치킨 (1회 32,000원)": 32000,
            "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": 65000,
            "한 달에 한 번 속눈썹/네일 정기권 (1회 55,000원)": 55000
        }
        unit_price = price_dict[habit]
        weekly_expense = unit_price * count
        yearly_budget = weekly_expense * 52
        total_seed = yearly_budget * years
        
        asset_info = HISTORICAL_STOCK_DATA[target_asset]
        current_price = asset_info["current_price"]
        prices_history = asset_info["yearly_prices"][:years+1]
        
        # 1. 과거 적립식 매수 시뮬레이션
        total_shares = 0.0
        for i in range(years):
            past_price = prices_history[years - i]
            total_shares += yearly_budget / past_price
            
        is_foreign = ".KS" not in target_asset
        exchange_rate = 1350 if is_foreign else 1
        final_value = total_shares * current_price * exchange_rate
        price_unit = "$" if is_foreign else "원"
        missed_money = final_value - total_seed

        # 2. 미래 복리 예측 연산
        total_return_rate = final_value / total_seed if total_seed > 0 else 1.0
        total_weeks = years * 52
        
        if total_return_rate > 0:
            weekly_growth_rate = (total_return_rate) ** (1 / total_weeks) - 1
        else:
            weekly_growth_rate = 0.0
            
        future_value = final_value * total_return_rate

        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>📊 1. 과거 데이터 기반 실시간 정산</h3>", unsafe_allow_html=True)
        
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.markdown(f"""
                <div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;">
                    <div style="font-size: 12px; color: #AAADB0; font-weight: 500;">🪙 총 지출 매몰 원금</div>
                    <div style="font-size: 22px; font-weight: 600; color: #FFFFFF; margin-top: 5px;">{int(total_seed):,} 원</div>
                </div>
            """, unsafe_allow_html=True)
        with res_col2:
            st.markdown(f"""
                <div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;">
                    <div style="font-size: 12px; color: #81C995; font-weight: 500;">📈 현재 자산 가치 (오늘)</div>
                    <div style="font-size: 22px; font-weight: 600; color: #81C995; margin-top: 5px;">{int(final_value):,} 원</div>
                    <div style="font-size: 11px; color: #AAADB0; margin-top: 2px;">({round(total_shares,2)}주 보유 중)</div>
                </div>
            """, unsafe_allow_html=True)
        with res_col3:
            card_color = "#F28B82" if missed_money > 0 else "#8AB4F8"
            status_text = "🚨 기회상실 순손실액" if missed_money > 0 else "🛡️ 리스크 최종 방어액"
            st.markdown(f"""
                <div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;">
                    <div style="font-size: 12px; color: {card_color}; font-weight: 500;">{status_text}</div>
                    <div style="font-size: 22px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div>
                </div>
            """, unsafe_allow_html=True)

        # 미래 행복회로 예측 스코어보드
        st.write("")
        st.markdown(f"<h3 style='color: #FFFFFF; font-size: 18px;'>🔮 2. 미래 {years}년 뒤 자산 행복회로 예측</h3>", unsafe_allow_html=True)
        
        fut_col1, fut_col2 = st.columns(2)
        with fut_col1:
            st.markdown(f"""
                <div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;">
                    <div style="font-size: 12px; color: #D6BCFA; font-weight: 500;">⚡ 과거 주봉 평균 상승률 (복리 기준)</div>
                    <div style="font-size: 24px; font-weight: 600; color: #D6BCFA; margin-top: 5px;">{weekly_growth_rate*100:+.4f} % / 주</div>
                    <div style="font-size: 11px; color: #AAADB0; margin-top: 2px;">(과거 {years}년간의 누적 에너지를 주 단위로 환산)</div>
                </div>
            """, unsafe_allow_html=True)
        with fut_col2:
            st.markdown(f"""
                <div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;">
                    <div style="font-size: 12px; color: #FFD700; font-weight: 500;">💰 미래 {years}년 뒤 내 통장 최종 잔고 예측</div>
                    <div style="font-size: 24px; font-weight: 600; color: #FFD700; margin-top: 5px;">{int(future_value):,} 원</div>
                    <div style="font-size: 11px; color: #AAADB0; margin-top: 2px;">(현재 {int(final_value):,}원이 동일한 성장률로 복리 증식 시)</div>
                </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>✨ Gemini 종합 브리핑</h3>", unsafe_allow_html=True)
        habit_name = habit.split(" (")[0]
        
        if missed_money > 0:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #1A1B2F 0%, #16161D 100%); border: 1px solid #4A3E7D; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;">
                    <span style="color: #F28B82; font-weight: bold; font-size: 16px;">⚠️ [손실 진단 및 예측] 장바구니에 스며든 무서운 스노우볼 효과</span><br><br>
                    요청하신 데이터를 분석한 결과, 무심코 결제해 온 <b>'{habit_name}'</b> 비용이 <b>{target_asset}</b>의 폭발적인 주간 복리 성장세(주당 {weekly_growth_rate*100:+.3f}%)를 만나 잔인한 기회비용을 만들어냈습니다.<br><br>
                    이미 지나간 {years}년 동안 날린 돈만 <b>{int(missed_money/10000):,}만 원</b>에 달하며, 이 돈이 만약 동일한 주봉 상승 탄력을 유지하며 미래 {years}년 동안 '복리'로 더 굴러간다면... 당신의 통장에는 무려 <b>{int(future_value/10000):,}만 원</b>이라는 거금이 찍혀 있게 됩니다.<br><br>
                    강남 아파트 계약금이나 포르쉐 한 대 뽑을 수준의 미래 자산이 지금 스타벅스 컵과 마라탕 그릇, 지그재그 장바구니 속에서 살살 녹아내리고 있다는 뜻입니다. 미래의 자신에게 사죄하는 마음으로 오늘부터 즉시 충동 결제를 전면 중단할 것을 강력히 권고합니다.
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #16261E 0%, #16161D 100%); border: 1px solid #2B543A; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;">
                    <span style="color: #81C995; font-weight: bold; font-size: 16px;">😎 [반전 정산] 파괴적 역복리를 피한 인류 최강의 생존 전략</span><br><br>
                    축하합니다. 시뮬레이션 결과 귀하의 소비는 자산 폭락의 역복리 늪을 피해 간 '천재적인 리스크 관리'였음이 데이터로 입증되었습니다.<br><br>
                    만약 {years}년 전에 눈물 흘려가며 참아낸 돈을 <b>{target_asset}</b>에 적립했다면, 주당 {weekly_growth_rate*100:.3f}%씩 계좌가 살살 녹아내리는 고문을 당했을 것입니다. 만약 이 파괴적인 하락세가 미래 {years}년 뒤까지 그대로 복리로 이어진다면, 당신의 자산은 반토막을 넘어 <b>{int(future_value/10000):,}만 원</b> 수준으로 처참하게 소멸할 예정이었습니다.<br><br>
                    주식에 묶여서 증발할 뻔한 미래의 돈을 미리 끄집어내어 <b>'{habit_name}'</b>으로 알차게 도파민을 충전한 당신이 이 시대의 진정한 금융 승리자입니다. 앞으로도 상사가 킹받게 할 때는 주식 창을 켜는 대신 장바구니를 채우며 자산을 든든하게 방어하십시오.
                </div>
            """, unsafe_allow_html=True)
