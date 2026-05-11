import streamlit as st

st.title("🚀 실생활 문제 해결 프로젝트")
st.write("학번과 이름을 입력하고 프로젝트를 시작하세요.")

name = st.text_input("이름")
if name:
    st.success(f"{name}님, 환영합니다! 이제 코드를 수정해 문제를 해결해 보세요.")

name = st.text_input("이름이 뭐야?")
choice = st.selectbox("오늘 기분은?", ["좋음", "보통", "피곤"])
score = st.slider("나의 에너지 점수", 0, 100)
if st.button("응원 메시지 받기"):
st.success("오늘도 잘 할 수 있어!")
