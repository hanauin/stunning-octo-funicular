import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# API 키가 입력되면, OpenAI API 키 설정
if openai.api_key:
    # 세션 상태 초기화 (대화 내용 저장)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Clear 버튼 클릭 시 대화 초기화
    if st.button("Clear Chat"):
        st.session_state.messages = []

    # 기존 대화 출력
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 사용자 입력 받기
    if prompt := st.chat_input("메시지를 입력하세요"):
        # 사용자 메시지 저장
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # OpenAI API로 응답 받기
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 또는 gpt-4
            messages=st.session_state.messages,
        )

        assistant_response = response['choices'][0]['message']['content']
        st.markdown(assistant_response)

        # 어시스턴트 응답 저장
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

else:
    st.warning("API 키를 입력해주세요.")
