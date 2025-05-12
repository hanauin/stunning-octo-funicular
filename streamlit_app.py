import streamlit as st
import openai

st.set_page_config(page_title="GPT 질문 응답", page_icon="🤖")
st.title("💬 GPT 질문 응답 웹 앱")

# API Key 입력받기 (비밀번호 형태)
api_key = st.text_input("🔑 OpenAI API Key를 입력하세요", type="password")

# 질문 입력
question = st.text_input("❓ 질문을 입력하세요")

# GPT 응답 함수 (캐시 적용)
@st.cache_data(show_spinner="🤖 GPT가 응답 중입니다...")
def get_gpt_response(api_key: str, user_question: str) -> str:
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 또는 "gpt-4o", "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_question}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]

# 버튼 클릭 시 실행
if st.button("응답 받기"):
    if not api_key:
        st.warning("🔐 먼저 OpenAI API Key를 입력해주세요.")
    elif not question:
        st.warning("💬 질문을 입력해주세요.")
    else:
        try:
            answer = get_gpt_response(api_key, question)
            st.markdown("### ✅ GPT 응답")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")
