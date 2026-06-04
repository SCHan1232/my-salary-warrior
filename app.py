import streamlit as st
import streamlit.components.v1 as components
import datetime

# 1. 제미나이 검색 및 다크모드 환경에 최적화된 설정
st.set_page_config(
    page_title="✨ Gemini - 자산 최적화 시뮬레이션", 
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
            무엇을 도와드릴까요? 일상 소비 효율성을 분석합니다.
        </h2>
    """, unsafe_allow_html=True)

    # 제미나이 스타일의 깔끔한 인풋 카드 연출을 위한 CSS 셋업
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
            
        submitted = st.form_submit_button("✨ 제미나이 분석 엔진 가동 (Enter)")

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
        
        total_shares = 0.0
        for i in range(years):
            past_price = prices_history[years - i]
            total_shares += yearly_budget / past_price
            
        is_foreign = ".KS" not in target_asset
        exchange_rate = 1350 if is_foreign else 1
        final_value = total_shares * current_price * exchange_rate
        price_unit = "$" if is_foreign else "원"
        missed_money = final_value - total_seed

        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>📊 분석 결과 데이터</h3>", unsafe_allow_html=True)
        
        # 다크모드 전용 고대비 결과 카드 (글자색 무조건 흰색/밝은 가독성 컬러 배치)
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
                    <div style="font-size: 12px; color: #81C995; font-weight: 500;">📈 적립 시 가치 (현재가 기준)</div>
                    <div style="font-size: 22px; font-weight: 600; color: #81C995; margin-top: 5px;">{int(final_value):,} 원</div>
                    <div style="font-size: 11px; color: #AAADB0; margin-top: 2px;">(현재가: {current_price:,}{price_unit} / {round(total_shares,2)}주)</div>
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

        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>✨ Gemini 종합 브리핑</h3>", unsafe_allow_html=True)
        habit_name = habit.split(" (")[0]
        
        # 제미나이 인공지능 답변 스타일의 화려하고 선명한 다크 박스
        if missed_money > 0:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #1A1B2F 0%, #16161D 100%); border: 1px solid #4A3E7D; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;">
                    <span style="color: #F28B82; font-weight: bold; font-size: 16px;">⚠️ [손실 진단] 장바구니와 소비 주둥이 통제 불능 상태</span><br><br>
                    요청하신 데이터를 분석한 결과, 네이버페이나 카카오페이로 생각 없이 결제해 온 <b>'{habit_name}'</b> 비용의 누적 타격이 매우 심각합니다.<br><br>
                    그 돈을 아껴 반도체 사이클 대장주인 <b>{target_asset}</b>에 적립식으로 투자했다면 금일 기준 총 자산은 <b>{int(final_value/10000):,}만 원</b>에 달했을 것입니다.<br><br>
                    순수하게 날려 보낸 초과 수익만 <b>{int(missed_money/10000):,}만 원</b>입니다. 이 금액이면 올리브영 매장을 통째로 털었거나 디올·샤넬백 스페셜 에디션을 뽑고도 프랑스 파리행 비행기 비즈니스석을 타고 유유히 떠났을 수준입니다. 입으로는 매일 '돈 없다, 회사 관두고 싶다'를 외치면서 손가락은 충동결제를 향하고 있었던 모순을 직시하십시오. 당장 쇼핑 앱 결제 카드를 삭제할 것을 권고합니다.
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #16261E 0%, #16161D 100%); border: 1px solid #2B543A; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;">
                    <span style="color: #81C995; font-weight: bold; font-size: 16px;">😎 [반전 정산] 영리한 도파민 결제와 리스크 헷지 완수</span><br><br>
                    축하합니다. 시뮬레이션 결과 귀하의 지출은 자산 파괴 행위가 아닌 '완벽한 위기관리 전략'이었음이 입증되었습니다.<br><br>
                    만약 해당 기간 절약을 한답시고 스트레스를 참아가며 <b>{target_asset}</b> 자산을 적립식으로 모았다면, 처참한 사이클 고점에 정통으로 물려 오늘 기준 무려 <b>-{int(abs(missed_money/10000)):,}만 원</b>의 원금 손실을 직면하고 매일 차트를 보며 피눈물을 흘렸을 것입니다.<br><br>
                    결과적으로 주식 대신 <b>'{habit_name}'</b>을 결제하여 회사 스트레스를 해소하고 도파민을 충전한 것이 자산 방어율 200%의 최고 재테크 헷지(Hedge)였습니다. 상사나 대리님이 혈압을 올릴 땐 마라탕을 때리고 옷을 지르는 행위가 금융 치료이자 합법적 자산 방어 기전이므로 앞으로도 당당하게 소비 흐름을 유지하십시오.
                </div>
            """, unsafe_allow_html=True)
