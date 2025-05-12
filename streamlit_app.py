import streamlit as st
import openai

# API 키 입력 받기
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.session_state.api_key = st.text_input(
    "OpenAI API Key를 입력하세요", type="password", value=st.session_state.api_key
)

if not st.session_state.api_key:
    st.warning("API 키를 입력하세요.")
    st.stop()

openai.api_key = st.session_state.api_key

# 질문 입력
user_input = st.text_input("질문을 입력하세요:")

@st.cache_data(show_spinner="GPT 응답을 생성 중입니다...")
def get_gpt_response(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",  # gpt-4.1-mini에 해당하는 최신 이름
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"]

# 응답 출력
if user_input:
    answer = get_gpt_response(user_input, st.session_state.api_key)
    st.markdown("### 💬 GPT 응답:")
    st.write(answer)
