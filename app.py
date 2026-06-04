import streamlit as st
import streamlit.components.v1 as components
import datetime
import random

# 1. 껄무새 다크모드 기반 최적화 설정
st.set_page_config(
    page_title="✨ 껄무새 - 2030 필수 자산 케어 v24", 
    page_icon="🦜",
    layout="wide"  # 와이드 레이아웃 유지
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

    st.markdown("""
        <div style="margin-bottom: 15px;">
            <span style="font-size: 38px; font-weight: 800; background: linear-gradient(45deg, #4285F4, #9B51E0, #E91E63); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px;">
                🦜 껄무새
            </span>
        </div>
    """, unsafe_allow_html=True)

    # 🛠️ [레이아웃 비율 초슬림 조정] 2.5대 0.8 구조로 대화방을 훨씬 작고 컴팩트하게 수정!
    main_layout, chat_layout = st.columns([2.5, 0.8], gap="medium")

    # ==================== [LEFT SIDE] 메인 기능 영역 ====================
    with main_layout:
        tab1, tab2, tab3 = st.tabs(["📊 자산 타임머신", "🔮 껄무새 사주도사", "⚔️ 주주총회 밸런스"])

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
                else:
                    habit_clean_name = selected_option.split(" (")[0]
                    unit_price = HABIT_PRICE_DICT[selected_option]

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
                            card_info = {"title": "🌱 시작은 달콤한 초보 탕진러", "desc": f"아직은 시드 규모가 작아 타격이 적어 보이죠? 하지만 무심코 긁어댄 '{habit_clean_name}' 비용이 미래 우량 자산 {asset_clean_name}의 레일 위에서 무럭무럭 손실 자산으로 자라나고 있습니다."}
                        elif total_seed <= 15000000:
                            card_info = {"title": "💸 월급 통장 슬레이어 대리", "desc": f"남들 주식 적립해서 미래 자산 불릴 때, 본이는 장바구니에 '{habit_clean_name}'을(를) 정성껏 적립해 통장을 야무지게 학살하셨습니다."}
                        elif total_seed <= 50000000:
                            card_info = {"title": "🚨 장바구니 풀소유 광기 야수", "desc": f"국산 중형차 한 대 뽑을 수준의 거금을 오직 '{habit_clean_name}' 하나에 꼴아박으며, 미래 통장 최종 잔고가 {int(future_value/10000):,}만 원으로 뻥튀기될 역사적 찬스를 걷어차셨습니다."}
                        else:
                            card_info = {"title": "👑 자산 파괴 자비에 교수", "desc": f"존경합니다 인간 지표 끝판왕이시여. 억 단위의 기회비용을 오직 본인의 영혼이 담긴 '{habit_clean_name}' 지출 명목으로 시장에 전부 기부하셨습니다."}
                    else:
                        custom_cards = {
                            "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": {"title": "🩸 혈당 폭발 마라탕 중독자", "desc": "마라 국물과 설탕 코팅에 영혼을 저당 잡아 혈당을 올리는 사이, 본인의 시드머니는 주식 시장에서 완전히 녹아내리게 방치한 위대한 푸드 파이터"},
                            "스타벅스 바닐라라떼+디저트 (1회 11,000원)": {"title": "☕ 사이렌 오더 기부 천사", "desc": "매달 스타벅스 별사냥과 고카페인 시럽에 취해 살며 스타벅스 코리아 매출 상승에는 기여했으나 정작 본인 계좌는 공황 상태에 빠뜨린 주주"},
                            "올리브영 세일 '구경만' 가기 (1회 45,000원)": {"title": "💄 올리브영 탕진 잼 마스터", "desc": "세일 문자만 오면 '구경만 해야지' 하고 들어가 틴트와 팩으로 바구니를 채우며 CJ 올리브영 시총 방어에 본인 시드를 갈아 넣은 VVIP 흑우"},
                            "불금 배달 엽떡+치킨 세트 (1회 32,000원)": {"title": "🐔 배달 앱 다이아몬드 등급", "desc": "금요일 밤의 고독과 스트레스를 캡사이신과 튀김 옷으로 위로하느라, 통장에 억 단위 자산이 쌓일 기회를 아주 야무지게 씹어 삼키신 야식 마스터"},
                            "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": {"title": "👗 새벽 배송 폰결제 야수", "desc": "침대에 누워 흐린 눈으로 옷 구경하다 네이버페 6자리를 광속으로 태우며, 방구석 드레스룸은 채웠으나 자산 포트폴리오는 전라로 만든 패셔니스타"},
                            "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": {"title": "💅 손끝 발끝 풀소유 영애", "desc": "손톱 위에 파츠를 올리고 눈썹을 바짝 끌어올려 비주얼 품격은 유지했으나, 정작 본인 자산 성장률은 바닥에 바짝 붙여버린 관리의 대가"}
                        }
                        card_info = custom_cards.get(selected_option, {"title": "🛍️ 프로 탕진러", "desc": "지출로 도파민을 채우며 우량주 투자 타이밍을 놓치신 직장인 명예 주주"})
                else:
                    card_info = {"title": "🛡️ 자산 수호 헷지 명인", "desc": "폭락 사이클을 예리한 자산 우회 방어로 피해 가며 내 통장의 순수 가치를 사수해 낸 위대한 금융 트레이더"}

                # 실시간 오픈 대화방 연동용 세션 저장
                st.session_state["current_audit"] = {
                    "habit": habit_clean_name,
                    "asset": asset_clean_name,
                    "future_val": f"{int(future_value):,} 원",
                    "grade": card_info["title"]
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
                with st.container(border=True):
                    st.markdown(f"<center><span style='font-family: sans-serif; font-size: 13px; font-weight: bold; letter-spacing: 2px; color: #9B51E0;'>📊 MY SHIBAL COST REPORT</span></center>", unsafe_allow_html=True)
                    st.markdown(f"<center><h2 style='font-family: sans-serif; font-size: 26px; font-weight: 800; color: #FFFFFF; margin: 10px 0;'>\"{habit_clean_name}\"</h2></center>", unsafe_allow_html=True)
                    st.caption(f"<center>참고 {asset_clean_name} 매수하고 미래로 {years}년 직진했다면?</center>", unsafe_allow_html=True)
                    st.write("")
                    sub_c1, sub_c2 = st.columns(2)
                    with sub_c1: st.metric(label="💸 사라진 내 원금", value=f"{int(total_seed):,} 원")
                    with sub_c2: st.metric(label="🔮 미래 최종 잔고 예측", value=f"{int(future_value):,} 원")
                    st.write("")
                    if missed_money > 0: st.error(f"🏅 **흑우 판정 등급: {card_info['title']}**\n\n{card_info['desc']}")
                    else: st.success(f"🏅 **판정 등급: {card_info['title']}**\n\n{card_info['desc']}")

        # TAB 2: 사주 운세
        with tab2:
            st.markdown("### 🔮 생년월일 명리 기반 주식 매수 타이밍 진단")
            user_birth = st.text_input("🎂 생년월일 8자리를 입력하세요 (예: 19961025)", max_chars=8, placeholder="19950714", key="saju_birth")
            stock_question = st.text_input("💬 주식 질문을 던지세요", placeholder="예: 삼성전자 오늘 사도 될까요?", key="saju_stock")
            
            if st.button("☯️ 사주 연동 점괘 받기"):
                if len(user_birth) < 8 or not stock_question: st.error("🚨 생년월일 8자리와 질문을 채워라 휴먼!")
                else:
                    seed_num = sum([int(char) for char in user_birth]) % 4
                    clean_stock = stock_question.replace("사도 될까요", "").replace("사도 됨", "").strip()
                    saju_responses = [
                        f"🔮 점괘 결과: [🔥 화(火)기운 과다 / 편재살 대치]\n\n오늘 손가락에 급격한 충동 매수 마귀가 꼈습니다. '{clean_stock}'(으)로 대박 노리다간 고점에 처물리기 딱 좋습니다. 지갑 닫으십시오.",
                        f"🔮 점괘 결과: [🌱 목(木)기운 보존 / 정재 귀인 합류]\n\n사주에 재물창고를 채우는 대길의 운이 흐릅니다. '{clean_stock}'을(를) 오늘 쪼개서 진입하는 것은 도파민을 황금알로 바꾸는 전략입니다.",
                        f"🔮 점괘 결과: [🪨 토(土)기운 정체 / 겁재살 강세]\n\n내 돈을 강탈하는 겁재살이 강합니다. 지금 '{clean_stock}' 주문을 넣으면 외인과 기관의 밥이 될 뿐이니 치킨이나 한마리 시켜 드십시오.",
                        f"🔮 점괘 결과: [🌊 수(水)기운 유동 / 식신생재 활성화]\n\n돈복이 물밀듯 밀려옵니다. 의심을 거두고 '{clean_stock}'에 소신껏 진입하는 것은 매우 훌륭한 자산 액막이가 될 것입니다."
                    ]
                    st.info(saju_responses[seed_num])

        # TAB 3: 밸런스 게임
        with tab3:
            st.markdown("### ⚔️ 주주총회 자산 파괴 밸런스 게임")
            st.write("**Q. 평생 동안 다음 중 딱 하나의 상황만 선택해야 한다면?**")
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                if st.button("🅰️ 평생 배달 야식+스타벅스 완전히 끊고, 그 돈 전액 엔비디아 적립식 풀매수", key="v_a"): st.session_state["vote_data"]["A"] += 1; st.rerun()
            with col_v2:
                if st.button("🅱️ 평생 패션/올영 전면 금지당하는 대신 고점 물린 삼전 원금 강제 회복", key="v_b"): st.session_state["vote_data"]["B"] += 1; st.rerun()
            total_votes = st.session_state["vote_data"]["A"] + st.session_state["vote_data"]["B"]
            per_A = (st.session_state["vote_data"]["A"] / total_votes) * 100
            st.progress(int(per_A))
            st.caption(f"📊 주주 배틀 현황: 🅰️ {per_A:.1f}% vs 🅱️ {100-per_A:.1f}% (총 {total_votes}명 의결권 행사)")

    # ==================== 🛠️ [RIGHT SIDE] 초슬림&컴팩트 미니 대화방 위젯 ====================
    with chat_layout:
        st.markdown("<h3 style='margin-top:23px; font-size:16px;'>💬 실시간 오픈방</h3>", unsafe_allow_html=True)
        
        # 👑 등급 인증 연동 모듈 크기도 작게 압축
        if st.session_state["current_audit"] is not None:
            audit = st.session_state["current_audit"]
            st.caption(f"🏅 **내 등급:** {audit['grade']}")
            if st.button("👑 내 등급 바로 인증", use_container_width=True):
                cert_text = f"🚨 [흑우인증] 탕진: '{audit['habit']}' ➡️ '{audit['asset']}' 에 박았으면 미래 잔고 **{audit['future_val']}** 뚫었음; 등급: [{audit['grade']}]"
                st.session_state["chat_messages"].append({"role": "user", "name": f"인증러_{random.randint(100,999)}", "text": cert_text})
                st.session_state["current_audit"] = None
                st.toast("✅ 인증 완료!", icon="🔥")
                st.rerun()

        # 대화 피드 높이도 550 ➡️ 450으로 콤팩트하게 줄여서 우측 사이드에 귀엽게 밀착!
        chat_container = st.container(height=450)
        with chat_container:
            for msg in st.session_state["chat_messages"]:
                is_cert = "[흑우인증]" in msg["text"]
                avatar_icon = "👑" if is_cert else "🦜"
                with st.chat_message(msg["role"], avatar=avatar_icon):
                    st.markdown(f"**{msg['name']}**")
                    if is_cert: st.caption(msg["text"]) # 인증 메시지도 슬림하게 캡션 처리
                    else: st.write(msg["text"])

        # 입력 창
        if user_live_input := st.chat_input("한탄하기..."):
            st.session_state["chat_messages"].append({"role": "user", "name": f"익명_{random.randint(100,999)}", "text": user_live_input})
            st.rerun()
