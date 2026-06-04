import streamlit as st
import streamlit.components.v1 as components
import datetime
import random

# 1. 껄무새 다크모드 기반 최적화 설정
st.set_page_config(
    page_title="✨ 껄무새 - 2030 필수 자산 케어 v29", 
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
    st.session_state["vote_data"] = [
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

    # 헤더 섹션
    st.markdown("""
        <div style="margin-bottom: 5px;">
            <span style="font-size: 38px; font-weight: 800; background: linear-gradient(45deg, #4285F4, #9B51E0, #E91E63); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px;">
                🦜 껄무새
            </span>
        </div>
    """, unsafe_allow_html=True)

    # 🚨 [신설] 1번, 4번 기획: 실시간 글로벌 마켓 도파민 신호등 메인 보드
    today_seed_gen = int(datetime.date.today().strftime('%Y%m%d'))
    random.seed(today_seed_gen)
    fg_index = random.randint(25, 82) # 실시간 공포탐욕지수 시뮬레이션
    
    if fg_index < 40:
        fg_status = "📉 극단적 공포 (Extreme Fear)"
        fg_color = "#F28B82"
        fg_advice = "시장 전체가 패닉셀 중입니다. 지금 탕후루/위스키 끊고 우량주 주우면 미래에 퀀텀점프합니다."
        signal_led = "🟢 예수금 충전 라이트 온"
    elif fg_index > 65:
        fg_status = "🚀 극단적 탐욕 (Extreme Greed)"
        fg_color = "#81C995"
        fg_advice = "포모(FOMO)에 눈 돌아서 고점에 침수당하기 딱 좋은 날. 충동 매수 멈추고 커피나 마시며 관망하세요."
        signal_led = "🔴 충동 매수 뇌절 경보 발령"
    else:
        fg_status = "📊 중립 기어 (Neutral)"
        fg_color = "#8AB4F8"
        fg_advice = "무난한 시장 분위기. 흐린 눈 지출을 아껴 적립식 매수를 기계적으로 실행하기 적절한 타이밍입니다."
        signal_led = "🟡 상시 적립 유효 보드 가동"

    st.markdown(f"""
        <div style="border: 1px solid #3C4043; padding: 15px; border-radius: 10px; background-color: #1A1D20; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size: 11px; color: #AAADB0; font-weight: 600; letter-spacing: 1px;">🚨 REAL-TIME FINANCIAL DOPAMINE MONITOR</span>
                    <h4 style="margin: 5px 0 0 0; font-size: 16px; color: #FFFFFF;">글로벌 공포&탐욕 지수: <span style="color: {fg_color}; font-weight: bold;">{fg_index} ({fg_status})</span></h4>
                </div>
                <div style="background-color: #2D3136; padding: 8px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; color: {fg_color}; border: 1px solid {fg_color};">
                    {signal_led}
                </div>
            </div>
            <p style="margin: 10px 0 0 0; font-size: 13px; color: #AAADB0; line-height: 1.4;">💡 <b>오늘의 껄무새 마켓 소견:</b> {fg_advice}</p>
        </div>
    """, unsafe_allow_html=True)
    
    random.seed() # 다음 연산을 위해 시드 리셋

    # 좌우 분할 구조 레이아웃 (2.5 대 0.8)
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
                if selected_option == "✍️ 내 쓸모없는 지출 직접 입력하기":
                    habit_clean_name = custom_habit_name if custom_habit_name else "익명 탕진 지출"
                    unit_price = custom_habit_price
                    ggul_title = f"\"{habit_clean_name}\" 안 사고 진작 조기 퇴사했을 '껄'"
                else:
                    habit_clean_name = selected_option.split(" (")[0]
                    unit_price = HABIT_PRICE_DICT[selected_option]
                    
                    # 껄 리포트 전용 커스텀 후회 매핑 타이틀
                    GGUL_TITLE_MAP = {
                        "탕후루/마라탕 수명 단축 쿨타임": "마라탕 끊고 엔비디아 풀매수해서 건물 올렸을 '껄'",
                        "스타벅스 바닐라라떼+디저트": "스벅 프리미엄 당수치 올릴 돈으로 건물주 됐을 '껄'",
                        "올리브영 세일 '구경만' 가기": "올영 올인할 시드로 시총 우량주 풀소유 해봤을 '껄'",
                        "불금 배달 엽떡+치킨 세트": "야식 배달 라이더 팁 쏠 돈으로 배달 앱 주주 됐을 '껄'",
                        "지그재그/W컨셉 충동 의류 매수": "지그재그 장바구니 비우고 테슬라 평단가 낮췄을 '껄'",
                        "매달 속눈썹 펌/네일 정기권": "네일 파츠 올릴 정성으로 계좌 평단가 심폐소생했을 '껄'",
                        "퇴근 후 카미카제 주말 위스키": "위스키 가오 잡을 세금 아껴 위스키 수입사 대주주 됐을 '껄'",
                        "플랫폼 가챠/게임 스킨 현질": "게임 픽업 가챠 지를 돈으로 게임 개발사 인수했을 '껄'",
                        "주말 골프 연습장/필드 호사": "골프장 머리 올리러 가다 내 계좌 주가 지붕 뚫었을 '껄'",
                        "기념일 에피타이저 오마카세": "오마카세 예약 똥줄 탈 돈으로 파인다이닝 배당받았을 '껄'",
                        "체형 교정 명목 필라테스": "필라테스 거울 셀카 찍다 내 계좌 성장률 째졌을 '껄'",
                        "유럽 축구 구단 감성 레플리카 유니폼": "축구 유니폼 수집할 열정으로 구단주 지분 샀을 '껄'"
                    }
                    ggul_title = GGUL_TITLE_MAP.get(habit_clean_name, f"\"{habit_clean_name}\" 아껴서 경제적 자유 누렸을 '껄'")

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
                
                # 🌶️ 선을 넘지 않는 킹받는(Triggering) 2~3줄 팩폭 코멘트 카드
                if missed_money > 0:
                    if selected_option == "✍️ 내 쓸모없는 지출 직접 입력하기":
                        if total_seed <= 3000000:
                            card_info = {"title": "🌱 응애급 소소한 탕진러", "desc": f"소액 결제 위주라 당장 계좌가 안 터질 것 같아 보이시나 봅니다.\n무심코 긁어버린 '{habit_clean_name}' 지출들이 뒤에서 주주의 미래를 야무지게 좀먹는 중입니다.\n하루라도 빨리 비밀번호 가방에 묶어두지 않으면 미래 평단가는 구렁텅이에서 올라올 수 없습니다."}
                        elif total_seed <= 15000000:
                            card_info = {"title": "💸 통장 믹서기 분쇄 대리", "desc": f"남들이 대가리 깨져가며 우량주 주워 담을 때, 탕진 리스트에 정성껏 시드를 갈아 넣으셨군요.\n'{habit_clean_name}' 명목으로 소멸시킨 천만 원대의 거금은 주식 시장의 세력들이 아주 달콤하게 나눠 가졌습니다.\n찰나의 도파민과 미래 최종 잔고 {int(future_value/10000):,}만 원을 완벽히 맞교환하신 위대한 자산 기부천사십니다."}
                        elif total_seed <= 50000000:
                            card_info = {"title": "🚨 장바구니 풀소유 광기 야수", "desc": f"웬만한 국산 중형차 풀옵션을 뽑고도 남을 거금을 오직 '{habit_clean_name}' 하나에 물 붓듯 태우셨네요.\n미래에 {asset_clean_name}의 폭발적인 상승 기류를 타고 조기 은퇴할 수 있는 골든 티켓을 셀프로 차단하셨습니다.\n내일 아침 출근길 버스 창가에 이마 대고 오늘 손실액을 찬찬히 곱씹으며 복습하시기 바랍니다."}
                        else:
                            card_info = {"title": "👑 자산 파괴계의 월드클래스 GOAT", "desc": f"걸어 다니는 인간 지표이자 자산 분쇄의 신이 우리 회사에 상주하고 계셨군요.\n억 단위의 기회비용을 오직 본인의 영혼이 담긴 '{habit_clean_name}' 지출 명목으로 자본주의 시장에 전부 헌납하셨습니다.\n덕분에 {asset_clean_name}의 진짜 주주들은 발 뻗고 편안하게 잡니다. 눈물 닦고 9시 정각에 보고서나 올리세요."}
                    else:
                        custom_cards = {
                            "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": {"title": "🩸 혈당 폭발 마라탕 중독자", "desc": "남들 반도체 사이클 호황 누릴 때 혼자 붉은 고추기름 국물과 설탕 시럽 코팅에 영혼을 저당 잡힌 돼지 주주님.\n입안의 사치와 뱃살을 얻은 대가로 통장 잔고의 미래 척추는 완벽하게 내려앉아 아작이 났습니다.\n포르쉐 핸들 대신 마라탕 숟가락 잡고 있을 미래의 자신에게 조용히 박수를 보내세요."},
                            "스타벅스 바닐라라떼+디저트 (1회 11,000원)": {"title": "☕ 사이렌 오더 명예 의장", "desc": "매달 스타벅스 프리미엄 별 사냥과 액상과당에 취해 살며 남의 나라 커피 기업 시총 방어에 본인 시드를 장렬히 갈아 넣으신 호구.\n본인 계좌는 한파 주의보가 내렸는데 아침마다 당당하게 닉네임 불리며 종이컵 받아오는 모습이 참 눈물겹습니다.\n그 컵홀더 모아두면 미래에 한강 뷰 아파트 전세 계약서로 바꿔 준답니까?"},
                            "올리브영 세일 '구경만' 가기 (1회 45,000원)": {"title": "💄 올영 시총 수호대 대장", "desc": "세일 알림 문자만 오면 눈이 뒤집혀서 '구경만 해야지' 하고 기어 들어가 장바구니 가득 팩과 틴트를 쟁여 나오는 지능적인 영애.\n피부는 일시적으로 매끈해졌을지 몰라도, 귀하의 투자 포트폴리오는 알거지 상태로 굶주려 비명을 지르고 있습니다.\n미래에 화장품 바닥까지 다 바르고 거울 보며 서럽게 울고 계실 모습이 참으로 든든합니다."},
                            "불금 배달 엽떡+치킨 세트 (1회 32,000원)": {"title": "🐔 배달 앱 다이아몬드 VVIP", "desc": "금요일 스트레스 핑계 대며 캡사이신과 기름진 닭 튀김으로 위장을 혹사하는 사이, 통장에 우량 자산이 꽂힐 기회는 야무지게 소화되어 사라졌습니다.\n라이더 영웅들에게 배달 팁 쾌척하며 자선사업 하시는 동안 귀하의 노후 자금은 완벽하게 멸망의 길로 직진했습니다.\n남은 치킨 무 국물이나 마시며 시원하게 껄껄 대십시오."},
                            "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": {"title": "👗 방구석 드레스룸 독재자", "desc": "침대에 누워 흐린 눈으로 옷 구경하다 네이버페이 지문 인식 광속으로 태우며 택배 박스 뜯는 도파민에 중독된 중꺾소 패셔니스타.\n방구석 옷장은 미어터지지만 주식 계좌는 인공호흡기를 단 채 비명을 지르고 있습니다.\n미래에 그 옷 레이어드로 수십 벌 겹쳐 입고 서울역 광장에서 노숙이라도 하실 기세라 참 보기 좋습니다."},
                            "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": {"title": "💅 손끝 발끝 풀소유 영애", "desc": "손톱 위에 파츠 가득 올리고 속눈썹 바짝 바비인형처럼 끌어올려 겉치레 품격은 채웠으나 정작 자산 성장률은 바닥에 메친 모순의 극치.\n키보드 두드릴 때 손가락에서 영롱한 빛이 나니 월급이 삭제되는 고통도 깨끗이 잊으셨나 봅니다.\n그 반짝이는 파츠 떼어다 주식 시장에 예수금으로 박을 이성적 판단은 애초에 불가능하셨습니까?"}
                        }
                        card_info = custom_cards.get(selected_option, {"title": "🛍️ 프로 시발비용러", "desc": "눈앞의 소소한 지출에 영혼을 지배당해 미래 자산 퀀텀점프의 황금 노선 버스를 쿨하게 놓치신 멍청한 직장인.\n남들 은퇴해서 휴양지에서 파이어족으로 호의호식할 때 님은 환갑 넘어서도 출근 셔틀버스 안에서 이거 켜고 피눈물 흘릴 운명입니다."})
                else:
                    card_info = {"title": "🛡️ 자산 수호 헷지 명인", "desc": "폭락 사이클을 예리한 자산 우회 방어로 피해 가며 내 통장의 순수 가치를 사수해 낸 위대한 금융 트레이더"}

                # 대화방 및 포모 차단기 연동용 세션 저장
                st.session_state["current_audit"] = {
                    "habit": habit_clean_name,
                    "asset": asset_clean_name,
                    "future_val": f"{int(future_value):,} 원",
                    "grade": card_info["title"],
                    "seed": total_seed,
                    "ggul_title": ggul_title
                }

                # 데이터 출력부
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
                with res_col2: st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 11px; color: #81C995; font-weight: 500;">📈 현재 자산 가치 (오늘)</div><div style="font-size: 21px; font-weight: 600; color: #81C995; margin-top: 5px;">{int(final_value):,} 원</div></div>""", unsafe_allow_html=True)
                with res_col3:
                    card_color = "#F28B82" if missed_money > 0 else "#8AB4F8"
                    status_text = "🚨 기회상실 순손실액" if missed_money > 0 else "🛡️ 리스크 최종 방어액"
                    st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 11px; color: {card_color}; font-weight: 500;">{status_text}</div><div style="font-size: 21px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div></div>""", unsafe_allow_html=True)

                st.write("")
                st.markdown(f"<h3 style='color: #FFFFFF; font-size: 17px;'>🔮 2. 미래 {years}년 뒤 자산 행복회로 퀀텀점프 예측</h3>", unsafe_allow_html=True)
                fut_col1, fut_col2 = st.columns(2)
                with fut_col1: st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;"><div style="font-size: 12px; color: #D6BCFA; font-weight: 500;">🚀 미래 엔진에 투영된 과거 에너모멘텀</div><div style="font-size: 22px; font-weight: 600; color: #D6BCFA; margin-top: 5px;">{total_asset_growth:+.2f} % 직진 반영</div></div>""", unsafe_allow_html=True)
                with fut_col2: st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;"><div style="font-size: 12px; color: #FFD700; font-weight: 500;">💰 미래 {years}년 뒤 최종 잔고 예측</div><div style="font-size: 22px; font-weight: 600; color: #FFD700; margin-top: 5px;">{int(future_value):,} 원</div></div>""", unsafe_allow_html=True)

                st.write("")
                st.markdown("### 📸 3. 인스타 스토리 박제용 캡처 카드")
                
                # 🛠️ 버그 완치: 들여쓰기를 완벽하게 수평 정렬하여 마크다운 코드블록 충돌 해결!
                html_card_layout = f"""
<div style="border: 3px solid #E91E63; padding: 25px; border-radius: 12px; background: linear-gradient(135deg, #1A1B2F 0%, #0D0E15 100%); width: 100%; max-width: 420px; aspect-ratio: 1/1; box-shadow: 0px 8px 24px rgba(233,30,99,0.2); margin: 0 auto; display: flex; flex-direction: column; justify-content: space-between; font-family: sans-serif;">
<div style="text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
<span style="font-size: 12px; font-weight: bold; letter-spacing: 2px; color: #FFD700;">📊 껄껄 리포트 (GGUL-GGUL REPORT)</span>
</div>
<div style="text-align: center; margin: 20px 0;">
<span style="font-size: 13px; color: #AAADB0; display: block; margin-bottom: 8px;">📢 절망의 무한 루프 헤드라인</span>
<h2 style="font-size: 19px; font-weight: 800; color: #FFFFFF; margin: 0; line-height: 1.4; word-break: keep-all;">"{ggul_title}"</h2>
</div>
<div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 12px 15px; border-radius: 8px; margin-bottom: 10px;">
<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
<span style="font-size: 11px; color: #AAADB0;">💸 소멸된 소비 원금</span>
<span style="font-size: 13px; font-weight: bold; color: #FFFFFF;">{int(total_seed):,} 원</span>
</div>
<div style="display: flex; justify-content: space-between;">
<span style="font-size: 11px; color: #81C995;">🔮 미래 예상 최종 자산</span>
<span style="font-size: 13px; font-weight: bold; color: #81C995;">{int(future_value):,} 원</span>
</div>
</div>
<div style="text-align: center; background: rgba(233,30,99,0.1); border: 1px solid rgba(233,30,99,0.3); padding: 8px; border-radius: 6px;">
<span style="font-size: 11px; color: #FF8DA1; font-weight: bold;">🎖️ 판정 등급: {card_info['title']}</span>
</div>
</div>
"""
                st.markdown(html_card_layout, unsafe_allow_html=True)
                
                st.write("")
                if missed_money > 0: st.error(f"🏅 **흑우 판정 코멘트**\n\n{card_info['desc']}")
                else: st.success(f"🏅 **판정 코멘트**\n\n{card_info['desc']}")

        # TAB 2: 사주 운세 (3번 기획 고도화: 매일 바뀌는 일진 연동)
        with tab2:
            st.markdown("### 🔮 생년월일 명리 기반 실시간 주식 일진(日辰) 진단")
            st.caption(f"📅 오늘 날짜 기운({datetime.date.today().strftime('%Y년 %m월 %d일')})을 실시간 해체하여 당일 매수운을 매칭합니다.")
            
            user_birth = st.text_input("🎂 생년월일 8자리를 입력하세요", max_chars=8, placeholder="19961025", key="saju_birth")
            stock_question = st.text_input("💬 오늘 진입할 주식 종목명", placeholder="예: 엔비디아", key="saju_stock")
            
            if st.button("☯️ 오늘의 일진 대운 오픈"):
                if len(user_birth) < 8 or not stock_question: st.error("🚨 생년월일 8자리와 종목명을 입력해야 점괘가 작동합니다!")
                else:
                    # 오늘 날짜값과 생년월일을 조합해 매일 변하는 동적 시드 생성
                    day_factor = int(datetime.date.today().strftime('%d'))
                    seed_num = (sum([int(char) for char in user_birth]) + day_factor) % 4
                    clean_stock = stock_question.strip()
                    
                    saju_responses = [
                        f"🔮 [오늘의 일진: ⚠️ 편재살 대치 / 비견 겁재 강세]\n\n오늘은 손가락에 급격한 도파민 충동 마귀가 끼는 날입니다. 지금 시점에 '{clean_stock}' 주문 넣었다간 외인/기관 형님들의 달콤한 설거지 밥이 될 뿐이니 원화 예수금을 소중히 숨기십시오.",
                        f"🔮 [오늘의 일진: ✨ 정재 귀인 합류 / 식신생재 활성화]\n\n귀하의 명리와 오늘 일진의 기운이 황금 합을 이룹니다. 소액이라도 흐린 눈 소비 아낀 돈으로 '{clean_stock}'을(를) 분할 적립하면 도파민이 황금 알로 변하는 역사적 기류를 타게 됩니다.",
                        f"🔮 [오늘의 일진: 🪨 토(土)기운 정체 / 문서운 하강]\n\n계좌를 지키는 관성 기운이 정체되었습니다. 오늘 사면 귀하가 산 가격이 정확히 3개월 동안 난공불락의 고점 벽이 될 수 있으니 매수 버튼에서 손 떼고 치킨이나 한 마리 시켜 드십시오.",
                        f"🔮 [오늘의 일진: 🌊 수(수)기운 유동 / 편인 대길 수혜]\n\n재물 창고 문이 가볍게 열리는 일진입니다. 지나친 의심을 거두고 '{clean_stock}'에 소신껏 분할 진입하는 것은 오늘 저녁 치킨 스킨 결제하는 것보다 500배 유용한 자산 액막이가 됩니다."
                    ]
                    st.info(saju_responses[seed_num])

        # TAB 3: 밸런스 게임 (무한 순환형 10종 리빌딩)
        with tab3:
            st.markdown("### ⚔️ 주주총회 자산 파괴 밸런스 의결방")
            
            g_idx = st.session_state["current_game_idx"]
            game_set = st.session_state["vote_data"][g_idx]
            
            st.markdown(f"**Q{g_idx+1}. {game_set['question']}**")
            
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                if st.button(f"🅰️ 선택 (Q{g_idx+1})", key=f"v_a_{g_idx}", use_container_width=True):
                    st.session_state["vote_data"][g_idx]["A"] += 1
                    st.session_state["current_game_idx"] = (g_idx + 1) % 10
                    st.rerun()
            with col_v2:
                if st.button(f"🅱️ 선택 (Q{g_idx+1})", key=f"v_b_{g_idx}", use_container_width=True):
                    st.session_state["vote_data"][g_idx]["B"] += 1
                    st.session_state["current_game_idx"] = (g_idx + 1) % 10
                    st.rerun()
                    
            total_votes = game_set["A"] + game_set["B"]
            per_A = (game_set["A"] / total_votes) * 100
            st.progress(int(per_A))
            st.caption(f"📊 Q{g_idx+1} 실시간 의결권 배틀 현황: 🅰️ {per_A:.1f}% vs 🅱️ {100-per_A:.1f}% (총 {total_votes}명 투표 완료)")
            
            if st.button("⏭️ 다음 밸런스 게임 패스하기", use_container_width=True):
                st.session_state["current_game_idx"] = (g_idx + 1) % 10
                st.rerun()

        # TAB 4: 포모 차단기 (지출 항목별 고유 정신승리 스펙)
        with tab4:
            st.markdown("### 🧠 뇌과학 기반 멘탈 세이프티 포모(FOMO) 차단기")
            st.write("주식 안 사고 시발비용으로 탕진한 나 자신에게 바치는 과학적 정신 승리 진단서")
            
            if st.session_state["current_audit"] is None:
                st.warning("💡 먼저 '📊 자산 타임머신' 탭에서 시뮬레이션을 한 번 돌리고 오셔야 정밀 뇌스캔이 작동합니다!")
            else:
                audit_data = st.session_state["current_audit"]
                habit_name = audit_data["habit"]
                asset_name = audit_data["asset"]
                base_seed = audit_data["seed"]
                
                st.info(f"🔍 **포모 스캔 연동:** '{habit_name}' 소비 ➡️ 대체 자산: '{asset_name}'")
                
                dopamine_score = int((base_seed / 10000) * 14) + 420
                cortisol_saved = int(dopamine_score * 7.8)
                hair_saved = int(base_seed / 220000) + 95
                
                # 지출 항목별 커스텀 뇌과학 분석 멘트 스위칭 로직
                CUSTOM_FOMO_MAP = {
                    "탕후루/마라탕 수명 단축 쿨타임": "마라탕의 캡사이신이 귀하의 전두엽 스트레스를 강제로 리셋시킨 덕분에, 하락장에서 매일 파란 불 보며 고통받았을 정신적 대미지를 훌륭히 방어했습니다.",
                    "스타벅스 바닐라라떼+디저트": "고카페인과 달콤한 디저트가 공급한 세로토닌 덕분에 아침 회의 부장님의 잔소리를 견뎌낼 수 있었으니, 주식 창 보며 불면증에 시달렸을 비용보다 훨씬 이득입니다.",
                    "올리브영 세일 '구경만' 가기": "화장품과 팩을 뜯으며 얻은 피부 진정 효과가 주식 고점에 물려 피가 거꾸로 솟구쳐 올랐을 급격한 노화 현상을 완벽하게 상쇄 방어했습니다.",
                    "불금 배달 엽떡+치킨 세트": "금요일 밤의 고독감과 업무 스트레스를 튀김 옷과 매운 양념으로 완벽 헷지했습니다. 주식 예수금으로 묵혀뒀으면 매일 폭락장 보며 위궤양 걸렸을 확률 98%입니다.",
                    "지그재그/W컨셉 충동 의류 매수": "새 옷을 입고 거울을 보며 얻은 외모 자존감이, 보유 주식 반토막 나서 주주 단톡방에서 눈물 흘리며 구걸하고 있었을 사회적 체면을 든든하게 사수했습니다.",
                    "매달 속눈썹 펌/네일 정기권": "손톱 위 파츠의 영롱한 시각적 도파민은 귀하의 좌뇌를 안정시켰습니다. 주식 매수한 뒤 차트 분봉 보며 손톱 물어뜯어 피 흘렸을 리스크를 완벽하게 차단했습니다."
                }
                
                default_fomo_text = f"주식 시장의 굶주린 세력 고래들에게 물려서 눈물 흘리느니, 귀하의 소중한 신체 위장과 시각적 행복에 100% 자율 기부한 귀하가 마인드셋 최종 승리자입니다."
                fomo_advice = CUSTOM_FOMO_MAP.get(habit_name, default_fomo_text)
                
                with st.container(border=True):
                    st.markdown(f"<center><b>🧠 귀하의 소비 행동에 따른 생체 이득 정산서</b></center>", unsafe_allow_html=True)
                    st.write("")
                    
                    m_c1, m_c2, m_c3 = st.columns(3)
                    with m_c1: st.metric(label="🔋 충전된 행복 도파민", value=f"{dopamine_score:,} pg/mL", delta="우울증 예방 완료")
                    with m_c2: st.metric(label="🛡️ 방어한 스트레스 (코르티솔)", value=f"{cortisol_saved:,} 🌟", delta="울화통 리스크 헷지")
                    with m_c3: st.metric(label="💇 사수한 모근(毛根) 개수", value=f"약 {hair_saved:,} 개", delta="하락장 탈모 방어 성공")
                    
                    st.write("---")
                    st.markdown(f"""
                    **💡 껄무새 도사의 최종 뇌과학 소견서**\n
                    만약 귀하가 탕진 지출 대신 진짜로 **'{asset_name}'** 주식을 매수했다면, 매일 오전 주식 창이 열릴 때마다 심장이 벌렁거리고 스트레스 코르티솔 수치가 수천 배 폭발하여 이미 **약 {hair_saved:,}개의 모근이 장렬히 탈모**되었을 것으로 추정됩니다.
                    
                    {fomo_advice}\n
                    결론적으로 내 멘탈을 우량주 수준으로 수호한 당신이 최종 위너입니다. 꺾이지 않는 소비(중꺾소) 나이스샷! 🚀
                    """)

    # ==================== [RIGHT SIDE] 우측 고정방 및 실제 인원 카운터 ====================
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
