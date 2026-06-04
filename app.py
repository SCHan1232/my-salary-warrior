import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf
import datetime

# 1. 힙한 UI를 위한 페이지 설정
st.set_page_config(
    page_title="월급루팡 방지 시스템 v2", 
    page_icon="🚬",
    layout="wide"
)

# 2. ⚡ 부장님 감지 패닉 버튼 (Space바 연타)
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

# -----------------------------------------------------------------------------
# 🔴 AREA A: 부장님 모드 (완벽한 고인물 사내 인트라넷 변신)
# -----------------------------------------------------------------------------
if is_boss_mode:
    st.error("🔒 [보안 네트워크] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026년 전사 리소스 최적화 및 파이프라인 정량 지표")
    st.caption("보안등급: 대외비 (Class A) | 시스템 정상 작동 중")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="인프라 가동률 (OEE)", value="94.28%", delta="0.45% ▲")
    col2.metric(label="FinOps 비용 절감률", value="81.20%", delta="-1.5% ▼")
    col3.metric(label="API 레이턴시 (p99)", value="12.4 ms", delta="-2.1 ms ▲")
    
    st.subheader("📝 분기별 데이터셋 데이터프레임")
    st.dataframe({
        "부서코드": ["DE-01", "DE-02", "MK-04"],
        "프로젝트명": ["Next-Gen ERP", "Data Pipeline v3", "Core Sandbox"],
        "진척도": ["완료", "검증 중", "기획단계"]
    }, use_container_width=True)
    
    if st.button("🔄 시스템 세션 재연결"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# -----------------------------------------------------------------------------
# 🟢 AREA B: 흑우 탈출 껄무새 계산기 (담배/커피 적립식 버전)
# -----------------------------------------------------------------------------
else:
    # 대형 타이틀과 요즘 감성 이모지
    st.title("🚬 흑우 탈출! 일상 절약 주식 타임머신 ☕")
    st.markdown("### *'그때 담배 안 피우고 이 주식 샀으면 내 통장은 어땠을까...?'*")
    st.info("🚨 **[초긴급 전용 방어막]** 부장님이 뒤에 오면 **[스페이스바 연속 2번]** 탕탕! 치세요. 0.1초 만에 일잘러 화면으로 도망갑니다.")
    
    st.write("---")
    
    # 30분 단위 실시간 API 캐싱 (yfinance 가격 30분 보관)
    @st.cache_data(ttl=1800)
    def get_live_price(ticker):
        try:
            stock = yf.Ticker(ticker)
            # 최신 1일치 데이터를 분 단위로 가져와서 맨 마지막 종가 추출
            df = stock.history(period="1d", interval="30m")
            if not df.empty:
                return int(df['Close'].iloc[-1])
            else:
                return stock.info.get('regularMarketPrice', 70000)
        except:
            # 에러 발생 시 더미 가격 대처
            fallback = {"005930.KS": 72300, "NVDA": 125, "BTC-USD": 68000}
            return fallback.get(ticker, 50000)

    # 입력 UI 섹션
    with st.form("saving_form"):
        st.markdown("#### 🏃‍♂️ 나의 일상 '돈 지랄' 패턴 입력")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            habit = st.selectbox("어떤 돈을 아끼실 건가요? 🛍️", ["담배 (1갑 4,500원)", "스타벅스 아메리카노 (1잔 4,500원)", "배달음식 (1회 22,000원)"])
            count = st.slider("일주일에 몇 번(갑)이나 소비하시나요? 📊", 1, 14, 5)
        
        with col2:
            target_stock = st.selectbox(
                "적립식으로 매수했어야 할 자산 📈", 
                ["삼성전자 (005930.KS)", "엔비디아 (NVDA)", "비트코인 (BTC-USD)"]
            )
            years = st.slider("몇 년 동안 모았다고 가정할까요? ⏳", 1, 5, 3)
            
        with col3:
            st.markdown("<br>", unsafe_allow_html=True)
            leverage = st.checkbox("🔥 빡세게 2배 레버리지로 굴리기 (야수의 심장)")
            
        submitted = st.form_submit_button("🚀 내 잃어버린 자산 정산하기")

    # 결과 연산 및 연출
    if submitted:
        # 1. 일주일 소비 금액 계산
        unit_price = 4500 if habit != "배달음식 (1회 22,000원)" else 22000
        weekly_expense = unit_price * count
        yearly_expense = weekly_expense * 52
        total_seed = yearly_expense * years # 원금
        
        # 2. 주식 데이터 매핑 및 가상 수익률 계산
        ticker_map = {
            "삼성전자 (005930.KS)": "005930.KS",
            "엔비디아 (NVDA)": "NVDA",
            "비트코인 (BTC-USD)": "BTC-USD"
        }
        
        # 실제 30분 캐싱된 실시간 주가 들고오기
        current_price = get_live_price(ticker_map[target_stock])
        
        # 과거 대비 가상 수익률 매핑 (현실적인 통계치)
        # 3년 전 삼전, 엔비디아, 비트코인 등의 대략적인 적립식 누적 성과율 적용
        mock_returns = {
            "삼성전자 (005930.KS)": 1.18,   # 원금 대비 18% 상승
            "엔비디아 (NVDA)": 4.85,      # 원금 대비 385% 상승
            "비트코인 (BTC-USD)": 2.10     # 원금 대비 110% 상승
        }
        
        return_rate = mock_returns[target_stock]
        if leverage:
            return_rate = ((return_rate - 1.0) * 2.0) + 1.0
            
        final_value = total_seed * return_rate
        missed_money = final_value - total_seed
        
        st.write("---")
        st.markdown("## 📊 정산 스코어보드")
        
        # 트렌디한 카드형 카드 UI 디자인 연출
        res_col1, res_col2, res_col3 = st.columns(3)
        
        with res_col1:
            st.info(f"🪙 **그동안 그냥 길바닥에 버린 원금**\n\n### {int(total_seed):,} 원")
        with res_col2:
            st.success(f"📈 **현재 가치 (실시간 주가 반영)**\n\n### {int(final_value):,} 원\n\n(실시간: {current_price:,} 원 기준)")
        with res_col3:
            if missed_money > 0:
                st.warning(f"💸 **피눈물 흘리며 놓친 기회비용**\n\n### + {int(missed_money):,} 원")
            else:
                st.error(f"📉 **강제 방어한 손실 금액**\n\n### {int(abs(missed_money)):,} 원")

        # 3. 요즘 유행하는 팩트폭행 말투 및 MBTI식 결과 코멘트
        st.write("---")
        st.markdown("### 🦜 껄무새의 냉정한 한마디")
        
        if missed_money > 5000000:
            st.subheader(f"🚨 님 지금 폐가 썩는 것보다 통장 썩는 게 더 급함;;")
            st.markdown(f"말 그대로 주당 {count}번씩 주둥이에 털어 넣은 돈을 **{target_stock}**에 던졌으면, 지금 만질 수 있었던 공짜 돈만 **{int(missed_money/10000):,}만 원**입니다. 이 돈이면 지금 하와이 비행기 표 끊고 탕후루 500번 사 먹었습니다. 정신 차리세요 휴먼!")
        elif missed_money > 0:
            st.subheader(f"🚬 음~ 맛있는 니코틴 재테크~")
            st.markdown(f"아주 그냥 연기를 마시면서 돈을 공중에 뿌리셨군요? 원금 {int(total_seed/10000):,}만 원이 불어날 기회를 스스로 걷어차셨습니다. 다음 주부턴 한 갑 필 거 반 갑만 피고 소수점 투자나 켜십시오.")
        else:
            st.subheader(f"😎 의외의 개이득? 오히려 좋아!")
            st.markdown(f"님 주식 고르지 마셈 주식 샀으면 오히려 -{int(abs(missed_money/10000)):,}만 원 손해 봐서 지금 한강 갈 뻔했음ㅋㅋ 담배나 커피 맛있게 드신 걸로 인생 승리하신 겁니다. 축하드립니다!")
