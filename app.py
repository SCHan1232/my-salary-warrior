import streamlit as st
import streamlit.components.v1 as components
import datetime
import random

# 1. 껄무새 다크모드 기반 최적화 설정
st.set_page_config(
    page_title="✨ 껄무새 - 2030 필수 자산 케어 v18", 
    page_icon="🦜",
    layout="centered" 
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
if "chat_log" not in st.session_state:
    st.session_state["chat_log"] = [
        "익명루팡: 마라탕이랑 스벅 끊었으면 이미 해외여행 비즈니스 탔음..", 
        "서학개미: 구글 모으는 게 인생 최고 개이득",
        "껄껄: 테슬라 3년 전에 샀어야 했는데 껄껄껄..."
    ]
if "vote_data" not in st.session_state:
    st.session_state["vote_data"] = {"A": 245, "B": 198}

# 🔴 AREA A: 부장님 방어막
if is_boss_mode:
    st.error("🔒 [보안] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026_전사_리소스_최적화_KPI_Data")
    st.dataframe({"Index": [1, 2], "Task": ["Next-Gen ERP 구축", "Data Pipeline v3"], "Progress": ["94.2%", "81.2%"]}, use_container_width=True)
    if st.button("🔄 시스템 세션 새로고침"): st.query_params["boss_mode"] = "false"; st.rerun()

# 🟢 AREA B: 껄무새 놀이터
else:
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

    st.markdown("""
        <div style="margin-bottom: 5px;">
            <span style="font-size: 38px; font-weight: 800; background: linear-gradient(45deg, #4285F4, #9B51E0, #E91E63); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px;">
                🦜 껄무새
            </span>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 자산 타임머신", "🔮 껄무새 사주도사", "⚔️ 주주총회 밸런스"])

    # ==================== TAB 1: 메인 시뮬레이터 탭 ====================
    with tab1:
        st.markdown("<p style='color: #AAADB0; font-size: 14px; margin-bottom: 20px;'>내 탕진 비용의 스노우볼을 역산하고 미래 퀀텀점프 자산을 예측합니다.</p>", unsafe_allow_html=True)
        
        with st.form("gemini_form"):
            col1, col2 = st.columns(2)
            with col1:
                habit = st.selectbox("🛍️ 매달 '흐린 눈'으로 지출 중인 항목", list(HABIT_PRICE_DICT.keys()))
                count = st.slider("📊 주간 평균 소비 빈도", 1, 14, 3)
            with col2:
                target_asset = st.selectbox("📈 연동할 목적 자산", list(HISTORICAL_STOCK_DATA.keys()))
                years = st.slider("⏳ 타임머신 추적 기간 (년)", 1, 5, 3)
            submitted = st.form_submit_button("✨ 껄무새 엔진 가동 (Enter)")

        if submitted:
            unit_price = HABIT_PRICE_DICT[habit]
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

            max_idx = min(years, len(prices_history) - 1)
            then_price = prices_history[max_idx]
            total_asset_growth = ((current_price - then_price) / then_price) * 100
            
            growth_multiplier = current_price / then_price
            future_value = final_value * growth_multiplier

            # 0. 데이터 검증 리포트
            st.write("---")
            st.markdown(f"<h3 style='color: #FFFFFF; font-size: 17px;'>🔍 0. 데이터 신뢰성 검증 리포트</h3>", unsafe_allow_html=True)
            val_col1, val_col2 = st.columns(2)
            with val_col1:
                display_then = f"{then_price:,} 원" if not is_foreign else f"${then_price:,} (원화 약 {int(then_price*exchange_rate):,} 원)"
                st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 15px; border-radius: 8px; background-color: #1A1D20;"><div style="font-size: 11px; color: #AAADB0;">⏳ {max_idx}년 전 실제 당일 가격</div><div style="font-size: 17px; font-weight: 600; color: #F28B82; margin-top: 5px;">{display_then}</div></div>""", unsafe_allow_html=True)
            with val_col2:
                display_now = f"{current_price:,} 원" if not is_foreign else f"${current_price:,} (원화 약 {int(current_price*exchange_rate):,} 원)"
                st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 15px; border-radius: 8px; background-color: #1A1D20;"><div style="font-size: 11px; color: #81C995;">✨ 현재 실시간 시세</div><div style="font-size: 17px; font-weight: 600; color: #81C995; margin-top: 5px;">{display_now}</div><div style="font-size: 11px; color: #FFFFFF; margin-top: 3px; font-weight: bold;">📊 {max_idx}년 간 순수 누적 수익률: {total_asset_growth:+.2f}%</div></div>""", unsafe_allow_html=True)

            # 🛠️ [리팩토링] 1. 인스타 스토리 전용 올인원 캡처 팩 (오류 유발 구문 완전 삭제 및 등급 통합)
            st.write("---")
            st.markdown("### 📸 1. 인스타 스토리 박제용 캡처 카드 (여기만 스크린샷 하세요!)")
            
            habit_clean_name = habit.split(" (")[0]
            asset_clean_name = target_asset.split(" (")[0]

            # 등급 데이터 사전 매핑
            if missed_money > 0:
                custom_cards = {
                    "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": {"title": "🩸 혈당 폭발 마라탕 중독자", "desc": "마라 국물과 설탕 코팅에 영혼을 저당 잡아 혈당을 올리는 사이, 본인의 시드머니는 주식 시장에서 완전히 녹아내리게 방치한 위대한 푸드 파이터"},
                    "스타벅스 바닐라라떼+디저트 (1회 11,000원)": {"title": "☕ 사이렌 오더 기부 천사", "desc": "매달 스타벅스 별사냥과 고카페인 시럽에 취해 살며 스타벅스 코리아 매출 상승에는 기여했으나 정작 본인 계좌는 공황 상태에 빠뜨린 주주"},
                    "올리브영 세일 '구경만' 가기 (1회 45,000원)": {"title": "💄 올리브영 탕진 잼 마스터", "desc": "세일 문자만 오면 '구경만 해야지' 하고 들어가 틴트와 팩으로 바구니를 채우며 CJ 올리브영 시총 방어에 본인 시드를 갈아 넣은 VVIP 흑우"},
                    "불금 배달 엽떡+치킨 세트 (1회 32,000원)": {"title": "🐔 배달 앱 다이아몬드 등급", "desc": "금요일 밤의 고독과 스트레스를 캡사이신과 튀김 옷으로 위로하느라, 통장에 억 단위 자산이 쌓일 기회를 아주 야무지게 씹어 삼키신 야식 마스터"},
                    "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": {"title": "👗 새벽 배송 폰결제 야수", "desc": "침대에 누워 흐린 눈으로 옷 구경하다 네이버페이 6자리를 광속으로 태우며, 방구석 드레스룸은 채웠으나 자산 포트폴리오는 전라로 만든 패셔니스타"},
                    "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": {"title": "💅 손끝 발끝 풀소유 영애", "desc": "손톱 위에 파츠를 올리고 눈썹을 바짝 끌어올려 비주얼 품격은 유지했으나, 정작 본인 자산 성장률은 바닥에 바짝 붙여버린 관리의 대가"},
                    "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": {"title": "🥃 고독한 오크통 주주", "desc": "피트 향 머금은 싱글몰트로 오늘 하루의 서러움을 녹이려다 통장 잔고까지 완벽하게 증발시켜 미장 빅테크 주주들의 기쁨이 되어주신 알코올 요정"},
                    "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": {"title": "🎮 데이터 쪼가리 풀소유 야수", "desc": "모니터 속 전설 스킨과 가챠 연출의 도파민에 취해 클릭 몇 번으로 실제 집 한 채 살 돈을 게임 서버 유지비로 쾌척해 버린 명예 야수"},
                    "주말 골프 연습장/필드 호사 (1회 120,000원)": {"title": "⛳ 잔디밭 지출의 나이스샷", "desc": "굿샷을 외치며 그린 위에서 호사를 누리는 동안 정작 본인 주식 자산 포트폴리오는 OB 구역 숲속으로 완벽하게 날려버린 필드의 타이거 흑우"},
                    "기념일 에피타이저 오마카세 (1회 150,000원)": {"title": "🍣 럭셔리 파인다이닝 영애", "desc": "셰프의 친절한 설명을 들으며 입안의 사치를 즐기는 순간, 내 통장 잔고는 엔비디아의 성장 에너지를 먹지 못해 원자 단위로 굶주려가던 모순의 극치"},
                    "체형 교정 명목 필라테스 (1회 60,000원)": {"title": "🧘 기구 위에서 비명지르는 영애", "desc": "코어 근육을 단단하게 잡아내어 척추 정렬에는 성공했으나, 정작 미래 내 집 마련을 위한 자산의 척추는 완벽하게 무너뜨린 관리의 모순"},
                    "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": {"title": "⚽ 방구석 올드 트래포드 구단주", "desc": "해외 축구 구단의 엠블럼 패치를 보며 밤마다 열광했으나, 정작 본인 자산 리그는 4부 리그 강등권에서 처참하게 헤매게 만든 유니폼 수집가"}
                }
                card_info = custom_cards.get(habit, {"title": "🛍️ 프로 시발비용러", "desc": "소소한 지출로 도파민을 채우며 미래 자산 퀀텀점프의 기회를 쿨하게 걷어차신 직장인 영애/대리"})
            else:
                card_info = {"title": "🛡️ 자산 수호 헷지 명인", "desc": "폭락 사이클을 영리한 탕진 소비로 우회 방어해 낸 금융 위기관리의 천재"}

            # HTML 꼬임 방지를 위해 완벽히 검증된 Streamlit 네이티브 외곽선 연출 및 메트릭 패키징
            with st.container(border=True):
                st.markdown(f"<center><b>🦜 GGUL-MUSAET AUDIT REPORT</b></center>", unsafe_allow_html=True)
                st.markdown(f"<center><h3 style='margin:10px 0;'>\"{habit_clean_name}\"</h3></center>", unsafe_allow_html=True)
                st.caption(f"<center>참고 {asset_clean_name} 매수하고 미래로 {years}년 직진했다면?</center>", unsafe_allow_html=True)
                st.write("")
                
                # 아기자기하고 보기 좋게 숫자를 배치
                sub_col1, sub_col2 = st.columns(2)
                with sub_col1:
                    st.metric(label="💸 사라진 내 원금", value=f"{int(total_seed):,} 원")
                with sub_col2:
                    st.metric(label="🔮 미래 최종 잔고 예측", value=f"{int(future_value):,} 원")
                
                st.write("")
                # 등급과 일침 한탄 멘트를 카드 안으로 완전 병합!
                if missed_money > 0:
                    st.error(f"🏅 **흑우 판정 등급: {card_info['title']}**\n\n{card_info['desc']}")
                else:
                    st.success(f"🏅 **판정 등급: {card_info['title']}**\n\n{card_info['desc']}")
                
                st.caption("<center>📸 스마트폰 화면을 이 카드 크기에 맞춰 캡처 후 인스타 스토리에 올리세요!</center>", unsafe_allow_html=True)

            # 2. 하단 상세 브리핑 브레이크다운
            st.write("")
            st.markdown("<h3 style='color: #FFFFFF; font-size: 17px;'>📊 2. 과거 데이터 기반 세부 실시간 정산</h3>", unsafe_allow_html=True)
            res_col1, res_col2, res_col3 = st.columns(3)
            with res_col1: st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: #AAADB0; font-weight: 500;">🪙 총 지출 매몰 원금</div><div style="font-size: 22px; font-weight: 600; color: #FFFFFF; margin-top: 5px;">{int(total_seed):,} 원</div></div>""", unsafe_allow_html=True)
            with res_col2: st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: #81C995; font-weight: 500;">📈 현재 자산 가치 (오늘)</div><div style="font-size: 22px; font-weight: 600; color: #81C995; margin-top: 5px;">{int(final_value):,} 원</div></div>""", unsafe_allow_html=True)
            with res_col3:
                card_color = "#F28B82" if missed_money > 0 else "#8AB4F8"
                status_text = "🚨 기회상실 순손실액" if missed_money > 0 else "🛡️ 리스크 최종 방어액"
                st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: {card_color}; font-weight: 500;">{status_text}</div><div style="font-size: 22px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div></div>""", unsafe_allow_html=True)

        # 3. 실시간 방명록 한탄방
        st.write("---")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 17px;'>💬 실시간 월급루팡 익명 한탄방</h3>", unsafe_allow_html=True)
        user_comment = st.text_input("💬 한마디 남기기 (Enter 입력 시 등록)", placeholder="예: 위스키 마실 돈 모았으면 이미 테슬라 몰고 대리 불렀지..")
        if user_comment:
            st.session_state["chat_log"].insert(0, f"익명루팡_{random.randint(100,999)}: {user_comment}")
            st.rerun()
        chat_box_html = "<div style='background-color: #1E1F20; border: 1px solid #3C4043; padding: 15px; border-radius: 8px; max-height: 150px; overflow-y: auto; color: #FFFFFF; font-family: monospace; font-size: 12.5px; line-height: 1.6;'>"
        for log in st.session_state["chat_log"]: chat_box_html += f"<div>{log}</div>"
        chat_box_html += "</div>"
        st.markdown(chat_box_html, unsafe_allow_html=True)

    # ==================== TAB 2: 사주 명리 껄무새 도사 탭 ====================
    with tab2:
        st.markdown("### 🔮 생년월일 명리 기반 주식 매수 타이밍 진단")
        st.write("8자리 생년월일 기운을 오행으로 분해하여, 질문하신 주식 종목의 진입 적절성을 사주학적으로 감정합니다.")
        
        user_birth = st.text_input("🎂 생년월일 8자리를 입력하세요 (예: 19961025)", max_chars=8, placeholder="19950714")
        stock_question = st.text_input("💬 주식 질문을 던지세요", placeholder="예: 삼성전자 오늘 사도 될까요?")
        
        if st.button("☯️ 껄무새 도사에게 사주 연동 점괘 받기"):
            if len(user_birth) < 8 or not user_birth.isdigit():
                st.error("🚨 생년월일 8자리를 정확히 숫자로만 입력해라 휴먼!")
            elif not stock_question:
                st.error("🚨 어떤 주식을 살지 질문을 적어야 도사님이 일침을 주지!")
            else:
                seed_num = sum([int(char) for char in user_birth]) % 4
                clean_stock = stock_question.replace("사도 될까요", "").replace("사도 됨", "").replace("지금", "").strip()
                
                saju_responses = [
                    f"🔮 점괘 결과: [🔥 화(火)기운 과다 / 편재살 대치]\n\n귀하의 생년월일 기운상 오늘 손가락에 급격한 충동 매수 마귀가 꼈습니다. '{clean_stock}'(으)로 일확천금을 노리려는 야수의 심장은 고점에 처물리기 딱 좋은 운세입니다. 관재구설과 계좌 소멸 살이 보입니다. 오늘은 매수 버튼에서 손을 때고 조용히 자중하십시오.",
                    f"🔮 점괘 결과: [🌱 목(木)기운 보존 / 정재 귀인 합류]\n\n사주에 따박따박 창고를 채우는 財庫(재고) 귀인의 기운이 가득합니다. '{clean_stock}'을(를) 오늘 분할 적립식으로 진입하는 것은 장기적으로 마라탕 그릇을 황금알로 바꾸는 신의 한 수가 될 상입니다. 다만 일시적 횡보는 인내하셔야 문이 열립니다.",
                    f"🔮 점괘 결과: [🪨 토(土)기운 정체 / 겁재살 강세]\n\n지갑에 구멍이 뚫려 재물이 강탈당하는 겁재의 살이 도사리고 있습니다. 지금 흥분해서 '{clean_stock}' 매수 주문을 넣으면, 기관 및 외국인 세력에게 귀하의 소중한 월급 루팡 시드를 고스란히 헌납하는 형국이 됩니다. 금융 치료를 당하기 싫다면 오늘 밤 야식이나 배달 시켜 드시는 게 리스크 헷지입니다.",
                    f"🔮 점괘 결과: [🌊 수(水)기운 유동 / 식신생재 활성화]\n\n재물이 샘물처럼 흘러 들어와 자산 전략과 합을 이루는 대길의 기운입니다. 의심을 거두고 '{clean_stock}'에 진입하는 것은 도파민을 가치 있는 자산으로 치환하는 훌륭한 액막이가 될 것입니다. 과감하게 야수의 본능을 깨워 시뮬레이션을 밀어붙이십시오."
                ]
                st.info(saju_responses[seed_num])

    # ==================== TAB 3: 주식 결합형 자산 파괴 밸런스 게임 탭 ====================
    with tab3:
        st.markdown("### ⚔️ 주주총회 자산 파괴 밸런스 게임")
        st.write("2030 영애·대리들의 계좌와 멘탈을 가장 완벽하게 도려내는 극한의 밸런스 매치업입니다.")
        st.write("**Q. 평생 동안 다음 중 딱 하나의 상황만 선택하여 살아갈 수 있다면?**")
        
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            if st.button("🅰️ 평생 배달 엽떡+치킨+스벅 싹 다 끊고, 그 돈 전액 엔비디아 무지성 적립하기", key="btn_vote_a"):
                st.session_state["vote_data"]["A"] += 1
                st.rerun()
        with col_v2:
            if st.button("🅱️ 평생 올리브영/쇼핑 금지당하는 대신, 고점에 물려 -70% 토막 난 삼성전자 원금 회복되기", key="btn_vote_b"):
                st.session_state["vote_data"]["B"] += 1
                st.rerun()
                
        total_votes = st.session_state["vote_data"]["A"] + st.session_state["vote_data"]["B"]
        per_A = (st.session_state["vote_data"]["A"] / total_votes) * 100
        per_B = (st.session_state["vote_data"]["B"] / total_votes) * 100
        
        st.write("")
        st.progress(int(per_A))
        st.caption(f"📊 실시간 주주총회 의결 현황: 🅰️ {per_A:.1f}% vs 🅱️ {per_B:.1f}% (총 {total_votes}명 키보드 배틀 중)")
