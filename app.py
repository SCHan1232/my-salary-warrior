import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf
import datetime

# 1. 페이지 설정
st.set_page_config(
    page_title="월급루팡 방지 시스템 v4", 
    page_icon="🚬",
    layout="wide"
)

# 2. ⚡ 부장님 감지 패닉 버튼
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

# 🔴 AREA A: 부장님 모드
if is_boss_mode:
    st.error("🔒 [보안 네트워크] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026년 전사 리소스 최적화 및 파이프라인 정량 지표")
    if st.button("🔄 시스템 세션 재연결"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# 🟢 AREA B: 초정밀 주식 타임머신 (과거 월별 실제 주가 매수 반영)
else:
    st.title("🚬 흑우 탈출! 일상 절약 주식 타임머신 ☕")
    st.markdown("### *'과거 {N}년 전 오늘부터 담배 값을 아껴서 진짜 그 당시 주가로 샀다면?'*")
    st.info("🚨 **[초긴급 방어막]** 부장님이 오면 **[스페이스바 연속 2번]** 연타! 0.1초 만에 업무 보고서 화면으로 순간이동!")
    st.write("---")

    # 3. 📈 [핵심 엔진] 과거 N년 전부터 매월 적립식 매수를 시뮬레이션하는 함수
    @st.cache_data(ttl=3600)  # 서버 과부하 방지를 위해 1시간 캐싱
    def simulate_savings(ticker, years, monthly_budget):
        try:
            # 기준일 계산 (오늘: 2026년 6월 4일 -> 시작일: 2023년 6월 4일)
            end_date = datetime.date.today()
            start_date = end_date - datetime.timedelta(days=365 * years)
            
            # 야후 파이낸스에서 과거 {years}년 전부터 오늘까지의 '월별(1mo)' 주가 데이터 원본 가져오기
            stock = yf.Ticker(ticker)
            df = stock.history(start=start_date, end=end_date, interval="1mo")
            
            if df.empty:
                return 0, 0, 0, 0
                
            total_invested = 0  # 총 투자 원금
            total_shares = 0.0  # 누적 주식 수
            
            # 과거 월별 주가를 돌면서 매달 예산만큼 주식을 쪼개서 매수 (적립식)
            for index, row in df.iterrows():
                buy_price = row['Close']  # 그 당시 해당 월의 실제 종가 (Close)
                
                # 매달 아낀 돈으로 살 수 있는 주식 수 연산 (예: 90,000원 아껴서 45,000원짜리 삼전 2주 매수)
                shares_bought = monthly_budget / buy_price
                total_shares += shares_bought
                total_invested += monthly_budget
            
            # 마지막 거래일의 진짜 실시간 가격 (현재 주가)
            current_price = df['Close'].iloc[-1]
            
            # 현재 자산 가치 = 여태까지 모은 총 주식 수 * 현재 실시간 주가
            final_value = total_shares * current_price
            
            return int(total_invested), int(final_value), int(current_price), round(total_shares, 2)
        except Exception as e:
            st.error(f"데이터를 불러오는 중 오류 발생: {e}")
            return 0, 0, 0, 0

    # 입력 UI 섹션
    with st.form("saving_form"):
        st.markdown("#### 🏃‍♂️ 나의 일상 절약 패턴 입력")
        col1, col2 = st.columns(2)
        
        with col1:
            habit = st.selectbox("어떤 돈을 아끼실 건가요? 🛍️", ["담배 (1갑 4,500원)", "스타벅스 아메리카노 (1잔 4,500원)", "배달음식 (1회 22,000원)"])
            count = st.slider("일주일에 몇 번(갑)이나 소비하시나요? 📊", 1, 14, 5)
        
        with col2:
            target_asset = st.selectbox(
                "그때부터 적립식으로 모았어야 할 자산 📈", 
                ["삼성전자 (005930.KS)", "SK하이닉스 (000660.KS)", "엔비디아 (NVDA)", "비트코인 (BTC-USD)"]
            )
            years = st.slider("몇 년 동안 모았다고 가정할까요? ⏳", 1, 5, 3)
            
        submitted = st.form_submit_button("🚀 과거 실제 주가로 타임머신 가동!")

    if submitted:
        # 1. 한 달(4주 기준) 예산 환산
        unit_price = 4500 if habit != "배달음식 (1회 22,000원)" else 22000
        weekly_expense = unit_price * count
        monthly_budget = weekly_expense * 4  # 매달 주식 계좌에 이체했을 금액
        
        # 종목코드 파싱
        ticker = target_asset.split(" (")[1].replace(")", "")
        
        # 2. 백테스팅 시뮬레이션 엔진 가동
        with st.spinner("⏳ 과거 {years}년치 실제 월별 주가 데이터를 조회하여 정산 중..."):
            total_seed, final_value, current_price, total_shares = simulate_savings(ticker, years, monthly_budget)
        
        if total_seed > 0:
            missed_money = final_value - total_seed
            
            st.write("---")
            st.markdown(f"## 📊 {years}년 동안의 실제 적립식 정산 스코어보드")
            
            res_col1, res_col2, res_col3 = st.columns(3)
            with res_col1:
                st.info(f"🪙 **매달 모은 총 투자 원금**\n\n### {total_seed:,} 원\n\n(월 약 {int(monthly_budget):,}원씩 적립)")
            with res_col2:
                # 2026년 6월 4일 기준 실제 종가가 찍힙니다!
                st.success(f"📈 **오늘 기준 자산 가치**\n\n### {final_value:,} 원\n\n(현재 주가: {current_price:,} 원 / 총 {total_shares}주 보유)")
            with res_col3:
                if missed_money > 0:
                    st.warning(f"💸 **눈앞에서 놓친 실제 기회비용**\n\n### + {missed_money:,} 원")
                else:
                    st.error(f"📉 **강제 손실 방어 금액 (개이득)**\n\n### {abs(missed_money):,} 원")

            st.write("---")
            st.markdown("### 🦜 껄무새의 냉정한 팩트 폭행")
            if missed_money > 0:
                st.subheader(f"🚨 주둥이에 연기 털어 넣을 때가 아니었습니다.")
                st.markdown(f"실제 과거 차트를 대조해 본 결과, 당신이 3년 동안 담배 연기로 날려 보낸 돈을 **{target_asset}**에 넣었으면 오늘 기준으로 **{int(missed_money/10000):,}만 원**을 공짜로 벌 수 있었습니다. 이 돈이면 지금 하와이 비행기 표 끊고 남았습니다. 정신 차리세요 휴먼!")
            else:
                st.subheader(f"😎 흡연과 카페인이 살린 인생!")
                st.markdown(f"과거 주가 추이를 분석해 보니, 님은 주식 샀으면 상판때기 박살 나고 원금 까먹어서 지금쯤 피눈물 흘리고 있었을 겁니다ㅋㅋ 그냥 담배나 커피 맛있게 드신 게 최고의 헷지(Hedge) 재테크였습니다!")
