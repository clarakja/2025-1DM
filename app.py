import streamlit as st
from itertools import product

# Streamlit 앱 제목
st.title("논리와 부울 대수 학습 애플리케이션")

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴 선택", [
    "기본 논리 연산",
    "진리표 생성",
    "논리 회로 시뮬레이션",
    "논리식 평가기",
    "조건 기반 프로그램",
    "암호 해독 게임"
])

# 1. 기본 논리 연산
if menu == "기본 논리 연산":
    st.header("기본 논리 연산")
    a = st.checkbox("A (True/False)", value=True)
    b = st.checkbox("B (True/False)", value=False)
    st.write(f"**A AND B:** {a and b}")
    st.write(f"**A OR B:** {a or b}")
    st.write(f"**NOT A:** {not a}")

# 2. 진리표 생성
elif menu == "진리표 생성":
    st.header("진리표 생성")
    inputs = list(product([True, False], repeat=2))
    st.write("**진리표**")
    st.write("A\tB\tA AND B\tA OR B\tNOT A")
    for a, b in inputs:
        st.write(f"{a}\t{b}\t{a and b}\t{a or b}\t{not a}")

# 3. 논리 회로 시뮬레이션
elif menu == "논리 회로 시뮬레이션":
    st.header("논리 회로 시뮬레이션")
    a = st.checkbox("A (True/False)", value=True)
    b = st.checkbox("B (True/False)", value=False)
    and_gate = a and b
    or_gate = a or b
    not_a = not a
    st.write(f"**AND Gate:** {and_gate}")
    st.write(f"**OR Gate:** {or_gate}")
    st.write(f"**NOT A:** {not_a}")

# 4. 논리식 평가기
elif menu == "논리식 평가기":
    st.header("논리식 평가기")
    st.write("논리식을 입력하세요 (예: `a and b or not c`)")
    expression = st.text_input("논리식 입력", "a and b or not c")
    a = st.checkbox("A (True/False)", value=True)
    b = st.checkbox("B (True/False)", value=False)
    c = st.checkbox("C (True/False)", value=True)
    variables = {'a': a, 'b': b, 'c': c}
    try:
        result = eval(expression, {}, variables)
        st.write(f"**논리식 결과:** {result}")
    except Exception as e:
        st.error(f"오류: {e}")

# 5. 조건 기반 프로그램
elif menu == "조건 기반 프로그램":
    st.header("조건 기반 프로그램")
    grade = st.slider("점수 입력", 0, 100, 85)
    is_club_member = st.checkbox("동아리 활동 여부", value=True)
    if grade > 80 and is_club_member:
        st.success("합격: 점수가 높고 동아리 활동을 하고 있습니다.")
    elif grade > 80 or is_club_member:
        st.warning("조건부 합격: 점수나 동아리 중 하나는 만족합니다.")
    else:
        st.error("불합격")

# 6. 암호 해독 게임
elif menu == "암호 해독 게임":
    st.header("암호 해독 게임")
    a = st.checkbox("A (True/False)", value=True)
    b = st.checkbox("B (True/False)", value=False)
    c = st.checkbox("C (True/False)", value=True)

    def unlock_code(a, b, c):
        return (a and not b) or (c and not a)

    if unlock_code(a, b, c):
        st.success("문이 열렸습니다!")
    else:
        st.error("잠겨 있습니다.")
