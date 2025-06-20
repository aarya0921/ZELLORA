from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template="{text} in detail ",
    input_variables=["text"],
    validate_template=True
)
template.save("prompt_template.json")