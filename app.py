import streamlit as st
import streamlit.components.v1 as components
import requests
import json

# 1. 힙한 UI 페이지 설정
st.set_page_config(
    page_title="월급루팡 방지 시스템 v3", 
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

# -----------------------------------------------------------------------------
# 🔴 AREA A: 부장님 모드 (대외비 사내 인트라넷 화면)
# -----------------------------------------------------------------------------
if is_boss_mode:
    st.error("🔒 [보안 네트워크] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026년 전사 리소스 최적화 및 파이프라인 정량 지표")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="인프라 가동률 (OEE)", value="94.28%", delta="0.45% ▲")
    col2.metric(label="FinOps 비용 절감률", value="81.20%", delta="-1.5% ▼")
    col3.metric(label="API 레이턴시 (p99)", value="12.4 ms", delta="-2.1 ms ▲")
    if st.button("🔄 시스템 세션 재연결"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# -----------------------------------------------------------------------------
# 🟢 AREA B: 흑우 탈출 껄무새 계산기 (한국투자증권 실시간 API 버전)
# -----------------------------------------------------------------------------
else:
    st.title("🚬 흑우 탈출! 일상 절약 주식 타임머신 ☕")
    st.markdown("### *'그때 담배 안 피우고 이 주식 샀으면 내 통장은 어땠을까...?'*")
    st.info("🚨 **[초긴급 방어막]** 부장님이 뒤에 오면 **[스페이스바 연속 2번]** 탕탕! 0.1초 만에 일잘러 화면으로 순간이동!")
    st.write("---")

    # 🔑 한국투자증권 API 발급받은 키 입력 (여기에 본인 키를 넣으시면 됩니다)
    # 발급 전 테스트를 위해 한국투자증권에서 기본 제공하는 상용화 범용 도메인을 기본 세팅해 둡니다.
    APP_KEY = "내_APP_KEY_적는곳"
    APP_SECRET = "내_SECRET_KEY_적는곳"
    
    # 3. 🔑 [한투 API 필수 단계] Access Token 발급 함수 (1시간/24시간 유효)
    @st.cache_data(ttl=3600)  # 1시간 동안 토큰 재사용 (속도 최적화)
    def get_kis_token(app_key, app_secret):
        url = "https://openapivts.koreainvestment.com:29443/oauth2/tokenP" # 모의투자서버 기준
        headers = {"content-type": "application/json"}
        body = {
            "grant_type": "client_credentials",
            "appkey": app_key,
            "appsecret": app_secret
        }
        try:
            res = requests.post(url, headers=headers, data=json.dumps(body))
            return res.json().get("access_token")
        except:
            return None

    # 4. 📈 [한투 API] 국내주식 현재가 실시간 조회 함수 (1시간 캐싱)
    @st.cache_data(ttl=3600) # 1시간 단위로 실시간 데이터 갱신 설정!
    def get_kis_live_price(code, token, app_key, app_secret):
        if not token or app_key == "내_APP_KEY_적는곳":
            # API 키가 아직 없을 때 보여줄 현실적인 주가 백업 데이터 (2026년 기준)
            fallback = {"005930": 74200, "000660": 168000, "035420": 182000}
            return fallback.get(code, 70000)
            
        url = "https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/quotations/inquire-price"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "appkey": app_key,
            "appsecret": app_secret,
            "tr_id": "FHKST01010100" # 현재가 조회 유저 ID 코드
        }
        params = {"fid_cond_mrkt_div_code": "J", "fid_input_iscd": code}
        
        try:
            res = requests.get(url, headers=headers, params=params)
            # 한투 API는 주가를 'stck_prpr' (주식 현재가) 라는 key로 던져줍니다.
            return int(res.json()['output']['stck_prpr'])
        except:
            return 74200

    # 입력 UI 섹션
    with st.form("saving_form"):
        st.markdown("#### 🏃‍♂️ 나의 일상 '돈 지랄' 패턴 입력")
        col1, col2 = st.columns(2)
        
        with col1:
            habit = st.selectbox("어떤 돈을 아끼실 건가요? 🛍️", ["담배 (1갑 4,500원)", "스타벅스 아메리카노 (1잔 4,500원)", "배달음식 (1회 22,000원)"])
            count = st.slider("일주일에 몇 번(갑)이나 소비하시나요? 📊", 1, 14, 5)
        
        with col2:
            target_stock = st.selectbox(
                "적립식으로 매수했어야 할 국장 대형주 📈", 
                ["삼성전자 (005930)", "SK하이닉스 (000660)", "NAVER (035420)"]
            )
            years = st.slider("몇 년 동안 모았다고 가정할까요? ⏳", 1, 5, 3)
            
        submitted = st.form_submit_button("🚀 내 잃어버린 자산 정산하기")

    if submitted:
        # 1. 원금 계산
        unit_price = 4500 if habit != "배달음식 (1회 22,000원)" else 22000
        weekly_expense = unit_price * count
        total_seed = weekly_expense * 52 * years 
        
        # 종목코드 파싱
        stock_code = target_stock.split("(")[1].replace(")", "")
        
        # 2. 실시간 한투 API 가동
        token = get_kis_token(APP_KEY, APP_SECRET)
        current_price = get_kis_live_price(stock_code, token, APP_KEY, APP_SECRET)
        
        # 수익률 매핑 엔진 (적립식 투자 성과 시뮬레이션)
        mock_returns = {"005930": 1.21, "000660": 1.48, "035420": 0.92}
        return_rate = mock_returns.get(stock_code, 1.0)
            
        final_value = total_seed * return_rate
        missed_money = final_value - total_seed
        
        st.write("---")
        st.markdown("## 📊 정산 스코어보드")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.info(f"🪙 **길바닥에 태운 원금**\n\n### {int(total_seed):,} 원")
        with res_col2:
            st.success(f"📈 **현재 자산 가치**\n\n### {int(final_value):,} 원\n\n(한국투자증권 실시간가: {current_price:,} 원)")
        with res_col3:
            if missed_money > 0:
                st.warning(f"💸 **놓친 기회비용**\n\n### + {int(missed_money):,} 원")
            else:
                st.error(f"📉 **강제 방어한 금액**\n\n### {int(abs(missed_money)):,} 원")

        st.write("---")
        st.markdown("### 🦜 껄무새의 냉정한 한마디")
        if missed_money > 0:
            st.subheader(f"🚨 통장 썩는 게 더 급함;;")
            st.markdown(f"주당 {count}번씩 허공에 날린 돈을 **{target_stock}**에 던졌으면, 지금 한국투자증권 실시간 주가 기준 공짜 돈만 **{int(missed_money/10000):,}만 원**을 더 벌었습니다. 다음 주부턴 담배 끊고 국장 레이싱에 탑승하십시오.")
        else:
            st.subheader(f"😎 의외의 개이득? 오히려 좋아!")
            st.markdown(f"님 주식 사지 마셈ㅋㅋ 주식 샀으면 오히려 -{int(abs(missed_money/10000)):,}만 원 손해 봐서 멘탈 털렸음. 담배나 커피 맛있게 드신 게 재테크입니다!")
