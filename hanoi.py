import streamlit as st
import graphviz

def hanoi_tower(n, source, target, auxiliary, graph=None):
    """
    하노이 타워 문제 해결 함수 (시각화 포함)
    :param n: 원반의 개수
    :param source: 원반이 시작하는 기둥
    :param target: 원반이 이동해야 하는 목표 기둥
    :param auxiliary: 원반 이동을 보조하는 기둥
    :param graph: Graphviz 객체
    """
    if n == 1:
        move = f"Move disk 1 from {source} to {target}"
        st.write(move)
        if graph:
            graph.edge(source, target, label=f"Disk 1")
        return

    # Step 1: n-1개의 원반을 보조 기둥으로 이동
    hanoi_tower(n - 1, source, auxiliary, target, graph)

    # Step 2: 가장 큰 원반을 목표 기둥으로 이동
    move = f"Move disk {n} from {source} to {target}"
    st.write(move)
    if graph:
        graph.edge(source, target, label=f"Disk {n}")

    # Step 3: n-1개의 원반을 목표 기둥으로 이동
    hanoi_tower(n - 1, auxiliary, target, source, graph)

# Streamlit 앱 제목
st.title("하노이 타워 시각화")

# 사용자 입력 받기
num_disks = st.number_input("원반 개수를 입력하세요 (1~10):", min_value=1, max_value=10, step=1, value=3)

if st.button("시작하기"):
    st.write(f"**{num_disks}개의 원반을 이동하는 단계:**")
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR')  # 왼쪽에서 오른쪽 방향 그래프 설정
    
    # 하노이 타워 실행
    hanoi_tower(num_disks, 'A', 'C', 'B', graph)

    # Graphviz 차트 출력
    st.subheader("재귀 호출 시각화")
    st.graphviz_chart(graph)
