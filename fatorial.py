import streamlit as st
import graphviz

def factorial(n):
    """팩토리얼 계산 함수 (재귀)"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def visualize_factorial_call(n):
    """재귀 호출 관계를 시각화"""
    graph = graphviz.Digraph()
    
    def add_edges(num):
        if num == 0 or num == 1:
            graph.node(str(num), f"{num}! = 1")
        else:
            graph.node(str(num), f"{num}! = {num} * ({num - 1})!")
            graph.edge(str(num), str(num - 1))
            add_edges(num - 1)

    add_edges(n)
    return graph

# Streamlit 앱 제목
st.title("팩토리얼 계산기 및 재귀 호출 시각화")

# 사용자 입력 받기
n = st.number_input("팩토리얼을 계산할 숫자를 입력하세요 (0 이상 정수)", min_value=0, step=1, value=5)

# 계산 및 결과 표시
if st.button("계산 및 시각화"):
    result = factorial(n)
    st.success(f"{n}! = {result}")

    # 재귀 호출 시각화
    st.subheader("재귀 호출 관계")
    graph = visualize_factorial_call(n)
    st.graphviz_chart(graph)
