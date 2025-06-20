#import necessary libraries
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

# Load environment variables
load_dotenv()

# Set up the Streamlit app
st.set_page_config(page_title="Zellora: Your AI Text Assistant",layout="centered")
st.title("Zellora: Your AI Text Assistant")

# Load the Hugging Face API key from environment variables
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

#Take user input 
user_input = st.text_input("Ask me:")
# Load the prompt template from a JSON file 
template=load_prompt("prompt_template.json")

# Configure the Hugging Face LLM endpoint (Zephyr-7B)
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
   huggingfacehub_api_token=api_key,
    task="text-generation",
    max_new_tokens=3000,
    temperature=0.5
 )

# Wrap the LLM in a LangChain chat wrapper
chat = ChatHuggingFace(llm=llm)

#When the user clicks the button, send the input to the LLM
if st.button('Search'):
    with st.spinner("Thinking..."):
        chain = template |chat                    # Create chain: prompt → LLM
        response = chain.invoke(user_input)
        st.write(response.content)                # Display output in the app
