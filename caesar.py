import streamlit as st

# 시저 암호 암호화 함수
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# 시저 암호 복호화 함수
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Streamlit 앱 제목
st.title("시저 암호 구현")

# 암호화와 복호화 선택
operation = st.radio("작업 선택", ("암호화", "복호화"))

# 사용자 입력 받기
text = st.text_input("텍스트 입력", "Hello, World!")
shift = st.number_input("이동 값 (Shift) 입력", min_value=1, max_value=25, value=3)

if st.button("실행"):
    if operation == "암호화":
        result = caesar_encrypt(text, shift)
        st.success(f"암호화된 텍스트: {result}")
    elif operation == "복호화":
        result = caesar_decrypt(text, shift)
        st.success(f"복호화된 텍스트: {result}")
