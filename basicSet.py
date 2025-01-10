import streamlit as st

# Streamlit 앱 제목
st.title("집합과 간단한 데이터 구조 학습 애플리케이션")

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴 선택", [
    "기본 집합 연산",
    "중복 제거",
    "집합 관계 확인",
    "두 리스트 비교",
    "동적 집합 업데이트",
    "공통 동아리원 찾기",
    "텍스트 분석"
])

# 1. 기본 집합 연산
if menu == "기본 집합 연산":
    st.header("기본 집합 연산")
    class_A = st.text_input("집합 A 입력 (쉼표로 구분)", "Alice,Bob,Charlie").split(',')
    class_B = st.text_input("집합 B 입력 (쉼표로 구분)", "Charlie,David,Eve").split(',')

    set_A = set(class_A)
    set_B = set(class_B)

    st.write("**합집합 (Union):**", set_A | set_B)
    st.write("**교집합 (Intersection):**", set_A & set_B)
    st.write("**차집합 (Difference A-B):**", set_A - set_B)

# 2. 중복 제거
elif menu == "중복 제거":
    st.header("중복 제거")
    student_list = st.text_input("학생 이름 입력 (쉼표로 구분)", "Alice,Bob,Charlie,Alice,Eve,Bob").split(',')

    unique_students = set(student_list)

    st.write("**원래 리스트:**", student_list)
    st.write("**중복 제거 후:**", unique_students)

# 3. 집합 관계 확인
elif menu == "집합 관계 확인":
    st.header("집합 관계 확인")
    group_A = st.text_input("집합 A 입력 (쉼표로 구분)", "Alice,Bob").split(',')
    group_B = st.text_input("집합 B 입력 (쉼표로 구분)", "Alice,Bob,Charlie,David").split(',')

    set_A = set(group_A)
    set_B = set(group_B)

    st.write("**A는 B의 부분 집합인가요?:**", set_A.issubset(set_B))
    st.write("**B는 A의 상위 집합인가요?:**", set_B.issuperset(set_A))

# 4. 두 리스트 비교
elif menu == "두 리스트 비교":
    st.header("두 리스트 비교")
    class_1 = st.text_input("리스트 1 입력 (쉼표로 구분)", "Alice,Bob,Charlie").split(',')
    class_2 = st.text_input("리스트 2 입력 (쉼표로 구분)", "Charlie,David,Eve").split(',')

    set_1 = set(class_1)
    set_2 = set(class_2)

    st.write("**공통 항목 (Intersection):**", set_1 & set_2)
    st.write("**리스트 1에만 있는 항목 (Difference):**", set_1 - set_2)

# 5. 동적 집합 업데이트
elif menu == "동적 집합 업데이트":
    st.header("동적 집합 업데이트")
    initial_set = st.text_input("초기 집합 입력 (쉼표로 구분)", "Alice,Bob").split(',')

    updated_set = set(initial_set)

    new_elements = st.text_input("추가할 항목 입력 (쉼표로 구분)", "Charlie,David").split(',')
    remove_element = st.text_input("제거할 항목 입력", "Bob")

    updated_set.update(new_elements)
    if remove_element in updated_set:
        updated_set.remove(remove_element)

    st.write("**업데이트된 집합:**", updated_set)

# 6. 공통 동아리원 찾기
elif menu == "공통 동아리원 찾기":
    st.header("공통 동아리원 찾기")
    club_1 = st.text_input("동아리 1 회원 (쉼표로 구분)", "Alice,Charlie,Eve").split(',')
    club_2 = st.text_input("동아리 2 회원 (쉼표로 구분)", "Charlie,David,Alice").split(',')

    common_members = set(club_1) & set(club_2)

    st.write("**공통 동아리원:**", common_members)

# 7. 텍스트 분석
elif menu == "텍스트 분석":
    st.header("텍스트 분석")
    sentence_1 = st.text_input("문장 1 입력", "I love programming in Python")
    sentence_2 = st.text_input("문장 2 입력", "Python is great for data analysis")

    words_1 = set(sentence_1.split())
    words_2 = set(sentence_2.split())

    st.write("**공통 단어:**", words_1 & words_2)
    st.write("**고유 단어:**", words_1 ^ words_2)
