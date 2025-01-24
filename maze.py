import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def create_maze_graph():
    """미로 그래프 생성"""
    G = nx.Graph()
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'G'), ('E', 'H'), ('F', 'I'),
        ('G', 'J'), ('H', 'J'), ('I', 'J')
    ]
    G.add_edges_from(edges)
    return G

def draw_graph(G, path=[]):
    """그래프 시각화"""
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
    if path:
        edge_list = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=2)
    st.pyplot(plt)

def find_shortest_path(G, start, end):
    """최단 경로 찾기"""
    try:
        path = nx.shortest_path(G, source=start, target=end)
        return path
    except nx.NetworkXNoPath:
        return None

st.title("미로 탐색 프로그램")

graph = create_maze_graph()
st.subheader("미로 구조")
draw_graph(graph)

start_node = st.selectbox("시작 노드 선택", list(graph.nodes))
end_node = st.selectbox("도착 노드 선택", list(graph.nodes))

if st.button("경로 찾기"):
    path = find_shortest_path(graph, start_node, end_node)
    if path:
        st.success(f"경로 찾기 성공: {' -> '.join(path)}")
        draw_graph(graph, path)
    else:
        st.error("경로를 찾을 수 없습니다.")
