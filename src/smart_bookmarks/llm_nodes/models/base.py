from openai import OpenAI
from src.smart_bookmarks.config import settings

class LLM:
    def __init__(
            self, 
            base_url: str = settings.llm.api_base_url, 
            api_key: str = settings.llm.api_key,
            model_name: str = settings.llm.model_name,
        ):
        self.base_url = base_url
        self.api_key = api_key
        self.model_name = model_name
        self.client: OpenAI = OpenAI(base_url=base_url, api_key=api_key)

    async def invoke(self, prompt: str) -> str:
        return await self.client.responses.create(
            model=self.model_name,
            input=prompt
        )


if __name__ == "__main__":
    import asyncio

    llm = LLM()
    response = asyncio.run(llm.invoke("Hello, how are you?"))
    print(response)