import streamlit as st

def is_prime_with_reason(n):
    """소수 판별 함수와 이유 제공"""
    if n <= 1:
        return False, "1 이하의 숫자는 소수가 아닙니다."
    if n <= 3:
        return True, "2와 3은 소수입니다."
    if n % 2 == 0:
        return False, f"{n}은(는) 2로 나누어 떨어지므로 소수가 아닙니다."
    if n % 3 == 0:
        return False, f"{n}은(는) 3으로 나누어 떨어지므로 소수가 아닙니다."
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False, f"{n}은(는) {i}로 나누어 떨어지므로 소수가 아닙니다."
        if n % (i + 2) == 0:
            return False, f"{n}은(는) {i + 2}로 나누어 떨어지므로 소수가 아닙니다."
        i += 6
    return True, f"{n}은(는) 자신을 제외한 어떠한 수로도 나누어 떨어지지 않으므로 소수입니다."

def find_primes_up_to(limit):
    """주어진 범위 내의 소수를 찾는 함수"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime_with_reason(num)[0]:
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
        is_prime, reason = is_prime_with_reason(number)
        st.markdown(f"{number}은(는) 소수입니다!<br>이유: {reason}", unsafe_allow_html=True)
    else:
        st.markdown(f"{number}은(는) 소수가 아닙니다.<br>이유: {reason}", unsafe_allow_html=True)

# 소수 생성
elif menu == "소수 생성":
    st.header("소수 생성기")
    limit = st.number_input("소수를 생성할 최대 범위를 입력하세요", min_value=2, step=1, value=10)

    if st.button("소수 생성"):
        primes = find_primes_up_to(limit)
        st.write(f"**{limit} 이하의 소수:**", primes)
