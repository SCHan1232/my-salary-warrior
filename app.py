import streamlit as st
import streamlit.components.v1 as components
import datetime
import random

# 1. 껄무새 다크모드 기반 최적화 설정
st.set_page_config(
    page_title="✨ 껄무새 - 2030 필수 자산 케어 v28", 
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

# 세션 데이터 유지 설정
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = [
        {"role": "user", "name": "익명루팡_724", "text": "마라탕이랑 스벅 끊었으면 이미 해외여행 비즈니스 탔음.. 😭"}, 
        {"role": "user", "name": "서학개미_119", "text": "구글 모으는 게 인생 최고 개이득인듯 다들 미장 가라"},
        {"role": "user", "name": "껄껄새_002", "text": "테슬라 3년 전에 샀어야 했는데 껄껄껄... 지금이라도 타?"}
    ]
if "vote_data" not in st.session_state:
    st.session_state["vote_data"] = {"A": 245, "B": 198}
if "current_audit" not in st.session_state:
    st.session_state["current_audit"] = None

# 무한 밸런스 게임 10종 리스트 & 투표 데이터 상태 정의
if "balance_games" not in st.session_state:
    st.session_state["balance_games"] = [
        {"id": 0, "q": "평생 동안 둘 중 딱 하나만 선택하여 살아갈 수 있다면?", "opt_a": "평생 배달 엽떡+치킨+스벅 끊고 그 돈 전액 엔비디아 무지성 적립 매수", "opt_b": "평생 패션/올영 전면 금지당하는 대신 고점 물려 -70% 토막 난 삼전 원금 강제 복구", "votes_a": 142, "votes_b": 98},
        {"id": 1, "q": "만약 한 달 동안 둘 중 하나만 반값 할인 혜택을 받는다면?", "opt_a": "한 달간 내 모든 배달비, 마라탕, 위스키 값 전면 50% 반값 바겐세일", "opt_b": "한미반도체 오늘 하루 동안 내 평단가 기준으로 50% 특별 추가 할인 분할 매수", "votes_a": 85, "votes_b": 112},
        {"id": 2, "q": "내 스마트폰에서 평생 하나의 영구 차단 패널티를 부여받아야 한다면?", "opt_a": "지그재그, W컨셉 등 모든 의류 모바일 결제 앱 계정 영구 삭제 및 가입 금지", "opt_b": "테슬라(TSLA) 주식 평생 매수 금지당하고 마이너스 계좌 강제 동결", "votes_a": 94, "votes_b": 76},
        {"id": 3, "q": "내 건강 자산과 금융 자산의 극단적인 딜이 들어왔다면?", "opt_a": "평생 속눈썹/네일 파츠 펌 금지당하는 대신 SK하이닉스 평단 5만원대 계좌 획득", "opt_b": "손톱 숨 쉴 구멍 없이 풀 파츠 올리고 한눈판 사이에 마이크론 고점 풀영끌 물리기", "votes_a": 121, "votes_b": 45},
        {"id": 4, "q": "퇴근 후 즐거움 중 단 하나만 평생 압수당해야 한다면?", "opt_a": "퇴근 후 주말 싱글몰트 피트 위스키 혼술하는 즐거움 영구 박탈당하기", "opt_b": "구글(GOOGL) 소수점 자동 적립식 이체 계정 영구 폐쇄당하고 강제 예금행", "votes_a": 73, "votes_b": 139},
        {"id": 5, "q": "주말 액티비티 중 사치 지수를 하나만 조정해야 한다면?", "opt_a": "주말 명품 골프 필드 나가는 호사 영구 정지당하고 방구석 스크린 골프만 치기", "opt_b": "샌디스크/WDC에 3년 동안 모은 돈 영끌했다가 주가 반토막 난 채로 손절 금지", "votes_a": 110, "votes_b": 88},
        {"id": 6, "q": "인스타용 미식 라이프스타일 중 하나만 영구 포기한다면?", "opt_a": "기념일 에피타이저 오마카세 및 파인다이닝 예약권 평생 영구 박탈당하기", "opt_b": "엔비디아 주식 소수점 다 팔고 국장 동전주 연속 5연상 가기 기도 메타 탑승", "votes_a": 102, "votes_b": 95},
        {"id": 7, "q": "내 몸의 기계적 척추와 자산의 척추 중 하나만 정렬한다면?", "opt_a": "체형 교정 명목 고액 필라테스 영구 정지당하고 평생 국민체조로 척추 펴기", "opt_b": "내가 적립식으로 모은 삼성전기 MLCC가 우주선 부품으로 선정되어 300% 떡상", "votes_a": 64, "votes_b": 152},
        {"id": 8, "q": "취미 덕질 영역 중 평생 동안 하나만 박탈당한다면?", "opt_a": "덕질 게임 가챠, 가상 스킨, 플랫폼 아바타 현질 권리 영구 박탈당하기", "opt_b": "엔비디아 젠슨 황과 1:1 프라이빗 디너 가지며 다음 세대 GPU 출시 꿀팁 듣기", "votes_a": 53, "votes_b": 164},
        {"id": 9, "q": "해외 축구 덕질과 자산 포트폴리오 중 하나만 고른다면?", "opt_a": "평생 내 최애 축구단 감성 레플리카 유니폼 수집 및 직관 기회 영구 정지", "opt_b": "구단 레플리카 살 돈으로 그 구단 주식 야무지게 적립해서 명예 소액 주주되기", "votes_a": 89, "votes_b": 118}
    ]
if "current_game_index" not in st.session_state:
    st.session_state["current_game_index"] = 0
if "last_voted_result" not in st.session_state:
    st.session_state["last_voted_result"] = None

# 🔴 AREA A: 부장님 방어막
if is_boss_mode:
    st.error("🔒 [보안] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026_전사_리소스_최적화_KPI_Data")
    st.dataframe({"Index": [1, 2], "Task": ["Next-Gen ERP 구축", "Data Pipeline v3"], "Progress": ["94.2%", "81.2%"]}, use_container_width=True)
    if st.button("🔄 시스템 세션 새로고침"): st.query_params["boss_mode"] = "false"; st.rerun()

# 🟢 AREA B: 껄무새 놀이터
else:
    # 📊 데이터베이스
    HABIT_PRICE_DICT = {
        "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": 18000,
        "스타벅스 바닐라라떼+디저트 (1회 11,000원)": 11000, 
        "올리브영 세일 '구경만' 가기 (1회 45,000원)": 45000,
        "불금 배달 엽떡+치킨 세트 (1회 32,000원)": 32000,
        "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": 65000,
        "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": 55000,
        "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": 85000, 
        "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": 50000, 
        "주말 골프 연습장/필드 호사 (1회 120,000원)": 120000,
        "기념일 에피타이저 오마카세 (1회 150,000원)": 150000, 
        "체형 교정 명목 필라테스 (1회 60,000원)": 60000,
        "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": 140000
    }

    # 🛠️ [기획 핵심 이식 1] 지출 항목별 "껄" 타이틀 매핑 데이터베이스
    GGUL_TITLE_MAP = {
        "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": "수명 연장하고 해외여행 비즈니스 탔을 '껄'",
        "스타벅스 바닐라라떼+디저트 (1회 11,000원)": "커피 머신 사고 홈카페 사장 됐을 '껄'",
        "올리브영 세일 '구경만' 가기 (1회 45,000원)": "명품 화장품 풀세트로 선물 돌렸을 '껄'",
        "불금 배달 엽떡+치킨 세트 (1회 32,000원)": "1년 PT 끊고 바디프로필 찍었을 '껄'",
        "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": "대장급 패딩 사서 어깨 펴고 다녔을 '껄'",
        "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": "손톱 숨 쉬게 냅두고 주주총회 갔을 '껄'",
        "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": "간 건강 사수하고 호텔 전신 스파 받았을 '껄'", 
        "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": "데이터 쪼가리 대신 실제 땅 한 평 샀을 '껄'", 
        "주말 골프 연습장/필드 호사 (1회 120,000원)": "필드 슬라이스 대신 내 자산 홀인원 했을 '껄'",
        "기념일 에피타이저 오마카세 (1회 150,000원)": "프랑스 파리에서 진짜 에스카르고 썰었을 '껄'", 
        "체형 교정 명목 필라테스 (1회 60,000원)": "기구 비명 대신 수익률로 척추 폈을 '껄'",
        "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": "유니폼 장식 대신 그 구단 주식 샀을 '껄'"
    }

    HISTORICAL_STOCK_DATA = {
        "삼성전자 (005930.KS)": {"current_price": 358250, "yearly_prices": [358250, 285000, 72500, 71500, 66500]},
        "SK하이닉스 (000660.KS)": {"current_price": 168000, "yearly_prices": [168000, 142000, 115000, 110300, 105000]},
        "한미반도체 (042700.KS)": {"current_price": 142500, "yearly_prices": [142500, 118000, 61000, 29800, 13200]},
        "삼성전기 (009150.KS)": {"current_price": 156500, "yearly_prices": [156500, 148000, 138000, 145200, 149000]},
        "엔비디아 (NVDA)": {"current_price": 125, "yearly_prices": [125, 85, 48, 39, 18]}, 
        "테슬라 (TSLA)": {"current_price": 178, "yearly_prices": [178, 210, 175, 214, 235]}, 
        "구글 (GOOGL)": {"current_price": 174, "yearly_prices": [174, 150, 112, 124, 115]}, 
        "마이크론 (MU)": {"current_price": 132, "yearly_prices": [132, 110, 68, 67, 71]}, 
        "샌디스크/웨스턴디지털 (WDC)": {"current_price": 72, "yearly_prices": [72, 64, 42, 39, 52]} 
    }

    # 좌우 분할 레이아웃 배치
    main_layout, chat_layout = st.columns([2.5, 0.8], gap="medium")

    # ==================== [LEFT SIDE] 메인 기능 영역 ====================
    with main_layout:
        tab1, tab2, tab3, tab4 = st.tabs(["📊 자산 타임머신", "🔮 껄무새 사주도사", "⚔️ 주주총회 밸런스", "🧠 포모 차단기"])

        # TAB 1: 타임머신
        with tab1:
            st.markdown("<p style='color: #AAADB0; font-size: 14px; margin-bottom: 20px;'>내 탕진 비용의 스노우볼을 역산하고 미래 퀀텀점프 자산을 예측합니다.</p>", unsafe_allow_html=True)
            
            dropdown_options = ["✍️ 내 쓸모없는 지출 직접 입력하기"] + list(HABIT_PRICE_DICT.keys())
            selected_option = st.selectbox("🛍️ 매달 '흐린 눈'으로 지출 중인 항목", dropdown_options)
            
            custom_habit_name = ""
            custom_habit_price = 0
            if selected_option == "✍️ 내 쓸모없는 지출 직접 입력하기":
                c_col1, c_col2 = st.columns(2)
                with c_col1: custom_habit_name = st.text_input("💸 지출 항목 이름 입력", placeholder="예: 아이돌 포카 시크릿 깡")
                with c_col2: custom_habit_price = st.number_input("🪙 1회당 지출 금액 (원)", min_value=0, value=20000, step=1000)

            with st.form("gemini_form"):
                col1, col2 = st.columns(2)
                with col1: count = st.slider("📊 주간 평균 소비 빈도", 1, 14, 3)
                with col2:
                    target_asset = st.selectbox("📈 연동할 목적 자산", list(HISTORICAL_STOCK_DATA.keys()))
                    years = st.slider("⏳ 타임머신 추적 기간 (년)", 1, 5, 3)
                submitted = st.form_submit_button("✨ 껄무새 엔진 가동 (Enter)")

            if submitted:
                # ✍️ 직접 입력 처리 시 동적 타이틀 생성
                if selected_option == "✍️ 내 쓸모없는 지출 직접 입력하기":
                    habit_clean_name = custom_habit_name if custom_habit_name else "익명 탕진 지출"
                    unit_price = custom_habit_price
                    ggul_card_title = f"'{habit_clean_name}' 안 사고 진작 조기 퇴사했을 '껄'"
                else:
                    habit_clean_name = selected_option.split(" (")[0]
                    unit_price = HABIT_PRICE_DICT[selected_option]
                    ggul_card_title = GGUL_TITLE_MAP.get(selected_option, f"'{habit_clean_name}' 안 사고 다른 거 했을 '껄'")

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
                missed_money = final_value - total_seed

                max_idx = min(years, len(prices_history) - 1)
                then_price = prices_history[max_idx]
                total_asset_growth = ((current_price - then_price) / then_price) * 100
                
                growth_multiplier = current_price / then_price
                future_value = final_value * growth_multiplier
                asset_clean_name = target_asset.split(" (")[0]
                
                # 금액대별 동적 등급 연산
                if missed_money > 0:
                    if selected_option == "✍️ 내 쓸모없는 지출 직접 입력하기":
                        if total_seed <= 3000000:
                            card_info = {"title": "🌱 응애 급 초보 탕진러", "desc": f"푼돈 긁으면서 자산에 타격 없을 거라고 흐린 눈 자위하는 단계입니다.\\n하지만 귀하가 생각 없이 던진 '{habit_clean_name}' 비용은 복리 마귀의 영양분이 되어 실시간으로 계좌의 뼈대를 갉아먹는 중입니다.\\n하루빨리 손가락을 묶지 않으면 미래 평단가는 영원히 구렁텅이에 처박힙니다."}
                        elif total_seed <= 15000000:
                            card_info = {"title": "💸 통장 믹서기 분쇄 대리", "desc": f"남들이 대가리 깨져가며 적립식 우량주 시드 모을 때 혼자 장바구니 풀소유로 파티를 벌이셨군요.\\n'{habit_clean_name}'에 쏟아부은 천만 원대의 거금은 주식 시장의 세력들이 아주 달콤하게 노 나눠 가졌습니다.\\n허접한 소비 도파민과 미래 잔고 {int(future_value/10000):,}만 원을 맞교환한 이 시대의 진정한 기부천사십니다."}
                        elif total_seed <= 50000000:
                            card_info = {"title": "🚨 장바구니 풀소유 광기 야수", "desc": f"이쯤 되면 지갑이 아니라 지능의 문제를 의심해봐야 합니다. 웬만한 국산 중형차 풀옵션을 뽑고도 남을 돈을 오직 '{habit_clean_name}'에 하수구 물 버리듯 태우셨네요.\\n미래에 {asset_clean_name}의 퀀텀점프 상승 기류를 타고 은퇴할 기회를 완벽하게 차단하셨습니다.\\n계속 그렇게 흐린 눈으로 결제 앱 비밀번호나 누르며 자위하십시오."}
                        else:
                            card_info = {"title": "👑 자산 분쇄계의 월드클래스 GOAT", "desc": f"경배하라, 걸어 다니는 마이너스 인간 지표이자 자산 파괴 of 신이 강림하셨습니다.\\n억 단위의 소중한 인생 시드를 오직 '{habit_clean_name}'이라는 기상천외한 명목으로 공중에 산산조각 분해해 버리셨군요.\\n덕분에 {asset_clean_name}의 진짜 주주들은 발 뻗고 잡니다. 님 덕분에 자본주의 시장이 돌아갑니다. 눈물 닦고 출근이나 하세요."}
                    else:
                        custom_cards = {
                            "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": {"title": "🩸 혈당 폭발 마라탕 중독자", "desc": "마라 국물과 설탕 코팅에 영혼을 저당 잡아 혈당을 올리는 사이, 본인의 시드머니는 주식 시장에서 완전히 녹아내리게 방치한 위대한 푸드 파이터.\\n입안의 사치와 뱃살을 얻은 대가로 통장 잔고의 미래 척추는 완벽하게 아작이 나 버렸습니다.\\n미래에 포르쉐 대신 마라탕 그릇이나 핥고 있을 귀하의 흐린 눈을 응원합니다."},
                            "스타벅스 바닐라라떼+디저트 (1회 11,000원)": {"title": "☕ 사이렌 오더 명예 기부 의장", "desc": "매달 스타벅스 별 사냥과 고카페인 시럽 액상과당에 취해 살며 남의 나라 스타벅스 코리아 시총 방어에 본인 시드를 장렬히 갈아 넣으신 호구.\\n정작 본인 계좌는 한파 주의보가 내렸는데 매일 아침 당당하게 닉네임 불리며 커피 픽업하는 모습이 참 눈물겹습니다.\\n그 컵홀더 모아두면 미래에 강남 아파트 전세라도 준답니까?"},
                            "올리브영 세일 '구경만' 가기 (1회 45,000원)": {"title": "💄 올영 시총 수호대 대장", "desc": "세일 문자만 오면 눈이 뒤집혀서 '구경만 해야지' 하고 기어들어가 장바구니를 틴트와 팩으로 꾸역꾸역 채워 나오는 뇌 빼놓은 영애.\\n피부는 일시적으로 매끈해졌을지 몰라도, 귀하의 투자 포트폴리오는 전라로 굶주려 비명을 지르고 있습니다.\\n미래에 그 화장품 다 바르고 한강 뷰 보며 울고 계실 모습이 참으로 선합니다."},
                            "불금 배달 엽떡+치킨 세트 (1회 32,000원)": {"title": "🐔 배달 앱 다이아몬드 등급 흑우", "desc": "금요일 퇴근 후 스트레스 핑계 대며 캡사이신과 닭 튀김 옷으로 위장을 혹사하는 사이, 통장에 억 단위 자산이 쌓일 기회는 야무지게 소화되어 사라졌습니다.\\n라이더 영웅들에게 배달 팁 쾌척하며 자선사업 하시는 동안 귀하의 노후 자금은 완벽하게 멸망의 길로 직진했습니다.\\n남은 치킨 무 국물이나 마시며 껄껄 대십시오."},
                            "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": {"title": "👗 방구석 드레스룸 독재자", "desc": "침대에 누워 흐린 눈으로 옷 구경하다 네이버페이 지문 인식 광속으로 태우며 택배 상자 뜯는 도파민에 중독된 중꺾소 패셔니스타.\\n방구석 옷장은 미어터지지만 주식 계좌는 알거지 상태로 처참하게 방치되어 인공호흡기를 달고 있습니다.\\n미래에 그 옷 레이어드로 껴입고 노숙이라도 하실 기세라 참 든든합니다."},
                            "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": {"title": "💅 손끝 발끝 풀소유 허세 영애", "desc": "손톱 위에 화려한 파츠 올리고 속눈썹 바짝 바비인형처럼 끌어올려 겉치레 품격은 채웠으나 정작 자산 성장률은 바닥에 바짝 붙여버린 관리의 대가.\\n키보드 두드릴 때 손톱에서 영롱한 빛이 나니 월급이 삭제되는 고통도 잊으셨나 봅니다.\\n그 파츠 떼어다 주식 시장에 예수금으로 박을 생각은 능 지상 불가능하셨습니까?"}
                        }
                        card_info = custom_cards.get(selected_option, {"title": "🛍️ 프로 시발비용러", "desc": "소소한 지출과 충동구매에 영혼을 지배당해 미래 자산 퀀텀점프의 버스를 쿨하게 놓치신 멍청한 직장인.\\n남들 은퇴해서 파이어족으로 호의호식할 때 님은 환갑 넘어서도 이 사이트 켜고 '그때 살 걸...' 하며 피눈물 흘릴 운명입니다."})
                else:
                    card_info = {"title": "🛡️ 자산 수호 헷지 명인", "desc": "폭락 사이클을 영리한 탕진 소비로 우회 방어해 낸 금융 위기관리의 천재"}

                # 대화방 연동용 데이터 보관 및 정신승리 데이터 연산 바인딩
                st.session_state["current_audit"] = {
                    "habit_key": selected_option, # 포모 차단기 1:1 매칭용 키 추가
                    "habit": habit_clean_name,
                    "asset": asset_clean_name,
                    "future_val": f"{int(future_value):,} 원",
                    "grade": card_info["title"],
                    "seed": total_seed
                }

                # 데이터 출력부 (순서 조정)
                st.write("---")
                st.markdown(f"<h3 style='color: #FFFFFF; font-size: 17px;'>🔍 0. 데이터 신뢰성 검증 리포트</h3>", unsafe_allow_html=True)
                val_col1, val_col2 = st.columns(2)
                with val_col1:
                    display_then = f"{then_price:,} 원" if not is_foreign else f"${then_price:,} (원화 약 {int(then_price*exchange_rate):,} 원)"
                    st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 15px; border-radius: 8px; background-color: #1A1D20;"><div style="font-size: 11px; color: #AAADB0;">⏳ {max_idx}년 전 실제 당일 가격</div><div style="font-size: 17px; font-weight: 600; color: #F28B82; margin-top: 5px;">{display_then}</div></div>""", unsafe_allow_html=True)
                with val_col2:
                    display_now = f"{current_price:,} 원" if not is_foreign else f"${current_price:,} (원화 약 {int(current_price*exchange_rate):,} 원)"
                    st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 15px; border-radius: 8px; background-color: #1A1D20;"><div style="font-size: 11px; color: #81C995;">✨ 현재 실시간 시세</div><div style="font-size: 17px; font-weight: 600; color: #81C995; margin-top: 5px;">{display_now}</div><div style="font-size: 11px; color: #FFFFFF; margin-top: 3px; font-weight: bold;">📊 {max_idx}년 간 순수 누적 수익률: {total_asset_growth:+.2f}%</div></div>""", unsafe_allow_html=True)

                st.write("")
                st.markdown("<h3 style='color: #FFFFFF; font-size: 17px;'>📊 1. 과거 데이터 기반 세부 실시간 정산</h3>", unsafe_allow_html=True)
                res_col1, res_col2, res_col3 = st.columns(3)
                with res_col1: st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 11px; color: #AAADB0; font-weight: 500;">🪙 총 지출 매몰 원금</div><div style="font-size: 21px; font-weight: 600; color: #FFFFFF; margin-top: 5px;">{int(total_seed):,} 원</div></div>""", unsafe_allow_html=True)
                with res_col2: st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: #81C995; font-weight: 500;">📈 현재 자산 가치 (오늘)</div><div style="font-size: 21px; font-weight: 600; color: #81C995; margin-top: 5px;">{int(final_value):,} 원</div></div>""", unsafe_allow_html=True)
                with res_col3:
                    card_color = "#F28B82" if missed_money > 0 else "#8AB4F8"
                    status_text = "🚨 기회상실 순손실액" if missed_money > 0 else "🛡️ 리스크 최종 방어액"
                    st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 11px; color: {card_color}; font-weight: 500;">{status_text}</div><div style="font-size: 21px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div></div>""", unsafe_allow_html=True)

                st.write("")
                st.markdown(f"<h3 style='color: #FFFFFF; font-size: 17px;'>🔮 2. 미래 {years}년 뒤 자산 행복회로 퀀텀점프 예측</h3>", unsafe_allow_html=True)
                fut_col1, fut_col2 = st.columns(2)
                with fut_col1: st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;"><div style="font-size: 12px; color: #D6BCFA; font-weight: 500;">🚀 미래 엔진에 투영된 과거 에너모멘텀</div><div style="font-size: 22px; font-weight: 600; color: #D6BCFA; margin-top: 5px;">{total_asset_growth:+.2f} % 직진 반영</div></div>""", unsafe_allow_html=True)
                with fut_col2: st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1FFD700; background-color: #1A1B2F;"><div style="font-size: 12px; color: #FFD700; font-weight: 500;">💰 미래 {years}년 뒤 최종 잔고 예측</div><div style="font-size: 22px; font-weight: 600; color: #FFD700; margin-top: 5px;">{int(future_value):,} 원</div></div>""", unsafe_allow_html=True)

                # 🛠️ [기획 핵심 이식 2] 3. 인스타 스토리 '껄껄 리포트' 카드 (완벽한 오류 회피형 인라인 CSS)
                st.write("")
                st.markdown("### 📸 3. 인스타 스토리 박제용 캡처 카드")
                
                # 중괄호 충돌을 원천 차단하기 위해, 인라인 CSS를 안전하게 적용하여 진짜 인스타 느낌의 사각형 카드로 렌더링합니다!
                st.markdown(f"""
<div style="background: linear-gradient(135deg, #121212 0%, #1A1A2E 100%); border: 3px solid #E91E63; padding: 30px; border-radius: 20px; max-width: 440px; margin: 0 auto; color: #FFFFFF; box-shadow: 0 10px 30px rgba(233,30,99,0.3); text-align: center; aspect-ratio: 1/1; display: flex; flex-direction: column; justify-content: center;">
<span style="font-family: sans-serif; font-size: 13px; font-weight: bold; letter-spacing: 2px; color: #E91E63; text-transform: uppercase; margin-bottom: 15px;">📊 껄껄 리포트 (GGUL-GGUL REPORT)</span>

<h2 style="font-family: sans-serif; font-size: 22px; font-weight: 800; color: #FFFFFF; margin: 0 0 5px 0; letter-spacing: -1px; line-height: 1.4;">"{ggul_card_title}"</h2>
<span style="font-family: sans-serif; font-size: 13px; color: #AAADB0; font-weight: 400; margin-top: 5px;">그 돈으로 {asset_clean_name} 적립 매수했다면...</span>

<div style="margin: 20px 0; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); padding: 15px 0;">
<div style="font-family: sans-serif; font-size: 12px; color: #AAADB0; margin-bottom: 5px;">💸 공중에 분해된 투자 원금</div>
<div style="font-family: sans-serif; font-size: 20px; font-weight: 700; color: #F28B82; margin-bottom: 15px;">{int(total_seed):,} 원</div>

<div style="font-family: sans-serif; font-size: 12px; color: #AAADB0; margin-bottom: 5px;">🔮 미래 {years}년 뒤 행복회로 최종 잔고</div>
<div style="font-family: sans-serif; font-size: 28px; font-weight: 800; color: #FFD700; background: linear-gradient(45deg, #FFD700, #FFA500); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{int(future_value):,} 원</div>
</div>

<span style="font-family: sans-serif; font-size: 12px; color: #E91E63; font-weight: bold;">🦜 껄무새 대시보드에서 나도 확인하기</span>
</div>
""", unsafe_allow_html=True)

                # 소비 맞춤형 흑우 등급 카드 (annoying, triggering but clean)
                st.write("")
                if missed_money > 0:
                    custom_cards = {
                        "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": {"title": "🩸 혈당 폭발 마라탕 중독자", "desc": "마라 국물과 설탕 코팅에 영혼을 저당 잡아 혈당을 올리는 사이, 본인의 시드머니는 주식 시장에서 완전히 녹아내리게 방치한 위대한 푸드 파이터.\\n입안의 사치와 뱃살을 얻은 대가로 통장 잔고의 미래 척추는 완벽하게 아작이 나 버렸습니다.\\n미래에 포르쉐 대신 마라탕 그릇이나 핥고 있을 귀하의 흐린 눈을 응원합니다.", "bg": "linear-gradient(135deg, #8B0000 0%, #1A1D20 100%)"},
                        "스타벅스 바닐라라떼+디저트 (1회 11,000원)": {"title": "☕ 사이렌 오더 명예 기부 의장", "desc": "매달 스타벅스 별사냥과 고카페인 시럽에 취해 살며 스타벅스 코리아 매출 상승에는 기여했으나 정작 본인 계좌는 공황 상태에 빠뜨린 주주.\\n정작 본인 계좌는 한파 주의보가 내렸는데 매일 아침 당당하게 닉네임 불리며 커피 픽업하는 모습이 참 눈물겹습니다.\\n그 컵홀더 모아두면 미래에 강남 아파트 전세라도 준답니까?", "bg": "linear-gradient(135deg, #124E3F 0%, #1A1D20 100%)"},
                        "올리브영 세일 '구경만' 가기 (1회 45,000원)": {"title": "💄 올리브영 탕진 잼 마스터", "desc": "세일 문자만 오면 '구경만 해야지' 하고 들어가 틴트와 팩으로 바구니를 채우며 CJ 올리브영 시총 방어에 본인 시드를 갈아 넣은 VVIP 흑우.\\n피부는 일시적으로 매끈해졌을지 몰라도, 귀하의 투자 포트폴리오는 전라로 굶주려 비명을 지르고 있습니다.\\n미래에 그 화장품 다 바르고 한강 뷰 보며 울고 계실 모습이 참으로 선합니다.", "bg": "linear-gradient(135deg, #5B7065 0%, #1A1D20 100%)"},
                        "불금 배달 엽떡+치킨 세트 (1회 32,000원)": {"title": "🐔 배달 앱 다이아몬드 등급", "desc": "금요일 밤의 고독과 스트레스를 캡사이신과 튀김 옷으로 위로하느라, 통장에 억 단위 자산이 쌓일 기회를 아주 야무지게 씹어 삼키신 야식 마스터.\\n라이더 영웅들에게 배달 팁 쾌척하며 자선사업 하시는 동안 귀하의 노후 자금은 완벽하게 멸망의 길로 직진했습니다.\\n남은 치킨 무 국물이나 마시며 껄껄 대십시오.", "bg": "linear-gradient(135deg, #4A154B 0%, #1A1D20 100%)"},
                        "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": {"title": "👗 새벽 배송 폰결제 야수", "desc": "침대에 누워 흐린 눈으로 옷 구경하다 네이버페이 6자리를 광속으로 태우며, 방구석 드레스룸은 채웠으나 자산 포트폴리오는 전라로 만든 패셔니스타.\\n방구석 옷장은 미어터지지만 주식 계좌는 알거지 상태로 처참하게 방치되어 인공호흡기를 달고 있습니다.\\n미래에 그 옷 레이어드로 껴입고 노숙이라도 하실 기세라 참 든든합니다.", "bg": "linear-gradient(135deg, #3A225D 0%, #1A1D20 100%)"},
                        "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": {"title": "💅 손끝 발끝 풀소유 영애", "desc": "손톱 위에 파츠를 올리고 눈썹을 바짝 끌어올려 비주얼 품격은 유지했으나, 정작 본인 자산 성장률은 바닥에 바짝 붙여버린 관리의 대가.\\n키보드 두드릴 때 손톱에서 영롱한 빛이 나니 월급이 삭제되는 고통도 잊으셨나 봅니다.\\n그 파츠 떼어다 주식 시장에 예수금으로 박을 생각은 능 지상 불가능하셨습니까?", "bg": "linear-gradient(135deg, #1C3D5A 0%, #1A1D20 100%)"},
                        "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": {"title": "🥃 고독한 알코올 오크통 주주", "desc": "피트 향 머금은 싱글몰트로 오늘 하루의 서러움을 녹이려다 통장 잔고까지 완벽하게 증발시켜 미장 빅테크 주주들의 기쁨이 되어주신 알코올 요정.\\n간 건강 사수하고 호텔 전신 스파를 받았을 기회비용은 가볍게 잊어주십시오.", "bg": "linear-gradient(135deg, #8A4F1D 0%, #1A1D20 100%)"},
                        "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": {"title": "🎮 데이터 쪼가리 풀소유 야수", "desc": "모니터 속 전설 스킨과 가챠 연출의 도파민에 취해 클릭 몇 번으로 실제 집 한 채 살 돈을 게임 서버 유지비로 쾌척해 버린 명예 야수.\\n덕분에 게임사 주주들은 발 뻗고 잠을 잡니다. 님 덕분에 자본주의 시장이 돌아갑니다.", "bg": "linear-gradient(135deg, #2D3748 0%, #1A1D20 100%)"},
                        "주말 골프 연습장/필드 호사 (1회 120,000원)": {"title": "⛳ 잔디밭 지출의 나이스샷", "desc": "굿샷을 외치며 그린 위에서 호사를 누리는 동안 정작 본인 주식 자산 포트폴리오는 OB 구역 숲속으로 완벽하게 날려버린 필드의 타이거 흑우.\\n그린 위 슬라이스 대신 내 자산 홀인원을 꿈꾸는 낭만 가득한 라이프스타일이 참 눈물겹습니다.", "bg": "linear-gradient(135deg, #2F855A 0%, #1A1D20 100%)"},
                        "기념일 에피타이저 오마카세 (1회 150,000원)": {"title": "🍣 럭셔리 파인다이닝 영애", "desc": "셰프의 친절한 설명을 들으며 입안의 사치를 즐기는 순간, 내 통장 잔고는 엔비디아의 성장 에너지를 먹지 못해 원자 단위로 굶주려가던 모순의 극치.\\n덕분에 프랑스 파리에서 진짜 에스카르고 썰었을 기회비용은 멋지게 날아가 버렸습니다.", "bg": "linear-gradient(135deg, #744210 0%, #1A1D20 100%)"},
                        "체형 교정 명목 필라테스 (1회 60,000원)": {"title": "🧘 기구 위에서 비명지르는 영애", "desc": "코어 근육을 단단하게 잡아내어 척추 정렬에는 성공했으나, 정작 미래 내 집 마련을 위한 자산의 척추는 완벽하게 무너뜨린 관리의 모순.\\n기구 비명 대신 수익률로 허리를 폈어야 했는데 참으로 선합니다.", "bg": "linear-gradient(135deg, #4A5568 0%, #1A1D20 100%)"},
                        "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": {"title": "⚽ 방구석 올드 트래포드 구단주", "desc": "해외 축구 구단의 엠블럼 패치를 보며 밤마다 열광했으나, 정작 본인 자산 리그는 4부 리그 강등권에서 처참하게 헤매게 만든 유니폼 수집가.\\n유니폼 장식 대신 그 구단 주식 샀을 기회비용은 잊고 맥주나 들이켜십시오.", "bg": "linear-gradient(135deg, #9B2C2C 0%, #1A1D20 100%)"}
                    }
                    card_info = custom_cards.get(selected_option, {"title": "🛍️ 프로 시발비용러", "desc": "소소한 지출로 도파민을 채우며 미래 자산 퀀텀점프의 기회를 쿨하게 걷어차신 직장인 영애/대리", "bg": "linear-gradient(135deg, #4A5568 0%, #1A1D20 100%)"})
                else:
                    card_info = {"title": "🛡️ 자산 수호 헷지 명인", "desc": "폭락 사이클을 영리한 탕진 소비로 우회 방어해 낸 금융 위기관리의 천재", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"}
                
                st.markdown(f"""<div style="background: {card_info['bg']}; border: 1px solid #3C4043; padding: 20px; border-radius: 12px; text-align: center; color: #FFFFFF; font-size: 13.5px; max-width: 440px; margin: 15px auto;"><b>🏅 흑우 판정 등급: {card_info['title']}</b><br><span style='color: #E8EAED; font-size:12.5px;'>{card_info['desc']}</span></div>""", unsafe_allow_html=True)

        # TAB 2: 사주 운세
        with tab2:
            st.markdown("### 🔮 생년월일 명리 기반 주식 매수 타이밍 진단")
            st.write("8자리 생년월일 기운을 오행으로 분해하여, 질문하신 주식 종목의 진입 적절성을 사주학적으로 감정합니다.")
            
            user_birth = st.text_input("🎂 생년월일 8자리를 입력하세요 (예: 19961025)", max_chars=8, placeholder="19950714", key="saju_birth")
            stock_question = st.text_input("💬 주식 질문을 던지세요", placeholder="예: 삼성전자 오늘 사도 될까요?", key="saju_stock")
            
            if st.button("☯️ 껄무새 도사에게 사주 연동 점괘 받기"):
                if len(user_birth) < 8 or not stock_question: st.error("🚨 생년월일 8자리와 질문을 채워라 휴먼!")
                else:
                    seed_num = sum([int(char) for char in user_birth]) % 4
                    clean_stock = stock_question.replace("사도 될까요", "").replace("사도 됨", "").strip()
                    saju_responses = [
                        f"🔮 점괘 결과: [🔥 화(火)기운 과다 / 편재살 대치]\\n\\n오늘 손가락에 급격한 충동 매수 마귀가 꼈습니다. '{clean_stock}'(으)로 대박 노리다간 고점에 처물리기 딱 좋습니다. 지갑 닫으십시오.",
                        f"🔮 점괘 결과: [🌱 목(木)기운 보존 / 정재 귀인 합류]\\n\\n사주에 재물창고를 채우는 대길의 운이 흐릅니다. '{clean_stock}'을(를) 오늘 쪼개서 진입하는 것은 도파민을 황금알로 바꾸는 전략입니다.",
                        f"🔮 점괘 결과: [🪨 토(土)기운 정체 / 겁재살 강세]\\n\\n내 돈을 강탈하는 겁재살이 강합니다. 지금 '{clean_stock}' 주문을 넣으면 외인과 기관의 밥이 될 뿐이니 치킨이나 한마리 시켜 드십시오.",
                        f"🔮 점괘 결과: [🌊 수(水)기운 유동 / 식신생재 활성화]\\n\\n돈복이 물밀듯 밀려옵니다. 의심을 거두고 '{clean_stock}'에 소신껏 진입하는 것은 매우 훌륭한 자산 액막이가 될 것입니다."
                    ]
                    st.info(saju_responses[seed_num])

        # TAB 3: 밸런스 게임
        with tab3:
            st.markdown("### ⚔️ 주주총회 자산 파괴 밸런스 게임")
            st.write("2030 영애·대리들의 계좌와 멘탈을 완벽하게 고문하는 극한의 밸런스 매치업입니다.")
            
            # 현재 게임 인덱스 및 세팅
            game_idx = st.session_state["current_game_index"]
            game = st.session_state["balance_games"][game_idx]
            
            st.markdown(f"**질문 {game_idx + 1} / 10**")
            st.markdown(f"#### Q. {game['q']}")
            
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                if st.button(f"🅰️ {game['opt_a']}", key=f"btn_a_{game_idx}"):
                    st.session_state["balance_games"][game_idx]["votes_a"] += 1
                    # 이전 투표 결과 캐싱 후 다음 게임 이동
                    tot = game["votes_a"] + game["votes_b"] + 1
                    st.session_state["last_voted_result"] = {
                        "q": game["q"],
                        "voted": "🅰️ " + game["opt_a"],
                        "pct_a": ( (game["votes_a"] + 1) / tot ) * 100,
                        "pct_b": ( game["votes_b"] / tot ) * 100,
                        "total": tot
                    }
                    st.session_state["current_game_index"] = (game_idx + 1) % len(st.session_state["balance_games"])
                    st.toast("✅ 투표 성공! 다음 질문으로 넘어갑니다.")
                    st.rerun()
            with col_v2:
                if st.button(f"🅱️ {game['opt_b']}", key=f"btn_b_{game_idx}"):
                    st.session_state["balance_games"][game_idx]["votes_b"] += 1
                    tot = game["votes_a"] + game["votes_b"] + 1
                    st.session_state["last_voted_result"] = {
                        "q": game["q"],
                        "voted": "🅱️ " + game["opt_b"],
                        "pct_a": ( game["votes_a"] / tot ) * 100,
                        "pct_b": ( (game["votes_b"] + 1) / tot ) * 100,
                        "total": tot
                    }
                    st.session_state["current_game_index"] = (game_idx + 1) % len(st.session_state["balance_games"])
                    st.toast("✅ 투표 성공! 다음 질문으로 넘어갑니다.")
                    st.rerun()
            
            # 이전 라운드의 리얼 투표 결과 실시간 아기자기 표시
            if st.session_state["last_voted_result"] is not None:
                last_res = st.session_state["last_voted_result"]
                with st.container(border=True):
                    st.markdown(f"🗳️ **직전 투표 결과 브리핑**")
                    st.caption(f"Q. {last_res['q']}")
                    st.markdown(f"선택: `{last_res['voted']}`")
                    st.progress(int(last_res["pct_a"]))
                    st.caption(f"📊 주주 지지율: 🅰️ {last_res['pct_a']:.1f}% vs 🅱️ {last_res['pct_b']:.1f}% (총 {last_res['total']}명 참전)")

        # TAB 4: 포모 차단기
        with tab4:
            st.markdown("### 🧠 뇌과학 기반 멘탈 세이프티 포모(FOMO) 차단기")
            st.write("주식 안 사고 내 몸과 정신에 맛있고 예쁘게 탕진한 나 자신을 위한 과학적 정신 승리 진단서")
            
            if st.session_state["current_audit"] is None:
                st.warning("💡 먼저 '📊 자산 타임머신' 탭에서 시뮬레이션을 한 번 돌리고 오셔야 정밀 뇌스캔이 작동합니다!")
            else:
                audit_data = st.session_state["current_audit"]
                habit_key = audit_data.get("habit_key", "")
                habit_clean_name = audit_data["habit"]
                asset_clean_name = audit_data["asset"]
                
                # 뇌과학적 모근 수치 연산
                base_seed = audit_data["seed"]
                dopamine_score = int((base_seed / 10000) * 12) + 500
                cortisol_saved = int(dopamine_score * 8.4)
                hair_saved = int(base_seed / 250000) + 120
                
                # 🛍️ 소비성 항목별 1:1 매칭 멘탈 위로 데이터베이스 구축
                custom_fomo_dict = {
                    "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": "수명 쿨타임을 마라의 캡사이신 자극으로 연장하는 도파민 대환장 파티! 만약 주식 사서 매일 장대 음봉 보며 피눈물 흘렸다면, 위궤양과 역류성 식도염으로 이미 위장 세포 수천만 개가 궤멸했을 것입니다. 장 정렬과 위장 평화를 지켜낸 님이 진정한 건강 주주입니다.",
                    "스타벅스 바닐라라떼+디저트 (1회 11,000원)": "매일 아침 달콤한 액상과당과 고농축 카페인으로 뇌세포에 활력을 가득 불어넣은 현명한 선택! 파랗게 물들어가는 빅테크 주식 창을 보며 머리를 쥐어짜다 혈압 상승으로 쓰러질 뻔한 뇌졸중 리스크를 스타벅스 컵 홀더로 완벽하게 헤징해 냈습니다.",
                    "올리브영 세일 '구경만' 가기 (1회 45,000원)": "화장대 위에 영롱한 틴트와 마스크팩을 가득 채우며 시각적 품격과 피부 진정을 달성한 VVIP 영애! 주식 하락세를 보며 얼굴을 찡그리느라 생겨났을 미간 주름과 피부 노화 진행을 올리브영 세일 패키지로 철통 방어해 냈습니다. 거울 속에 빛나는 님이 진정한 자산입니다.",
                    "불금 배달 엽떡+치킨 세트 (1회 32,000원)": "일주일의 서러움과 노동의 고단함을 화끈한 엽기떡볶이와 바삭한 튀김옷으로 야무지게 씻어내어 뇌내 세로토닌을 퀀텀점프 시킨 신의 한 수! 주식 고점에 물려 주말 내내 주식 게시판에서 키보드 배틀 뜨느라 뇌세포 3억 개를 소멸시킬 뻔한 스트레스 폭탄을 치킨무 국물로 진화하셨습니다.",
                    "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": "내 방 옷장에 예쁜 전투복을 가득 채워 출근길 어깨를 펴고 도파민 서장을 달성한 패셔니스타! 하락장 폭격을 맞고 헐벗은 계좌를 보며 멘탈이 전라(裸) 상태가 되어 떨고 있을 뻔한 최악의 사태를 지그재그 네이버페이 결제로 완벽 방어하셨습니다.",
                    "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": "손톱 위에 빛나는 파츠를 올리고 속눈썹을 바짝 올려 비주얼 아우라를 최상단 밴드로 유지하신 관리의 대가! 마이너스 난 잔고를 타이핑하며 손 떨다가 손톱 다 부러질 뻔한 우울증 리스크를, 영롱한 네일 정기권으로 완벽히 코팅하여 내면의 품격을 수호해 냈습니다.",
                    "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": "피트 향 가득한 싱글몰트 한 잔으로 오늘 하루의 노동 강박과 서러움을 원자 단위로 분해해 낸 위대한 연금술사! 주식 호가창의 초록불 빨간불에 영혼이 털리며 피폐해졌을 멘탈을 숙성 오크통의 은총으로 사수하셨습니다. 간은 힘들어도 영혼은 풍요롭습니다.",
                    "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": "모니터 속 넷상 전설 스킨의 화려한 임팩트로 어깨에 우주적 뽕을 주입해 낸 데이터 자산의 명예 구단주! 실물 없는 주식 시장의 세력 상어들에게 내 금쪽같은 현금을 먹히느라 홧병 생길 뻔한 스트레스를, 화려한 인게임 연출 도파민으로 조기 진화 완료했습니다.",
                    "주말 골프 연습장/필드 호사 (1회 120,000원)": "탁 트인 푸른 잔디밭에서 호쾌하게 드라이버를 갈기며 우주적 호사를 누린 스포츠의 제왕! 주가 차트의 OB 구역 폭락을 보며 멘탈이 산산조각 나 머리 빠질 탈모 위험을, 피톤치드 가득한 필드 위 나이스샷으로 모근 세포 약 15만 개를 든든하게 방어해 내셨습니다.",
                    "기념일 에피타이저 오마카세 (1회 150,000원)": "셰프의 우아한 서비스와 참치 뱃살의 사치를 혀끝으로 고스란히 느끼며 자존감을 천상계로 끌어올린 금융 미식가! 반도체 횡보장을 버티다 위벽이 헐어 위산 과다로 고통받을 기회비용을 오마카세 스페셜 피스로 가차 없이 헷징해 낸 영리한 혀끝의 트레이더십니다.",
                    "체형 교정 명목 필라테스 (1회 60,000원)": "무거운 기구 위에서 비명을 지르며 척추 뼈마디 정렬을 기어이 성공시킨 코어 자산의 사령탑! 마이너스 계좌를 보며 척추를 구부정하게 만 채 실시간으로 척추 디스크 터질 뻔한 위기를, 기구 필라테스로 꼿꼿하게 버텨내 통장 척추 대신 진짜 내 척추를 수호하셨습니다.",
                    "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": "최애 구단 엠블럼을 가슴에 박고 밤마다 맥주를 들이켜며 전 세계 축덕들과 유대 에너지를 뿜어낸 골수 구단주! 내가 적립식으로 모은 주식이 4부 리그로 처참하게 강등당해 심근경색 올 뻔한 리스크를, 영롱한 레플리카 수집 도파민으로 평화롭게 우회 헷징 하셨습니다."
                }
                
                # 직접 입력 유저를 위한 범용 멘트
                default_fomo = f"본인만의 확고하고 독창적인 고유 소비 버릇인 '{habit_clean_name}'에 시드를 털어 넣어 일상 도파민 자산을 획득한 금융 헷지 마스터! 주식의 하방 폭격을 얻어맞고 홧병으로 뇌세포 3억 개가 동시 폭파당할 뻔한 리스크를, 힙하고 맛있는 탕진 소비로 선제 방어하셨습니다. 님 돈 님 소비 나이스샷!"
                tailored_report = custom_fomo_dict.get(habit_key, default_fomo)
                
                with st.container(border=True):
                    st.markdown(f"<center><b>🧠 귀하의 소비 행동에 따른 생체 이득 정산서</b></center>", unsafe_allow_html=True)
                    st.write("")
                    
                    m_c1, m_c2, m_c3 = st.columns(3)
                    with m_c1: st.metric(label="🔋 충전된 도파민", value=f"{dopamine_score:,} pg/mL", delta="인생 행복 지수 증가")
                    with m_c2: st.metric(label="🛡️ 방어한 스트레스 (코르티솔)", value=f"{cortisol_saved:,} 🌟", delta="주식 화병 완벽 차단")
                    with m_c3: st.metric(label="💇 사수한 모근(毛根) 개수", value=f"약 {hair_saved:,} 개", delta="하락장 탈모 리스크 헷지")
                    
                    st.write("---")
                    st.markdown(f"""
                    **💡 껄무새 도사의 최종 뇌과학 위로 소견서**  
                    만약 귀하가 탕진 지출 대신 눈물 흘려가며 진짜로 **'{audit_data['asset']}'** 주식을 매수했다면, 매일 오전 9시 주식 창이 열릴 때마다 심장이 벌렁거리고 하락장 폭격을 맞으며 이미 **약 {hair_saved:,}개의 모근이 장렬히 탈모**되었을 것으로 추정됩니다.
                    
                    비록 미래 가치 {audit_data['future_val']}의 기회비용은 날렸을지언정, 귀하는 **'{habit_clean_name}'** 지출을 통해:
                    
                    > *{tailored_report}*
                    
                    결론적으로 주식 시장의 세력 상어들에게 뜯기느니 내 위장과 비주얼, 내 육체 자산에 영리하게 기부한 당신이 정신의학적 최종 승리자입니다. 마음 편하게 꿀잠 자고 내일 기분 좋게 루팡 하십시오! 🚀
                    """)

    # ==================== [RIGHT SIDE] 우측 고정방 및 실시간 인원 카운터 ====================
    with chat_layout:
        try:
            from streamlit.runtime.runtime import Runtime
            stats = Runtime.instance()._session_mgr.list_active_sessions()
            real_active_users = len(stats)
            if real_active_users < 1: real_active_users = 1
        except:
            real_active_users = 1
            
        st.markdown(f"<h3 style='margin-top:23px; font-size:16px;'>💬 실시간 오픈방 <span style='font-size:12px; color:#81C995; font-weight:normal;'>🟢 실제 {real_active_users}명 루팡 중</span></h3>", unsafe_allow_html=True)
        
        if st.session_state["current_audit"] is not None:
            audit = st.session_state["current_audit"]
            st.caption(f"🏅 **내 등급:** {audit['grade']}")
            if st.button("👑 내 등급 바로 인증", use_container_width=True):
                cert_text = f"🚨 [매운맛인증] 내 탕진: '{audit['habit']}' ➡️ '{audit['asset']}' 에 박았으면 미래 잔고 **{audit['future_val']}** 떴음; 팩폭 등급: [{audit['grade']}]"
                st.session_state["chat_messages"].append({"role": "user", "name": f"인증러_{random.randint(100,999)}", "text": cert_text})
                st.session_state["current_audit"] = None
                st.toast("✅ 대화방에 팩폭 등급 박제 성공!", icon="🔥")
                st.rerun()

        chat_container = st.container(height=450)
        with chat_container:
            for msg in st.session_state["chat_messages"]:
                is_cert = "[매운맛인증]" in msg["text"] or "[흑우인증]" in msg["text"]
                avatar_icon = "👑" if is_cert else "🦜"
                with st.chat_message(msg["role"], avatar=avatar_icon):
                    st.markdown(f"**{msg['name']}**")
                    if is_cert: st.caption(msg["text"])
                    else: st.write(msg["text"])

        if user_live_input := st.chat_input("우측 오픈방에 익명으로 한탄하기..."):
            st.session_state["chat_messages"].append({"role": "user", "name": f"익명_{random.randint(100,999)}", "text": user_live_input})
            st.rerun()
