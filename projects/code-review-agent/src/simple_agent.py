from .llm_client import LLMClient


def review_code(code: str) -> str:
    client = LLMClient()
    return client.chat(f"请审查以下代码：\n{code}")
