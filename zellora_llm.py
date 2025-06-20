from huggingface_hub import InferenceClient

class HuggingFaceLLM:
    def __init__(self, repo_id, api_token, max_tokens=1024, temperature=0.7):
        self.client = InferenceClient(model=repo_id, token=api_token)
        self.max_tokens = max_tokens
        self.temperature = temperature

    def _call(self, prompt, stop=None):
        response = self.client.text_generation(
            prompt,
            max_new_tokens=self.max_tokens,
            temperature=self.temperature,
            stop_sequences=stop if stop else None,
        )
        return response

    def __call__(self, prompt):
        return self._call(prompt)
