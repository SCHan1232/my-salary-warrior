import streamlit as st
import streamlit.components.v1 as components
import datetime
import random
import yfinance as yf

# 1. 껄무새 다크모드 기반 최적화 설정
st.set_page_config(
    page_title="✨ 껄무새 - 2030 필수 자산 케어 v34", 
    page_icon="🦜",
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

# 🛠️ 세션 데이터 구조 안전 보어선 가동
balance_games_pool = [
    {"question": "평생 배달 야식+스벅 끊고 엔비디아 풀매수 vs 고점 물린 삼전 원금 강제 회복", "A": 142, "B": 98},
    {"question": "매달 올영 구경 전면 금지 vs 테슬라 고점에 물려서 3년 강제 존버", "A": 85, "B": 132},
    {"question": "주말 골프/필드 호사 평생 포기 vs 내 계좌 전 종목 파란불 6개월 유지", "A": 110, "B": 74},
    {"question": "탕후루/마라탕 평생 금지 vs 애플 최고점에 상반기 보너스 올인", "A": 156, "B": 42},
    {"question": "지그재그/W컨셉 앱 영구 삭제 vs 비트코인 10% 하락 빔 직격타 맞기", "A": 93, "B": 121},
    {"question": "매달 네일/속눈썹 정기권 포기 vs 레버리지 상품에 퇴직금 몰빵", "A": 164, "B": 38},
    {"question": "퇴근 후 주말 위스키 전면 금지 vs 구글 주식 매수 후 비번 까먹기 (3년 보관)", "A": 119, "B": 105},
    {"question": "기념일 오마카세 평생 금지 vs 내 보유 종목 주총 의장으로 소환당하기", "A": 138, "B": 51},
    {"question": "체형교정 필라테스 영구 금지 vs 마이크론 최고점 추격 매수", "A": 77, "B": 143},
    {"question": "유럽 축구 유니폼 수집 금지 vs 엔비디아 숏(인버스) 상품에 저축 넣기", "A": 125, "B": 62}
]

if "vote_data" in st.session_state:
    if isinstance(st.session_state["vote_data"], dict):
        st.session_state["vote_data"] = balance_games_pool
else:
    st.session_state["vote_data"] = balance_games_pool

if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = [
        {"role": "user", "name": "익명루팡_724", "text": "마라탕이랑 스벅 끊었으면 이미 해외여행 비즈니스 탔음.. 😭"}, 
        {"role": "user", "name": "서학개미_119", "text": "차트 탭 열리니까 내가 날려먹은 상승 랠리가 한눈에 보여서 더 피눈물 남"},
        {"role": "user", "name": "껄껄새_002", "text": "테슬라 3년 전에 샀어야 했는데 껄껄껄... 지금이라도 타?"}
    ]
if "suggested_stocks" not in st.session_state:
    st.session_state["suggested_stocks"] = [
        {"time": "16:21", "text": "애플(AAPL)이랑 마이크로소프트(MSFT)도 시뮬레이션 할 수 있게 추가해주세요!"},
        {"time": "16:30", "text": "비트코인(BTC-USD) 기회비용 연동도 시급합니다 개발자님!"}
    ]
if "current_game_idx" not in st.session_state:
    st.session_state["current_game_idx"] = 0
if "current_audit" not in st.session_state:
    st.session_state["current_audit"] = None

# 🔴 AREA A: 부장님 방어막
if is_boss_mode:
    st.error("🔒 [보안] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026_전사_리소스_최적화_KPI_Data")
    st.dataframe({"Index": [1, 2], "Task": ["Next-Gen ERP 구축", "Data Pipeline v3"], "Progress": ["94.2%", "81.2%"]}, use_container_width=True)
    if st.button("🔄 시스템 세션 새로고침"): st.query_params["boss_mode"] = "false"; st.rerun()

# 🟢 AREA B: 껄무새 놀이터
else:
    # 📊 지출 데이터베이스
    HABIT_PRICE_DICT = {
        "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": 18000,
        "스타벅스 바닐라라떼+디저트 (1회 11,000원)": 11000, 
        "올리브영 세일 '구경만' 가기 (1회 45,000원)": 45000,
        "불금 배달 떡볶이+치킨 세트 (1회 32,000원)": 32000,
        "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": 65000,
        "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": 55000,
        "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": 85000, 
        "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": 50000, 
        "주말 골프 연습장/필드 호사 (1회 120,000원)": 120000,
        "기념일 에피타이저 오마카세 (1회 150,000원)": 150000, 
        "체형 교정 명목 필라테스 (1회 60,000원)": 60000,
        "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": 140000
    }

    # 야후 파이낸스 Ticker 매핑
    STOCK_TICKER_MAP = {
        "SK하이닉스 (000660.KS)": "000660.KS",
        "삼성전자 (005930.KS)": "005930.KS",
        "한미반도체 (042700.KS)": "042700.KS",
        "엔비디아 (NVDA)": "NVDA",
        "테슬라 (TSLA)": "TSLA",
        "구글 (GOOGL)": "GOOGL",
        "마이크론 (MU)": "MU"
    }

    # 헤더 텍스트
    st.markdown("""
        <div style="margin-bottom: 2px;">
            <span style="font-size: 38px; font-weight: 800; background: linear-gradient(45deg, #4285F4, #9B51E0, #E91E63); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px;">
                🦜 껄무새
            </span>
        </div>
    """, unsafe_allow_html=True)

    # 🛠
