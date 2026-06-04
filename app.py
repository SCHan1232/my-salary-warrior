import streamlit as st
import streamlit.components.v1 as components
import datetime

# 1. 미니멀한 노션 테마 설정
st.set_page_config(
    page_title="💰 [Notion] 2026 자산 최적화 프로젝트", 
    page_icon="📝",
    layout="centered" 
)

# 2. ⚡ 부장님 감지 패닉 버튼 (스페이스바 연타)
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
    if st.button("🔄 Notion 세션 새로고침"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# 🟢 AREA B: 노션으로 위장한 초정밀 팩폭 계산기
else:
    # 📊 [데이터 전면 리뉴얼] 국장 반도체 대장주 + 미장 마이크론, 샌디스크(WDC) 반영
    HISTORICAL_STOCK_DATA = {
        "삼성전자 (005930.KS)": {"current_price": 358250, "yearly_prices": [358250, 285000, 72500, 63100, 75500]},
        "SK하이닉스 (000660.KS)": {"current_price": 168000, "yearly_prices": [168000, 142000, 115000, 92000, 121000]},
        "한미반도체 (042700.KS)": {"current_price": 142500, "yearly_prices": [142500, 118000, 61000, 14500, 18500]}, # 국장 핫플 추가
        "엔비디아 (NVDA)": {"current_price": 125, "yearly_prices": [125, 85, 38, 16, 22]},
        "마이크론 (MU)": {"current_price": 132, "yearly_prices": [132, 110, 68, 55, 74]}, # 미장 추가
        "샌디스크/웨스턴디지털 (WDC)": {"current_price": 72, "yearly_prices": [72, 64, 42, 38, 52]} # 샌디스크 반영
    }

    # --- 노션 특유의 상단 UI 연출 ---
    st.markdown("""
        <div style="font-size: 75px; margin-bottom: 5px;">🦜</div>
        <h1 style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-weight: 700; color: #37352f; margin-top: 0; margin-bottom: 8px;">
            [개인] 소소한 행복 비용의 자산 전환 시뮬레이터
        </h1>
        <div style="color: rgba(55, 53, 47, 0.6); font-size: 14px; margin-bottom: 20px;">
            <span>📁 개인 아카이브</span> • <span>👤 schan1232</span> • <span>📅 최종 수정일: 2026년 6월 4일</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: #f1f1ef; padding: 16px; border-radius: 4px; display: flex; gap: 12px; margin-bottom: 25px;">
            <div style="font-size: 20px;">💡</div>
            <div style="color: #37352f; font-size: 14px; line-height: 1.5;">
                <b>안내 및 보안 지침</b><br>
                내가 탕진한 '시발비용'들을 주식에 적립식으로 넣었을 때의 실제 과거 주가 추이 기반 가치를 실시간으로 역산합니다.<br>
                <span style="color: #eb5757; font-weight: bold;">[🚨 월급루팡 전용 가드]</span> 뒤에 부장님이 접근 시 <b>[스페이스바 연속 2번]</b>을 누르면 즉시 사내 ERP 데이터셋으로 화면이 강제 전환됩니다.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚙️ 1. 데이터 추출 조건 설정")
    
    # 입력 양식
    with st.form("notion_form"):
        col1, col2 = st.columns(2)
        with col1:
            habit = st.selectbox(
                "🛍️ 나의 '흐린 눈' 지출 항목 선택", 
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
                "📈 연동 대상 주식/자산", 
                [
                    "삼성전자 (005930.KS)", 
                    "SK하이닉스 (000660.KS)", 
                    "한미반도체 (042700.KS)",
                    "엔비디아 (NVDA)", 
                    "마이크론 (MU)", 
                    "샌디스크/웨스턴디지털 (WDC)"
                ]
            )
            years = st.slider("⏳ 타임머신 추적 기간 (개년)", 1, 5, 3)
            
        submitted = st.form_submit_button("🔗 변경 데이터 반영하기 (Enter)")

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
            
        # 미장 판단 (.KS가 없으면 달러 기반 자산으로 인식)
        is_foreign = ".KS" not in target_asset
        exchange_rate = 1350 if is_foreign else 1
        final_value = total_shares * current_price * exchange_rate
        price_unit = "$" if is_foreign else "원"
        missed_money = final_value - total_seed

        st.write("")
        st.markdown("### 📊 2. 실시간 연산 결과 테이블")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.markdown(f"""
                <div style="border: 1px solid #e9e9e6; padding: 15px; border-radius: 4px; background: #fff;">
                    <div style="font-size: 12px; color: #7c7b77; font-weight: 500;">🪙 똥으로 사라진 매몰 원금</div>
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
            status_text = "🚨 피눈물 나는 기회비용" if missed_money > 0 else "🛡️ 강제 이득 본 금액"
            st.markdown(f"""
                <div style="border: 1px solid #e9e9e6; padding: 15px; border-radius: 4px; background: #fff;">
                    <div style="font-size: 12px; color: {card_color}; font-weight: 500;">{status_text}</div>
                    <div style="font-size: 22px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div>
                </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.markdown("### 💬 3. 껄무새의 데이터 분석 총평")
        habit_name = habit.split(" (")[0]
        
        if missed_money > 0:
            st.markdown(f"""
                <blockquote>
                    <b>🚨 [팩폭] 님 주둥이랑 장바구니가 문제임;;</b><br><br>
                    정신 차려 휴먼! 네이버 페이 비밀번호 6자리 뇌 빼고 누르면서 사 제낀 <b>'{habit_name}'</b> 비용...<br>
                    그 돈 안 쓰고 반도체 붐 탄 <b>{target_asset}</b>에 꼬박꼬박 박았으면 지금 계좌에 <b>{int(final_value/10000):,}만 원</b>이 꽂혀 있었어.<br><br>
                    순수하게 날린 초과 수익만 <b>{int(missed_money/10000):,}만 원</b>이야. 이 돈이면 올리브영 싹 쓸고 디올/샤넬 가방 하나 뽑았거나, 프랑스 파리행 비행기 비즈니스 끊었어 ㅠㅠ<br><br>
                    입으로는 맨날 '돈 없다, 퇴사하고 싶다' 달고 살면서 정작 시드머니는 장바구니에 털어 넣고 있었던 소름 돋는 현실... 내일부터 결제 앱 다 지워라 진짜.
                </blockquote>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <blockquote>
                    <b>😎 [대반전] 님 소비는 과학이었음! 오히려 좋아!</b><br><br>
                    와... 님 지출은 낭비가 아니라 완벽한 위기관리 능력이었음;;<br>
                    그때 돈 아끼겠답시고 청승 떨면서 <b>{target_asset}</b> 샀어 봐. 사이클 제대로 물려서 <b>-{int(abs(missed_money/10000)):,}만 원</b> 찐하게 물리치고 매일 밤 주식 차트 보면서 울었을 거임 ㅋㅋㅋ<br><br>
                    오히려 그 돈으로 <b>'{habit_name}'</b> 결제해서 도파민 채우고 스트레스 푼 게 자산 방어율 200%의 신의 한 수였다는 결론임. 대리님 짜증 날 땐 맛있는 거 먹고 옷 사는 게 합법적 재테크니까 앞으로도 당당하게 긁으셈!
                </blockquote>
            """, unsafe_allow_html=True)
