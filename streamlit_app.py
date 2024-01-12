import streamlit as st
from langchain.llms import OpenAI

st.title('QUICKSTART APP')
# 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
openai_api_key = st.sidebar.text_input('API Key:')

print(len(openai_api_key))
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form('my_form'):
    text = st.text_area(
        'Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
