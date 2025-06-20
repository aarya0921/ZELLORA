from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import load_prompt

# Load environment variables
load_dotenv()

# Use secrets from Streamlit Cloud
api_key = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Set page config
st.set_page_config(page_title="Zellora: Your AI Text Assistant")
st.title("Zellora: Your AI Text Assistant")

# Take user input
user_input = st.text_input("Ask me:")

# Load prompt
template = load_prompt("prompt_template.json")

# Initialize HuggingFaceHub LLM
llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=api_key,
    model_kwargs={"max_new_tokens": 1024, "temperature": 0.5}
)

# Create chain
chat = LLMChain(llm=llm, prompt=template)

# Generate response
if st.button("Search") and user_input:
    with st.spinner("Thinking..."):
        response = chat.invoke({"text": user_input})
        st.write(response["text"])
