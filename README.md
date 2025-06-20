Zellora – Your AI Text Assistant

Zellora is a smart, LLM-powered chatbot app built Streamlit and Langchain library.  
It uses **Zephyr-7B**, an open-source model from Hugging Face, to generate natural, intelligent responses to user prompts.


Features:-

- Chat interface using Streamlit
- Text generation using Zephyr-7B (via Hugging Face API)
- Prompt templating with LangChain
- Hugging Face token authentication via `.env`

## 📚 Libraries Used

- **[Streamlit](https://streamlit.io/)**  
  Used to build the interactive web interface for the chatbot. It provides easy-to-use components like text input, buttons, and layout for rapid app development.

- **[LangChain](https://docs.langchain.com/)**  
  Framework for chaining together LLM components such as prompts, models, and output parsing. Used to create a structured flow from input to response.

- **`langchain_huggingface`**  
  Enables integration of Hugging Face models (like Zephyr-7B) with LangChain for seamless model interaction and LLM-based chat.

- **[huggingface_hub](https://huggingface.co/docs/huggingface_hub/)**  
  Provides tools to securely access and interact with models hosted on Hugging Face via API.

- **[python-dotenv](https://pypi.org/project/python-dotenv/)**  
  Loads environment variables (such as Hugging Face API keys) from a `.env` file to keep sensitive data out of the source code.

- **`os` (Python standard library)**  
  Used to access environment variables from the system and interface with the `.env` configuration.

- **`PromptTemplate` / `load_prompt` (LangChain)**  
  Used to define and load a consistent, reusable prompt structure that guides the LLM’s response formatting and behavior.
