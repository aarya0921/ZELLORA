from langchain_core.language_models.llms import LLM
from typing import Optional, List
from huggingface_hub import InferenceClient

class HuggingFaceLLM(LLM):
    def __init__(self, repo_id: str, api_token: str, max_tokens: int = 300, temperature: float = 0.7):
        self.client = InferenceClient(model=repo_id, token=api_token)
        self.max_tokens = max_tokens
        self.temperature = temperature

    @property
    def _llm_type(self) -> str:
        return "huggingface_hub_custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self.client.text_generation(
            prompt=prompt,
            max_new_tokens=self.max_tokens,
            temperature=self.temperature,
            stop_sequences=stop,
        )
        return response
