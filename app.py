import streamlit as st
import streamlit.components.v1 as components
import datetime
import random

# 1. 제미나이 다크모드 기반 최적화 설정
st.set_page_config(
    page_title="✨ Gemini - 자산 최적화 시뮬레이션 v7", 
    page_icon="✨",
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

# 익명 방명록을 위한 Streamlit 세션 스테이트 초기화
if "chat_log" not in st.session_state:
    st.session_state["chat_log"] = [
        "익명루팡1: 나 방금 올영 5년 모았는데 한미반도체 1억 날림;; 한강 간다",
        "마라탕귀신: 마라탕 끊고 마이크론 간다 진짜 딱 기다려라",
        "킹받네: 주식 사서 까먹을 바엔 엽떡 치킨 먹은 내가 승리자 아님? ㅋㅋ"
    ]

# 🔴 AREA A: 부장님 방어막
if is_boss_mode:
    st.error("🔒 [보안] 本 화면은 사내 인트라넷 자산입니다. 외부 유출을 금합니다.")
    st.title("📊 2026_전사_리소스_최적화_KPI_Data")
    st.dataframe({
        "Index": [1, 2, 3],
        "Task": ["Next-Gen ERP 구축", "Data Pipeline v3 안정화", "Core Sandbox 기획"],
        "Progress": ["94.2%", "81.2%", "45.0%"]
    }, use_container_width=True)
    if st.button("🔄 Gemini 세션 새로고침"):
        st.query_params["boss_mode"] = "false"
        st.rerun()

# 🟢 AREA B: 제미나이 팩폭 + 도파민 놀이터
else:
    HISTORICAL_STOCK_DATA = {
        "삼성전자 (005930.KS)": {"current_price": 358250, "yearly_prices": [358250, 285000, 72500, 63100, 75500]},
        "SK하이닉스 (000660.KS)": {"current_price": 168000, "yearly_prices": [168000, 142000, 115000, 92000, 121000]},
        "한미반도체 (042700.KS)": {"current_price": 142500, "yearly_prices": [142500, 118000, 61000, 14500, 18500]},
        "엔비디아 (NVDA)": {"current_price": 125, "yearly_prices": [125, 85, 38, 16, 22]},
        "마이크론 (MU)": {"current_price": 132, "yearly_prices": [132, 110, 68, 55, 74]},
        "샌디스크/웨스턴디지털 (WDC)": {"current_price": 72, "yearly_prices": [72, 64, 42, 38, 52]}
    }

    st.markdown("""
        <div style="margin-bottom: 10px;">
            <span style="font-size: 32px; font-weight: 700; background: linear-gradient(45deg, #4285F4, #9B51E0, #E91E63); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                ✨ Gemini Custom Plus
            </span>
        </div>
        <h2 style="font-family: sans-serif; font-weight: 400; color: #FFFFFF; margin-top: 0; margin-bottom: 25px; font-size: 24px;">
            무엇을 도와드릴까요? 소비 분석, 미래 자산 예측 및 멘탈 케어를 통합 제공합니다.
        </h2>
    """, unsafe_allow_html=True)

    # 🎰 아이디어 4: 오늘의 시발비용 무작위 추천 가이드 (청개구리 기믹)
    st.markdown("##### 🎲 오늘의 합법적 탕진 메뉴 추천 가이드")
    if st.button("🎁 오늘 스트레스 만빵인데 주식 살까? 아니면 지를까?"):
        random_items = [
            "오늘은 반도체 장세가 흉흉합니다. 주식 사서 물릴 바엔 퇴근길에 마라탕에 꿔바로우(28,000원) 풀코스로 조지십시오.",
            "엔비디아가 횡보 중입니다. 무리한 진입보다는 올리브영에 가서 평소 갖고 싶던 향수(45,000원)를 결제해 자산을 헷지하세요.",
            "국장 거래대금이 처참합니다. 네이버페이 켜고 지그재그에서 옷 한 벌(65,000원) 시원하게 지르는 게 멘탈 건강에 개이득입니다.",
            "오늘은 야수의 심장이 굳어가는 날. 배달 앱 켜서 엽떡에 허니콤보 세트(32,000원) 땡기고 꿀잠 자는 게 진정한 금융 치료입니다."
        ]
        st.success(random.choice(random_items))

    st.write("---")
    st.markdown("##### 🔍 시뮬레이션 프롬프트 설정")
    
    with st.form("gemini_form"):
        col1, col2 = st.columns(2)
        with col1:
            habit = st.selectbox(
                "🛍️ 매달 '흐린 눈'으로 지출 중인 항목", 
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
                "📈 연동할 목적 자산 (반도체/AI 벨트)", 
                [
                    "삼성전자 (005930.KS)", 
                    "SK하이닉스 (000660.KS)", 
                    "한미반도체 (042700.KS)",
                    "엔비디아 (NVDA)", 
                    "마이크론 (MU)", 
                    "샌디스크/웨스턴디지털 (WDC)"
                ]
            )
            years = st.slider("⏳ 타임머신 추적 기간 (년)", 1, 5, 3)
            
        submitted = st.form_submit_button("✨ 제미나이 종합 분석 시뮬레이션 스타트 (Enter)")

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
            
        is_foreign = ".KS" not in target_asset
        exchange_rate = 1350 if is_foreign else 1
        final_value = total_shares * current_price * exchange_rate
        price_unit = "$" if is_foreign else "원"
        missed_money = final_value - total_seed

        total_return_rate = final_value / total_seed if total_seed > 0 else 1.0
        total_weeks = years * 52
        weekly_growth_rate = (total_return_rate) ** (1 / total_weeks) - 1 if total_return_rate > 0 else 0.0
        future_value = final_value * total_return_rate

        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>📊 1. 과거 데이터 기반 실시간 정산</h3>", unsafe_allow_html=True)
        
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: #AAADB0; font-weight: 500;">🪙 총 지출 매몰 원금</div><div style="font-size: 22px; font-weight: 600; color: #FFFFFF; margin-top: 5px;">{int(total_seed):,} 원</div></div>""", unsafe_allow_html=True)
        with res_col2:
            st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: #81C995; font-weight: 500;">📈 현재 자산 가치 (오늘)</div><div style="font-size: 22px; font-weight: 600; color: #81C995; margin-top: 5px;">{int(final_value):,} 원</div></div>""", unsafe_allow_html=True)
        with res_col3:
            card_color = "#F28B82" if missed_money > 0 else "#8AB4F8"
            status_text = "🚨 기회상실 순손실액" if missed_money > 0 else "🛡️ 리스크 최종 방어액"
            st.markdown(f"""<div style="border: 1px solid #3C4043; padding: 18px; border-radius: 8px; background-color: #1E1F20;"><div style="font-size: 12px; color: {card_color}; font-weight: 500;">{status_text}</div><div style="font-size: 22px; font-weight: 600; color: {card_color}; margin-top: 5px;">{"+" if missed_money > 0 else ""}{int(missed_money):,} 원</div></div>""", unsafe_allow_html=True)

        st.write("")
        st.markdown(f"<h3 style='color: #FFFFFF; font-size: 18px;'>🔮 2. 미래 {years}년 뒤 자산 행복회로 예측</h3>", unsafe_allow_html=True)
        
        fut_col1, fut_col2 = st.columns(2)
        with fut_col1:
            st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;"><div style="font-size: 12px; color: #D6BCFA; font-weight: 500;">⚡ 과거 주봉 평균 상승률 (복리)</div><div style="font-size: 24px; font-weight: 600; color: #D6BCFA; margin-top: 5px;">{weekly_growth_rate*100:+.4f} % / 주</div></div>""", unsafe_allow_html=True)
        with fut_col2:
            st.markdown(f"""<div style="border: 1px solid #4A3E7D; padding: 18px; border-radius: 8px; background-color: #1A1B2F;"><div style="font-size: 12px; color: #FFD700; font-weight: 500;">💰 미래 {years}년 뒤 최종 잔고 예측</div><div style="font-size: 24px; font-weight: 600; color: #FFD700; margin-top: 5px;">{int(future_value):,} 원</div></div>""", unsafe_allow_html=True)

        # 🧪 아이디어 2: '이 돈이면 차라리...' 실물 자산 환산기 연산
        maratang_count = int(total_seed / 10000)
        dior_bag_count = round(total_seed / 9000000, 1)
        car_count = round(total_seed / 28000000, 1)

        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>👜 3. 시발비용 실물 자산 환산 충격 요약</h3>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style="background-color: #202124; border: 1px solid #3C4043; padding: 20px; border-radius: 8px; color: #FFFFFF; font-size: 14px;">
                💡 님이 장바구니와 주둥이에 버린 원금 <b>{int(total_seed):,}원</b>을 다른 가치로 환산하면 다음과 같습니다.<br><br>
                • 🧋 <b>마라탕 계열 푸드:</b> 무려 <b>{maratang_count} 그릇</b>을 공중에 날려 보낸 효과<br>
                • 👜 <b>명품 백 스케일:</b> 백화점 명품관 <b>디올 레이디백 약 {dior_bag_count}개</b>를 눈앞에서 찢어버린 효과<br>
                • 🚗 <b>현대 자동차 스케일:</b> <b>아반떼 신형 풀옵션 {car_count}대</b>를 그냥 한강물에 집어 던진 효과
            </div>
        """, unsafe_allow_html=True)

        # 🪪 아이디어 1: SNS 박제용 흑우 등급 자산 인증서 카드 UI
        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>🪪 4. SNS 박제용 흑우 등급 인증서 (캡처용)</h3>", unsafe_allow_html=True)
        
        # 금액별 등급 나누기 기믹
        if missed_money > 30000000:
            cert_title = "🚨 천상계 기회 나눔 천사"
            cert_desc = "엔비디아와 하이닉스 주주들의 하와이 비행기 날개를 본인 장바구니로 직접 결제해 주신 위대한 기부천사 임직원"
            cert_bg = "linear-gradient(135deg, #4A154B 0%, #1A1D20 100%)"
        elif missed_money > 0:
            cert_title = "🛍️ 올리브영 VVIP 우량 흑우"
            cert_desc = "네이버페이 6자리 비번을 광속으로 누르며 미래 자산을 야무지게 도파민과 교환한 이 시대의 진정한 감성 지출러"
            cert_bg = "linear-gradient(135deg, #1C3D5A 0%, #1A1D20 100%)"
        else:
            cert_title = "🛡️ 자산 헤징의 신 (인생 승리자)"
            cert_desc = "처참한 반도체 고점 사이클을 기가 막힌 엽떡/마라탕 지출로 우회하여 원금 까먹을 위기를 방어한 위대한 월급방어 대가"
            cert_bg = "linear-gradient(135deg, #1B4D3E 0%, #1A1D20 100%)"

        st.markdown(f"""
            <div style="background: {cert_bg}; border: 2px dashed #FFFFFF; padding: 25px; border-radius: 12px; text-align: center; color: #FFFFFF; font-family: sans-serif; max-width: 500px; margin: 0 auto;">
                <span style="font-size: 12px; letter-spacing: 2px; color: #AAADB0;">OFFICIAL CERTIFICATE</span>
                <h2 style="color: #FFFFFF; margin: 10px 0; font-size: 24px;">{cert_title}</h2>
                <div style="border-top: 1px solid #3C4043; border-bottom: 1px solid #3C4043; padding: 15px 0; margin: 15px 0; font-size: 13.5px; line-height: 1.6; color: #E8EAED;">
                    {cert_desc}<br><br>
                    <b>최종 누적 매몰 자산:</b> {int(total_seed):,} 원<br>
                    <b>미래 상실 자산 예측:</b> {int(future_value):,} 원
                </div>
                <span style="font-size: 11px; color: #AAADB0;">✨ Gemini Asset Analyzer 박제 완료 • 스마트폰 화면을 캡처해서 인증하세요</span>
            </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>✨ Gemini 종합 브리핑</h3>", unsafe_allow_html=True)
        habit_name = habit.split(" (")[0]
        
        if missed_money > 0:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #1A1B2F 0%, #16161D 100%); border: 1px solid #4A3E7D; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;">
                    <span style="color: #F28B82; font-weight: bold; font-size: 16px;">⚠️ [손실 진단 및 예측] 장바구니에 스며든 무서운 스노우볼 효과</span><br><br>
                    요청하신 데이터를 분석한 결과, 무심코 결제해 온 <b>'{habit_name}'</b> 비용이 <b>{target_asset}</b>의 폭발적인 주간 복리 성장세(주당 {weekly_growth_rate*100:+.3f}%)를 만나 잔인한 기회비용을 만들어냈습니다.<br><br>
                    이미 지나간 {years}년 동안 날린 돈만 <b>{int(missed_money/10000):,}만 원</b>에 달하며, 이 돈이 만약 동일한 주봉 상승 탄력을 유지하며 미래 {years}년 동안 '복리'로 더 굴러간다면... 당신의 통장에는 무려 <b>{int(future_value/10000):,}만 원</b>이라는 거금이 찍혀 있게 됩니다.<br><br>
                    강남 아파트 계약금이나 포르쉐 한 대 뽑을 수준의 미래 자산이 지금 스타벅스 컵과 마라탕 그릇, 지그재그 장바구니 속에서 살살 녹아내리고 있다는 뜻입니다. 미래의 자신에게 사죄하는 마음으로 오늘부터 즉시 충동 결제를 전면 중단할 것을 강력히 권고합니다.
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #16261E 0%, #16161D 100%); border: 1px solid #2B543A; padding: 22px; border-radius: 12px; color: #FFFFFF; line-height: 1.7; font-size: 14.5px;">
                    <span style="color: #81C995; font-weight: bold; font-size: 16px;">😎 [반전 정산] 파괴적 역복리를 피한 인류 최강의 생존 전략</span><br><br>
                    축하합니다. 시뮬레이션 결과 귀하의 소비는 자산 폭락의 역복리 늪을 피해 간 '천재적인 리스크 관리'였음이 데이터로 입증되었습니다.<br><br>
                    만약 {years}년 전에 눈물 흘려가며 참아낸 돈을 <b>{target_asset}</b>에 적립했다면, 주당 {weekly_growth_rate*100:.3f}%씩 계좌가 살살 녹아내리는 고문을 당했을 것입니다. 만약 이 파괴적인 하락세가 미래 {years}년 뒤까지 그대로 복리로 이어진다면, 당신의 자산은 반토막을 넘어 <b>{int(future_value/10000):,}만 원</b> 수준으로 처참하게 소멸할 예정이었습니다.<br><br>
                    주식에 묶여서 증발할 뻔한 미래의 돈을 미리 끄집어내어 <b>'{habit_name}'</b>으로 알차게 도파민을 충전한 당신이 이 시대의 진정한 금융 승리자입니다. 앞으로도 상사가 킹받게 할 때는 주식 창을 켜는 대신 장바구니를 채우며 자산을 든든하게 방어하십시오.
                </div>
            """, unsafe_allow_html=True)

    # --- ⚔️ 아이디어 3: 실시간 월급루팡 익명 한탄 한줄 방명록 섹션 (맨 아래 배치) ---
    st.write("---")
    st.markdown("<h3 style='color: #FFFFFF; font-size: 18px;'>💬 5. 실시간 월급루팡 익명 한탄방</h3>", unsafe_allow_html=True)
    
    # 댓글 입력 창 구성
    with st.container():
        user_comment = st.text_input("💬 흑우로서 한마디 남기기 (Enter 입력 시 등록)", placeholder="예: 방금 한미반도체 돌려보고 기절함")
        if user_comment:
            # 새 댓글을 리스트 맨 위에 추가
            st.session_state["chat_log"].insert(0, f"익명루팡_{random.randint(100,999)}: {user_comment}")
            st.rerun()

        # 댓글 리스트 출력 박스 연출 (흰색 가독성 글씨)
        chat_box_html = "<div style='background-color: #1E1F20; border: 1px solid #3C4043; padding: 15px; border-radius: 8px; max-height: 200px; overflow-y: auto; color: #FFFFFF; font-family: monospace; font-size: 13px; line-height: 1.6;'>"
        for log in st.session_state["chat_log"]:
            chat_box_html += f"<div>{log}</div>"
        chat_box_html += "</div>"
        st.markdown(chat_box_html, unsafe_allow_html=True)
