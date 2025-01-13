import streamlit as st
from itertools import product

# Streamlit 앱 제목
st.title("논리와 부울 대수 학습 애플리케이션")

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴 선택", [
    "기본 논리 연산",
    "진리표 생성",
    "논리식 평가기",
])

# 1. 기본 논리 연산
if menu == "기본 논리 연산":
    st.header("기본 논리 연산")
    a = st.checkbox("A (True/False)", value=True)
    b = st.checkbox("B (True/False)", value=True)
    st.write(f"**A AND B:** {a and b}")
    st.write(f"**A OR B:** {a or b}")
    st.write(f"**NOT A:** {not a}")

# 2. 진리표 생성
elif menu == "진리표 생성":
    st.header("진리표 생성")
    inputs = list(product([True, False], repeat=2))
    truth_table = []
    for a, b in inputs:
        truth_table.append({
            "A": a,
            "B": b,
            "A AND B": a and b,
            "A OR B": a or b,
            "NOT A": not a
        })

    # 진리표 출력
    st.write("**진리표**")
    st.table(truth_table)

# 3.  논리식 평가기
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
