import streamlit as st
import openai
import os

# OpenAI API 키 설정 (환경변수 또는 직접 입력)
openai.api_key = os.getenv("OPENAI_API_KEY")
    
st.set_page_config(page_title="ChatBot with OpenAI", layout="centered")
st.title("🤖 Chat with OpenAI")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear 버튼
if st.button("Clear Chat"):
    st.session_state.messages = []

# 이전 메시지 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
if prompt := st.chat_input("메시지를 입력하세요"):
    # 사용자 메시지 저장 및 출력
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 응답 받기
    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 또는 gpt-4
            messages=st.session_state.messages,
            stream=True,
        )

        full_response = ""
        msg_placeholder = st.empty()

        for chunk in response:
            delta = chunk.choices[0].delta.get("content", "")
            full_response += delta
            msg_placeholder.markdown(full_response + "▌")

        msg_placeholder.markdown(full_response)

    # 어시스턴트 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": full_response})
