import streamlit as st

def is_prime(n):
    """소수 판별 함수"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_up_to(limit):
    """주어진 범위 내의 소수를 찾는 함수"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Streamlit 앱 제목
st.title("소수 판별기와 소수 생성기")

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴 선택", ["소수 판별", "소수 생성"])

# 소수 판별
if menu == "소수 판별":
    st.header("소수 판별기")
    number = st.number_input("판별할 숫자를 입력하세요", min_value=0, step=1, value=0)

    if st.button("소수 여부 확인"):
        if is_prime(number):
            st.success(f"{number}은(는) 소수입니다!")
        else:
            st.error(f"{number}은(는) 소수가 아닙니다.")

# 소수 생성
elif menu == "소수 생성":
    st.header("소수 생성기")
    limit = st.number_input("소수를 생성할 최대 범위를 입력하세요", min_value=2, step=1, value=10)

    if st.button("소수 생성"):
        primes = find_primes_up_to(limit)
        st.write(f"**{limit} 이하의 소수:**", primes)
