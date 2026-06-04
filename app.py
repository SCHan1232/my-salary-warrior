import streamlit as st
import streamlit.components.v1 as components
import datetime
import random

# 1. 제미나이 다크모드 기반 최적화 설정
st.set_page_config(
    page_title="✨ 껄무새 - 자산 최적화 시뮬레이션 v16", 
    page_icon="🦜",
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

# 익명 방명록 및 투표 세션 데이터 유지 설정
if "chat_log" not in st.session_state:
    st.session_state["chat_log"] = [
        "익명루팡: 마라탕이랑 스벅 끊었으면 이미 해외여행 비즈니스 탔음..", 
        "서학개미: 구글 모으는 게 인생 최고 개이득",
        "껄껄: 테슬라 3년 전에 샀어야 했는데 껄껄껄..."
    ]
if "vote_data" not in st.session_state:
    st.session_state["vote_data"] = {"A": 142, "B": 98}

# 🔴 AREA A: 부장님 방어막
if is_boss_mode:
    st.error("🔒 [보안] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026_전사_리소스_최적화_KPI_Data")
    st.dataframe({"Index": [1, 2], "Task": ["Next-Gen ERP 구축", "Data Pipeline v3"], "Progress": ["94.2%", "81.2%"]}, use_container_width=True)
    if st.button("🔄 시스템 세션 새로고침"): st.query_params["boss_mode"] = "false"; st.rerun()

# 🟢 AREA B: 껄무새 팩폭 놀이터
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

    # 껄무새 시그니처 상단 로고 디자인
    st.markdown("""
        <div style="margin-bottom: 5px;">
            <span style="font-size: 38px; font-weight: 800; background: linear-gradient(45deg, #4285F4, #9B51E0, #E91E63); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1px;">
                🦜 껄무새
            </span>
        </div>
    """, unsafe_allow_html=True)

    # 🛠️ [핵심 인프라 개조] 상단 메뉴 탭(Menu Tabs) 시스템 전면 배정!
    tab1, tab2, tab3 = st.tabs(["📊 자산 타임머신", "🔮 오늘의 사주 운세", "⚔️ 주주총회 밸런스"])

    # ==================== TAB 1: 메인 시뮬레이터 탭 ====================
    with tab1:
        st.markdown("<p style='color: #AAADB0; font-size: 14.5px; margin-bottom: 20px;'>그때 살 걸... 귀하의 흐린 눈 지출을 추적해 자산 최적화 대안을 제시합니다.</p>", unsafe_allow_html=True)
        
        # 오늘의 시발비용 추천 기믹을 타임머신 폼 상단에 배치
        with st.expander("🎰 오늘 스트레스 만빵인데 주식 살까? 지를까? (랜덤 가이드)"):
            if st.button("🎁 탕진 여부 판정받기"):
                random_items = [
                    "오늘은 장세가 흉흉합니다. 주식 사서 물릴 바엔 퇴근길에 마라탕에 꿔바로우(28,000원) 풀코스로 조지십시오.",
                    "미국 빅테크가 숨고르기 중입니다. 무리한 진입보다는 올리브영에 가서 평소 갖고 싶던 향수(45,000원)를 결제해 자산을 헷지하세요.",
                    "국장 거래대금이 처참합니다. 네이버페이 켜고 지그재그에서 옷 한 벌(65,000원) 시원하게 지르는 게 멘탈 건강에 개이득입니다.",
                    "오늘은 야수의 심장이 굳어가는 날. 배달 앱 켜서 엽떡에 허니콤보 세트(32,000원) 땡기고 꿀잠 자는 게 진정한 금융 치료입니다."
                ]
                st.success(random.choice(random_items))

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

            # 0. 데이터 신뢰성 검증 리포트
            st.write("---")
            st.markdown(f"<h3 style='color: #FFFFFF; font-size: 18px;'>🔍 0. 데이터 신뢰성 검증 리포트 ({target_asset.split(' (')[0]})</h3>", unsafe_allow_html=True)
            val_col1, val_col2 = st.columns(2)
            with val_col1:
                display_then = f"{then_price:,} 원" if not is_foreign else f"${then_price:,} (원화 약 {int(then_price*exchange_rate):,} 원)"
                st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 15px; border-radius: 8px; background-color: #1A1D20;"><div style="font-size: 11px; color: #AAADB0;">⏳ {max_idx}년 전 실제 당일 가격</div><div style="font-size: 18px; font-weight: 600; color: #F28B82; margin-top: 5px;">{display_then}</div></div>""", unsafe_allow_html=True)
            with val_col2:
                display_now = f"{current_price:,} 원" if not is_foreign else f"${current_price:,} (원화 약 {int(current_price*exchange_rate):,} 원)"
                st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 15px; border-radius: 8px; background-color: #1A1D20;"><div style="font-size: 11px; color: #81C995;">✨ 현재 실시간 시세</div><div style="font-size: 18px; font-weight: 600; color: #81C995; margin-top: 5px;">{display_now}</div><div style="font-size: 11px; color: #FFFFFF; margin-top: 3px; font-weight: bold;">📊 {max_idx}년 간 순수 누적 수익률: {total_asset_growth:+.2f}%</div></div>""", unsafe_allow_html=True)

            # 1. 과거 데이터 기반 실시간 정산
            st.write("")
            st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>📊 1. 과거 데이터 기반 실시간 정산</h3>", unsafe_allow_html=True)
            res_col1, res_col2, res_col3 = st.columns(3)
            with res_col1: st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: #AAADB0; font-weight: 500;">🪙 총 지출 매몰 원금</div><div style="font-size: 22px; font-weight: 600; color: #FFFFFF; margin-top: 5px;">{int(total_seed):,} 원</div></div>""", unsafe_allow_html=True)
            with res_col2: st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: #81C995; font-weight: 500;">📈 현재 자산 가치 (오늘)</div><div style="font-size: 22px; font-weight: 600; color: #81C995; margin-top: 5px;">{int(final_value):,} 원</div></div>""", unsafe_allow_html=True)
            with res_col3:
                card_color = "#F28B82" if missed_money > 0 else "#8AB4F8"
                status_text = "🚨 기회상실 순손실액" if missed_money > 0 else "🛡️ 리스크 최종 방어액"
                st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: {card_color}; font-weight: 500;">{status_text}</div><div style="font-size: 22px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div></div>""", unsafe_allow_html=True)

            # 2. 미래 퀀텀점프 예측
            st.write("")
            st.markdown(f"<h3 style='color: #FFFFFF; font-size: 18px;'>🔮 2. 미래 {years}년 뒤 자산 행복회로 퀀텀점프 예측</h3>", unsafe_allow_html=True)
            fut_col1, fut_col2 = st.columns(2)
            with fut_col1: st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;"><div style="font-size: 12px; color: #D6BCFA; font-weight: 500;">🚀 미래 엔진에 투영된 과거 에너모멘텀</div><div style="font-size: 24px; font-weight: 600; color: #D6BCFA; margin-top: 5px;">{total_asset_growth:+.2f} % 직진 반영</div></div>""", unsafe_allow_html=True)
            with fut_col2: st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;"><div style="font-size: 12px; color: #FFD700; font-weight: 500;">💰 미래 {years}년 뒤 최종 잔고 예측</div><div style="font-size: 24px; font-weight: 600; color: #FFD700; margin-top: 5px;">{int(future_value):,} 원</div></div>""", unsafe_allow_html=True)

            # 3. 인스타 박제용 영수증 UI
            st.write("")
            st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>🧾 3. 인스타 박제용 시발비용 매몰 영수증 (화면 캡처)</h3>", unsafe_allow_html=True)
            habit_clean_name = habit.split(" (")[0]
            asset_clean_name = target_asset.split(" (")[0]
            
            st.markdown(f"""
                <div style="background-color: #FFFFFF; color: #111111; font-family: 'Courier New', Courier, monospace; padding: 25px; border-radius: 4px; max-width: 420px; margin: 0 auto; box-shadow: 0 4px 10px rgba(0,0,0,0.5); border-top: 8px dashed #E91E63;">
                    <center>
                        <h2 style="margin: 0; color: #111111; font-size: 22px; font-weight: bold; letter-spacing: 2px;">★ SHIBAL RECEIPTS ★</h2>
                        <p style="font-size: 11px; margin: 5px 0; color: #666;">2026-06-04 CORP AUDIT REPORT</p>
                        <p style="margin: 0;">-----------------------------------------</p>
                    </center>
                    <div style="font-size: 13px; line-height: 1.6; margin: 10px 0;">
                        <div style="display: flex; justify-content: space-between;"><span>지출 항목:</span><b>[{habit_clean_name}]</b></div>
                        <div style="display: flex; justify-content: space-between;"><span>주간 지출 빈도:</span><b>주 {count} 회</b></div>
                        <div style="display: flex; justify-content: space-between;"><span>타임머신 연한:</span><b>지난 {years} 년간 적립</b></div>
                        <div style="display: flex; justify-content: space-between;"><span>대체 매수 자산:</span><b>{asset_clean_name}</b></div>
                    </div>
                    <p style="margin: 0;">-----------------------------------------</p>
                    <div style="font-size: 14px; font-weight: bold; margin: 12px 0;">
                        <div style="display: flex; justify-content: space-between; color: #E91E63;"><span>[1] 길바닥 매몰 원금:</span><span>{int(total_seed):,} 원</span></div>
                        <div style="display: flex; justify-content: space-between; color: #2E7D32;"><span>[2] 오늘 기준 자산 가치:</span><span>{int(final_value):,} 원</span></div>
                        <div style="display: flex; justify-content: space-between; color: #1565C0;"><span>[3] 미래 {years}년 퀀텀 잔고:</span><span>{int(future_value):,} 원</span></div>
                    </div>
                    <p style="margin: 0;">-----------------------------------------</p>
                    <div style="font-size: 11px; color: #555; text-align: center; margin-top: 15px; line-height: 1.4;">
                        <b>[최종 판정 코멘트]</b><br>
                        { "주둥이와 결제 앱 6자리를 잠그지 않으면 미래 자산 수십억이 마라탕 그릇과 장바구니에서 복리로 분해될 운명입니다." if missed_money > 0 else "축하합니다 폭락장을 기가 막히게 위장 지출로 방어한 당신은 이 시대 최고의 리스크 헷지 천재 트레이더입니다." }
                    </div>
                    <center style="margin-top: 20px;">
                        <div style="font-size: 32px; letter-spacing: -3px; font-weight: bold; opacity: 0.8; margin-bottom: 5px;">|||| | ||||| | |||| || ||</div>
                        <span style="font-size: 10px; color: #888;">✨ 🦜 껄무새 자산관리 시스템 ✨</span>
                    </center>
                </div>
            """, unsafe_allow_html=True)

            # 4. 소비 맞춤형 흑우 등급 인증서
            st.write("")
            st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>🪪 4. 소비 맞춤형 흑우 등급 인증서</h3>", unsafe_allow_html=True)
            if missed_money > 0:
                custom_cards = {
                    "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": {"title": "🩸 혈당 폭발 마라탕 중독자", "desc": "마라 국물과 설탕 코팅에 영혼을 저당 잡아 혈당을 올리는 사이, 본인의 시드머니는 주식 시장에서 완전히 녹아내리게 방치한 위대한 푸드 파이터", "bg": "linear-gradient(135deg, #8B0000 0%, #1A1D20 100%)"},
                    "스타벅스 바닐라라떼+디저트 (1회 11,000원)": {"title": "☕ 사이렌 오더 기부 천사", "desc": "매달 스타벅스 별사냥과 고카페인 시럽에 취해 살며 스타벅스 코리아 매출 상승에는 기여했으나 정작 본인 계좌는 공황 상태에 빠뜨린 주주", "bg": "linear-gradient(135deg, #124E3F 0%, #1A1D20 100%)"},
                    "올리브영 세일 '구경만' 가기 (1회 45,000원)": {"title": "💄 올리브영 탕진 잼 마스터", "desc": "세일 문자만 오면 '구경만 해야지' 하고 들어가 틴트와 팩으로 바구니를 채우며 CJ 올리브영 시총 방어에 본인 시드를 갈아 넣은 VVIP 흑우", "bg": "linear-gradient(135deg, #5B7065 0%, #1A1D20 100%)"},
                    "불금 배달 엽떡+치킨 세트 (1회 32,000원)": {"title": "🐔 배달 앱 다이아몬드 등급", "desc": "금요일 밤의 고독과 스트레스를 캡사이신과 튀김 옷으로 위로하느라, 통장에 억 단위 자산이 쌓일 기회를 아주 야무지게 씹어 삼키신 야식 마스터", "bg": "linear-gradient(135deg, #4A154B 0%, #1A1D20 100%)"},
                    "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": {"title": "👗 새벽 배송 폰결제 야수", "desc": "침대에 누워 흐린 눈으로 옷 구경하다 네이버페이 6자리를 광속으로 태우며, 방구석 드레스룸은 채웠으나 자산 포트폴리오는 전라로 만든 패셔니스타", "bg": "linear-gradient(135deg, #3A225D 0%, #1A1D20 100%)"},
                    "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": {"title": "💅 손끝 발끝 풀소유 영애", "desc": "손톱 위에 파츠를 올리고 눈썹을 바짝 끌어올려 비주얼 품격은 유지했으나, 정작 본인 자산 성장률은 바닥에 바짝 붙여버린 관리의 대가", "bg": "linear-gradient(135deg, #1C3D5A 0%, #1A1D20 100%)"},
                    "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": {"title": "🥃 고독한 알코올 오크통 주주", "desc": "피트 향 머금은 싱글몰트로 오늘 하루의 서러움을 녹이려다 통장 잔고까지 완벽하게 증발시켜 미장 빅테크 주주들의 기쁨이 되어주신 알코올 요정", "bg": "linear-gradient(135deg, #8A4F1D 0%, #1A1D20 100%)"},
                    "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": {"title": "🎮 데이터 쪼가리 풀소유 야수", "desc": "모니터 속 전설 스킨과 가챠 연출의 도파민에 취해 클릭 몇 번으로 실제 집 한 채 살 돈을 게임 서버 유지비로 쾌척해 버린 명예 넥슨/엔씨 주주", "bg": "linear-gradient(135deg, #2D3748 0%, #1A1D20 100%)"},
                    "주말 골프 연습장/필드 호사 (1회 120,000원)": {"title": "⛳ 잔디밭 지출의 나이스샷", "desc": "굿샷을 외치며 그린 위에서 호사를 누리는 동안 정작 본인 주식 자산 포트폴리오는 OB 구역 숲속으로 완벽하게 날려버린 필드의 타이거 흑우", "bg": "linear-gradient(135deg, #2F855A 0%, #1A1D20 100%)"},
                    "기념일 에피타이저 오마카세 (1회 150,000원)": {"title": "🍣 흐린눈 럭셔리 파인다이닝 영애", "desc": "셰프의 친절한 설명을 들으며 입안의 사치를 즐기는 순간, 내 통장 잔고는 엔비디아의 성장 에너지를 먹지 못해 원자 단위로 굶주려가던 모순의 극치", "bg": "linear-gradient(135deg, #744210 0%, #1A1D20 100%)"},
                    "체형 교정 명목 필라테스 (1회 60,000원)": {"title": "🧘 기구 위에서 비명지르는 영애", "desc": "코어 근육을 단단하게 잡아내어 척추 정렬에는 성공했으나, 정작 미래 내 집 마련을 위한 자산의 척추는 완벽하게 무너뜨린 관리의 모순", "bg": "linear-gradient(135deg, #4A5568 0%, #1A1D20 100%)"},
                    "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": {"title": "⚽ 방구석 올드 트래포드 구단주", "desc": "해외 축구 구단의 엠블럼 패치를 보며 밤마다 열광했으나, 정작 본인 자산 리그는 4부 리그 강등권에서 처참하게 헤매게 만든 유니폼 수집가", "bg": "linear-gradient(135deg, #9B2C2C 0%, #1A1D20 100%)"}
                }
                card_info = custom_cards.get(habit, {"title": "🛍️ 프로 시발비용러", "desc": "소소한 지출로 도파민을 채우며 미래 자산 퀀텀점프의 기회를 쿨하게 걷어차신 직장인 영애/대리", "bg": "linear-gradient(135deg, #4A5568 0%, #1A1D20 100%)"})
            else:
                custom_cards = {
                    "탕후루/마라탕 수명 단축 쿨타임 (1회 18,000원)": {"title": "🛡️ 마라탕 금융 치료 연맹", "desc": "처참하게 무너져 내리는 주식 시장을 예견하고 주식 대신 마라탕을 섭취함으로써 완벽한 원금 보존 및 도파민 해징에 성공한 천재 트레이더", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "스타벅스 바닐라라떼+디저트 (1회 11,000원)": {"title": "🛡️ 바닐라 시럽 자산 헤징 장인", "desc": "주식 계좌가 녹아내릴 고점 폭탄을 완벽하게 피해 매달 스타벅스 달콤한 라떼로 본인 멘탈을 우량하게 리프레시한 리스크 관리 책임자", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "올리브영 세일 '구경만' 가기 (1회 45,000원)": {"title": "🛡️ 올리브영 메이크업 생존자", "desc": "주식 차트 파란불에 스트레스받아 피부 뒤집어질 뻔한 위기를 올영 세일 꿀템 쇼핑으로 조기 진화한 명예 자산 방어 사령관", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "불금 배달 엽떡+치킨 세트 (1회 32,000원)": {"title": "🛡️ 엽떡 치킨 디펜스 마스터", "desc": "주식 시장에 시드를 던졌다면 마이너스 계좌를 보며 밤새 통곡했을 것을 배달 엽떡으로 배를 채우며 평화로운 불금을 사수한 지혜의 아이콘", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "지그재그/W컨셉 충동 의류 매수 (1회 65,000원)": {"title": "🛡️ 지그재그 풀 레이어 헷지왕", "desc": "주가가 바닥을 기는 하락장에 자금을 묶는 대신, 예쁜 옷을 사 입어 인간 지표로서의 삶의 질을 극대화한 영리한 자산 배분 전략가", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "매달 속눈썹 펌/네일 정기권 (1회 55,000원)": {"title": "🛡️ 네일 파츠 자산 수호 영애", "desc": "폭락장 주식에 투자했다면 멘탈과 손톱이 다 부러졌을 텐데, 뷰티 정기권 결제로 나 자신을 가꿔 강제 자산 방어를 실현한 진정한 승리자", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "퇴근 후 카미카제 주말 위스키 (1회 85,000원)": {"title": "🛡️ 위스키 바 오크통 방어 사령관", "desc": "주식 계좌가 녹아내릴 고점 폭탄을 피해 싱글몰트로 영혼을 치유하며 하락장 손실을 0원으로 헷징한 주류 경제학의 대가", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "플랫폼 가챠/게임 스킨 현질 (1회 50,000원)": {"title": "🛡️ 롤/메이플 넷상 자산 방어 야수", "desc": "하락장에 돈을 묶어 물리느니 화려한 게임 스킨으로 인게임 리더십과 눈 정화를 사수한 완벽한 가상 자산 헷지 장인", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "주말 골프 연습장/필드 호사 (1회 120,000원)": {"title": "🛡️ 싱글 플레이어 리스크 타겟", "desc": "주가 차트 폭락을 볼 바엔 탁 트인 초록색 잔디를 보며 스윙하는 게 정신과 자산을 동시에 지키는 초정밀 헷지 솔루션임을 입증", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "기념일 에피타이저 오마카세 (1회 150,000원)": {"title": "🛡️ 미식 경제 리스크 관리 소장", "desc": "물리는 주식 계좌 개설 대신 내 미각의 도파민을 우량하게 채워 인생의 순수 행복 총량을 완벽 수호한 미식계의 헤지펀드 거물", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "체형 교정 명목 필라테스 (1회 60,000원)": {"title": "🛡️ 척추 정렬 자산 방어 영애", "desc": "하락장에서 멘탈과 자산이 무너지는 대신 신체 코어 근육을 탄탄하게 잡아내어 물리적 건강 자산을 최상위 등급으로 헤징해 낸 명예 소장", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"},
                    "유럽 축구 구단 감성 레플리카 유니폼 (1회 140,000원)": {"title": "🛡️ 방구석 강등권 자산 방어 감독", "desc": "주식 샀으면 4부 리그로 강등당했을 자금을 유니폼 실물 자산으로 치환해 완벽한 가치 보존에 성공한 전술 마스터", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"}
                }
                card_info = custom_cards.get(habit, {"title": "🛡️ 영리한 헷지러", "desc": "자산 폭락의 계곡을 예리한 도파민 지출로 우회해 낸 명예 승리자", "bg": "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"})
            
            st.markdown(f"""
                <div style="background: {card_info['bg']}; border: 2px dashed #FFFFFF; padding: 25px; border-radius: 12px; text-align: center; color: #FFFFFF; font-family: sans-serif; max-width: 500px; margin: 0 auto;">
                    <span style="font-size: 12px; letter-spacing: 2px; color: #AAADB0;">OFFICIAL CERTIFICATE</span>
                    <h2 style="color: #FFFFFF; margin: 10px 0; font-size: 24px;">{card_info['title']}</h2>
                    <div style="border-top: 1px solid #3C4043; border-bottom: 1px solid #3C4043; padding: 15px 0; margin: 15px 0; font-size: 13.5px; line-height: 1.6; color: #E8EAED;">
                        {card_info['desc']}<br><br>
                        <b>최종 누적 매몰 자산:</b> {int(total_seed):,} 원<br>
                        <b>미래 상실 자산 예측:</b> {int(future_value):,} 원
                    </div>
                    <span style="font-size: 11px; color: #AAADB0;">✨ 껄무새 자산 예측 시스템 박제 완료</span>
                </div>
            """, unsafe_allow_html=True)

            # 5. Gemini 종합 팩폭 브리핑
            st.write("")
            st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>✨ Gemini 종합 브리핑</h3>", unsafe_allow_html=True)
            st.markdown(f"""<div style="background: linear-gradient(135deg, #1A1B2F 0%, #16161D 100%); border: 1px solid #4A3E7D; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;"><span style="color: #F28B82; font-weight: bold; font-size: 16px;">⚠️ [손실 진단 및 예측] 장바구니에 스며든 무서운 스노우볼 효과</span><br><br>요청하신 데이터를 분석한 결과, 뇌 빼고 결제해 온 <b>'{habit_clean_name}'</b> 비용이 <b>{target_asset}</b>의 폭발적인 과거 N년 순 누적 성장세(총 {total_asset_growth:+.2f}%)를 정통으로 얻어맞고 무시무시한 미래 폭탄을 만들어냈습니다.<br><br>이미 지나간 {years}년 동안 날린 돈만 <b>{int(missed_money/10000):,}만 원</b>에 달하며, 이 돈이 만약 과거의 미친 모멘텀을 100% 그대로 유지하며 미래 {years}년 동안 한 번 더 복사되어 달린다면... 당신의 통장에는 무려 <b>{int(future_value/10000):,}만 원</b>이라는 초거대 자산이 찍혀 있게 됩니다.<br><br>강남 아파트 등기나 포르쉐 한 대 뽑고 유유히 은퇴할 수준의 미래 기회비용이 지금 스타벅스 컵과 마라탕 그릇, 지그재그 장바구니 속에서 시원하게 녹아내리고 있다는 뜻입니다. 미래의 자신에게 사죄하는 마음으로 오늘부터 즉시 충동 결제를 전면 중단할 것을 강력히 권고합니다.</div>""" if missed_money > 0 else f"""<div style="background: linear-gradient(135deg, #16261E 0%, #16161D 100%); border: 1px solid #2B543A; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;"><span style="color: #81C995; font-weight: bold; font-size: 16px;">😎 [반전 정산] 파괴적 하락 역스노우볼을 피한 인류 최강의 생존 전략</span><br><br>축하합니다. 시뮬레이션 결과 귀하의 소비는 자산 폭락의 늪을 피한 '천재적인 리스크 관리 전략'이었음이 데이터로 입증되었습니다.<br><br>만약 {years}년 전에 눈물 흘려가며 참아낸 돈을 <b>{target_asset}</b>에 적립했다면, 과거의 처참한 하락 사이클({total_asset_growth:+.2f}%)에 정통으로 처맞고 계좌가 분해되는 고문을 당했을 것입니다. 만약 이 파괴적인 하락 에너지가 미래 {years}년 뒤까지 그대로 1:1 직진 적용된다면, 당신의 자산은 반토막을 넘어 <b>{int(future_value/10000):,}만 원</b> 수준으로 처참하게 증발할 예정이었습니다.<br><br>주식에 묶여서 증발할 뻔한 미래의 돈을 미리 끄집어내어 <b>'{habit_clean_name}'</b>으로 알차게 도파민을 충전한 당신이 이 시대의 진정한 금융 승리자입니다. 앞으로도 소비 흐름을 아주 든든하게 유지하십시오.</div>""", unsafe_allow_html=True)

        # 6. 실시간 한탄방 방명록 (타임머신 하단 고정)
        st.write("---")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>💬 실시간 월급루팡 익명 한탄방</h3>", unsafe_allow_html=True)
        user_comment = st.text_input("💬 흑우로서 한마디 남기기 (Enter 입력 시 등록)", placeholder="예: 축구 유니폼 살 돈 모았으면 이미 축구 구단 하나 샀겠네..")
        if user_comment:
            st.session_state["chat_log"].insert(0, f"익명루팡_{random.randint(100,999)}: {user_comment}")
            st.rerun()
        chat_box_html = "<div style='background-color: #1E1F20; border: 1px solid #3C4043; padding: 15px; border-radius: 8px; max-height: 200px; overflow-y: auto; color: #FFFFFF; font-family: monospace; font-size: 13px; line-height: 1.6;'>"
        for log in st.session_state["chat_log"]: chat_box_html += f"<div>{log}</div>"
        chat_box_html += "</div>"
        st.markdown(chat_box_html, unsafe_allow_html=True)

    # ==================== TAB 2: 오늘의 사주 운세 탭 ====================
    with tab2:
        st.markdown("### 🔮 사주 명리학 기반 오늘의 財物(재물) 운세 진단")
        st.write("나의 태어난 월(음력/양력 무관)에 흐르는 오행과 기운을 분석하여 자산 통제력을 감정합니다.")
        birth_month = st.selectbox("본인의 태어난 달(月)을 고르세요", [f"{m}월 생" for m in range(1, 13)], key="saju_tab_select")
        
        if st.button("☯️ 사주 오행 비밀 저장고 열기"):
            saju_database = {
                "1월 생": "🐯 [인월-木기운] 정재(正財)운 발달: 따박따박 모아야 할 시드머니가 장바구니 결제로 공중 분해되는 도화살이 꼈습니다. 지그재그 앱을 삭제해야 자산이 수호됩니다.",
                "2월 생": "🐰 [묘월-木기운] 겁재(劫財)운 유입: 내 지갑의 재물을 강탈해 가는 기운이 강합니다 오늘 배달 엽떡이나 치킨을 결제하면 야수의 손실 역복리가 스노우볼을 굴립니다.",
                "3월 생": "🐳 [진월-土기운] 화개(華蓋)살 작용: 미식과 뷰티에 돈을 탕진하기 쉬운 날. 오마카세나 네일숍 정기권 결제 욕구가 치솟으나, 참아내면 미래 반도체 주식의 영양분이 됩니다.",
                "4월 생": "🐍 [사월-火기운] 편재(偏財)운 강세: 일확천금을 노리는 야수의 심장이 불타오릅니다. 뜬금없는 게임 가챠나 위스키 충동 구매는 엔비디아 평단가를 파괴하는 지름길입니다.",
                "5월 생": "🐴 [오월-火기운] 양인(羊刃)살 등장: 소비 성향이 매우 극단적입니다 올리브영 세일에 '구경만' 갔다가 10만 원 넘게 긁고 나올 상이니 퇴근길 동선을 우회하십시오.",
                "6월 생": "🐑 [미월-土기운] 암록(暗祿)살 보존: 보이지 않는 곳에서 자산이 방어되는 날입니다. 오늘 마라탕과 스타벅스를 꾹 참아내면 삼전이 미래에 보이지 않는 은총을 내립니다.",
                "7월 생": "🐵 [신월-金기운] 역마(驛馬)살 동해: 소비성 이동이 많습니다. 주말 골프나 충동적인 의류 매수로 지출의 역마가 뛰노니 장바구니 비밀번호를 스스로 잠그는 지혜가 필요합니다.",
                "8월 생": "🐔 [유월-金기운] 유금(酉金) 격각: 자산 투자 타이머가 꼬이기 쉽습니다. 구글이나 테슬라 적립금의 씨앗을 털어 샌디스크 스킨이나 위스키를 사면 3년 뒤 피눈물을 흘립니다.",
                "9월 생": "🐶 [술월-土기운] 백호(白虎)살 대치: 지출의 폭발력이 어마어마합니다. 불금 야식 본능이 자산의 맥을 끊어놓을 수 있으니 생수를 마시며 재물운의 백호 마귀를 다스리십시오.",
                "10월 생": "🐷 [해월-水기운] 식신(食神)생재: 먹는 것에 돈을 쓰면 자산이 방어되는 신비한 날! 오늘 폭락하는 국장을 보면 차라리 마라탕이나 떡볶이로 리스크를 완벽 헷징 하십시오.",
                "11월 생": "🐭 [자월-水기운] 편관(偏官) 압박: 지출 압박 스트레스가 최고조입니다. 충동적으로 W컨셉이나 속눈썹 정기권을 지르고 싶겠으나, 참으면 미래 마이크론 주주가 됩니다.",
                "12월 생": "🐮 [축월-土기운] 재고(財庫) 귀인: 재물 창고가 열리는 대길의 날! 오늘 소비를 완전히 통제하고 우량주 시뮬레이션을 돌려 미래의 수십억 자산 기운을 받으십시오."
            }
            st.info(saju_database[birth_month])

    # ==================== TAB 3: 자산 파괴 밸런스 게임 탭 ====================
    with tab3:
        st.markdown("### ⚔️ 자산 파괴 주주총회 밸런스 게임")
        st.write("2026년 현재 대한민국 2030의 자산을 파괴하는 최악의 주범을 가립니다. 둘 중 하나만 끊을 수 있다면?")
        st.write("**Q. 평생 동안 둘 중 딱 하나만 안 쓰고 주식 계좌에 적립식으로 모을 수 있다면?**")
        
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            if st.button("🅰️ 평생 배달 엽떡+치킨 야식 끊기", key="btn_vote_a"):
                st.session_state["vote_data"]["A"] += 1
                st.rerun()
        with col_v2:
            if st.button("🅱️ 평생 올리브영 세일 '구경만' 가기 끊기", key="btn_vote_b"):
                st.session_state["vote_data"]["B"] += 1
                st.rerun()
                
        total_votes = st.session_state["vote_data"]["A"] + st.session_state["vote_data"]["B"]
        per_A = (st.session_state["vote_data"]["A"] / total_votes) * 100
        per_B = (st.session_state["vote_data"]["B"] / total_votes) * 100
        
        st.write("")
        st.progress(int(per_A))
        st.caption(f"📊 실시간 주주 투표 결과: 🅰️ {per_A:.1f}% vs 🅱️ {per_B:.1f}% (총 {total_votes}명 참여 배틀 중)")
