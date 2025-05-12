import streamlit as st
from openai import OpenAI

# API 키 입력 받기
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.session_state.api_key = st.text_input(
    "OpenAI API Key를 입력하세요", type="password", value=st.session_state.api_key
)

if not st.session_state.api_key:
    st.warning("API 키를 입력하세요.")
    st.stop()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=st.session_state.api_key)

# 질문 입력
user_input = st.text_input("질문을 입력하세요:")

@st.cache_data(show_spinner="GPT 응답을 생성 중입니다...")
def get_gpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",  # GPT-4.1-mini 대응 모델
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

if user_input:
    answer = get_gpt_response(user_input)
    st.markdown("### 💬 GPT 응답:")
    st.write(answer)
