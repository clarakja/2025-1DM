import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Streamlit 앱 제목
st.title("친구 관계 네트워크 시각화")

# 그래프 생성
G = nx.Graph()
G.add_edges_from([('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'), ('Charlie', 'Eve')])

# 네트워크 그래프 시각화 함수
def draw_graph(graph):
    plt.figure(figsize=(6, 4))
    nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
    st.pyplot(plt)

# 초기 그래프 출력
st.subheader("초기 친구 관계 네트워크")
draw_graph(G)

# 사용자 입력을 통한 네트워크 추가
st.subheader("관계를 추가해보세요")
node1 = st.text_input("첫 번째 친구 이름")
node2 = st.text_input("두 번째 친구 이름")

if st.button("관계 추가"):
    if node1 and node2:
        if node1 != node2:
            if G.has_edge(node1, node2):
                st.warning(f"{node1}와 {node2}의 관계는 이미 존재합니다.")
            else:
                G.add_edge(node1, node2)
                st.success(f"{node1}와 {node2}의 관계가 추가되었습니다.")
                draw_graph(G)
        else:
            st.error("자기 자신과의 관계는 추가할 수 없습니다.")
    else:
        st.error("두 개의 친구 이름을 모두 입력하세요.")
