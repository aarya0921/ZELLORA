from zellora_llm import HuggingFaceLLM
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import load_prompt

# Load environment variables
load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

st.set_page_config(page_title="Zellora", layout="centered")
st.title("Zellora: Your AI Text Assistant")

user_input = st.text_input("Ask me:")

# Load your prompt template
template = load_prompt("prompt_template.json")

# Initialize your custom LLM
llm = HuggingFaceLLM(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    api_token=api_key,
    max_tokens=1024,
    temperature=0.5
)

# When button is clicked
if st.button("Search") and user_input:
    with st.spinner("Thinking..."):
        final_prompt = template.format(text=user_input)
        response = llm(final_prompt)
        st.write(response)
