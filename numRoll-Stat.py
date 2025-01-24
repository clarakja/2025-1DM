import streamlit as st
import random
import collections
import matplotlib.pyplot as plt

st.title("주사위 시뮬레이터와 확률 분석")

num_rolls = st.number_input("주사위를 몇 번 던질까요?", min_value=10, value=1000, step=10)

if st.button("던지기"):
    results = [random.randint(1, 6) for _ in range(num_rolls)]
    counts = collections.Counter(results)
    
    probabilities = {number: counts[number] / num_rolls for number in range(1, 7)}
    
    st.write("이론적 확률: 1/6 (16.67%)")
    for number in range(1, 7):
        st.write(f"{number}: 실험적 확률 = {probabilities[number]*100:.2f}% (횟수: {counts[number]})")

    fig, ax = plt.subplots()
    ax.bar(probabilities.keys(), probabilities.values(), color='skyblue')
    plt.axhline(1/6, color='red', linestyle='--', label='이론적 확률 (16.67%)')
    plt.xlabel("주사위 값")
    plt.ylabel("확률")
    plt.title(f"{num_rolls}번의 주사위 던지기 결과")
    plt.legend()
    st.pyplot(fig)
