Zellora – Your AI Text Assistant

Zellora is a smart, LLM-powered chatbot app built Streamlit and Langchain library.  
It uses **Zephyr-7B**, an open-source model from Hugging Face, to generate natural, intelligent responses to user prompts.


Features:-

- Chat interface using Streamlit
- Text generation using Zephyr-7B (via Hugging Face API)
- Prompt templating with LangChain
- Hugging Face token authentication via `.env`

Libraries used:-

-Streamlit: Frontend framework to build the interactive chatbot UI 
-langchain: Framework to structure LLM chains (prompt → LLM → output) 
-langchain_huggingface: Integration with Hugging Face models through LangChain 
-huggingface_hub: Connects to Hugging Face model API securely 
-dotenv: Loads API keys securely from a `.env` file
-os: Used to access environment variables in Python 
-PromptTemplate/load_prompt: Used to load a reusable prompt format for Zephyr-7B 
