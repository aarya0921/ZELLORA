from huggingface_hub import InferenceClient

class HuggingFaceLLM:
    def __init__(self, repo_id, api_token, max_tokens=1024, temperature=0.5):
        self.client = InferenceClient(repo_id, token=api_token)
        self.max_tokens = max_tokens
        self.temperature = temperature

    def __call__(self, prompt):
        response = self.client.text_generation(
            prompt,
            max_new_tokens=self.max_tokens,
            temperature=self.temperature,
            do_sample=True
        )
        return response
