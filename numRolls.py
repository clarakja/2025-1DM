import streamlit as st
import random
import collections
import matplotlib.pyplot as plt

st.title("주사위 시뮬레이터")

# 사용자 입력
num_rolls = st.number_input("주사위를 몇 번 던질까요?", min_value=1, value=1000)

if st.button("던지기"):
    results = [random.randint(1, 6) for _ in range(num_rolls)]
    counts = collections.Counter(results)

    st.write("주사위 던지기 결과:")
    for number in range(1, 7):
        st.write(f"{number}: {counts[number]} 번")

    # 결과 시각화
    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values(), color='skyblue')
    plt.xlabel("주사위 값")
    plt.ylabel("빈도")
    plt.title(f"{num_rolls}번의 주사위 던지기 결과")
    st.pyplot(fig)
