import streamlit as st

# 웹 페이지 제목 설정
st.title("🎢 놀이기구 탑승 가능 여부 확인기")
st.write("본인의 키를 입력하거나 슬라이더를 조절해 보세요.")

# 1. 사용자로부터 키 입력 받기 (숫자 입력창과 슬라이더 조합)
height = st.number_input("키(cm)를 입력하세요:", min_value=0, max_value=250, value=150, step=1)
# 또는 아래와 같이 슬라이더를 쓸 수도 있습니다. (주석 해제 후 사용 가능)
# height = st.slider("키(cm)를 선택하세요:", 50, 220, 150)

st.divider() # 구분선

# 2. 조건에 따른 결과 출력 (st.info, st.success, st.error 등으로 시각화 효과 추가)
if height < 100:
    st.error("🚫 탑승 불가 (키가 100cm 미만입니다.)")

elif 100 <= height < 130:
    st.warning("⚠️ 보호자 동행 시 탑승 가능")

elif 130 <= height < 195:
    st.success("🟢 탑승 가능")

else:  # height >= 195 (기존 코드의 경계값 누락 보완 및 초과 조건 처리)
    st.error("🚫 탑승 불가 (키가 195cm 이상입니다.)")