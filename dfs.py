import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import time

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

def draw_graph(G, path=[], visited_nodes=[]):
    """그래프 시각화"""
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
    if visited_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='yellow')
    if path:
        edge_list = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=2)
    st.pyplot(plt)

def dfs(graph, start, end, path=None, visited=None):
    """깊이 우선 탐색 (DFS)"""
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    draw_graph(graph, path=path, visited_nodes=list(visited))
    time.sleep(1)

    if start == end:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, path, visited)
            if result:
                return result

    path.pop()
    return None

st.title("미로 탐색 프로그램 - 깊이 우선 탐색")

graph = create_maze_graph()
st.subheader("미로 구조")
draw_graph(graph)

start_node = st.selectbox("시작 노드 선택", list(graph.nodes))
end_node = st.selectbox("도착 노드 선택", list(graph.nodes))

if st.button("DFS 탐색 시작"):
    path = dfs(graph, start_node, end_node)
    if path:
        st.success(f"최종 경로: {' -> '.join(path)}")
        draw_graph(graph, path=path)
    else:
        st.error("경로를 찾을 수 없습니다.")
