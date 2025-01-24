import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Streamlit 앱 제목
st.title("친구 관계 네트워크 시각화")

# 그래프 생성
G = nx.Graph()
G.add_edges_from([('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'), ('Charlie', 'Eve')])

# 네트워크 그래프 시각화
st.subheader("친구 관계 네트워크")

plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
st.pyplot(plt)

# 사용자 입력을 통한 네트워크 추가
st.subheader("관계를 추가해보세요")
node1 = st.text_input("첫 번째 친구 이름")
node2 = st.text_input("두 번째 친구 이름")

if st.button("관계 추가"):
    G.add_edge(node1, node2)
    plt.figure(figsize=(6, 4))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
    st.pyplot(plt)
