from .base import LLM

from src.smart_bookmarks.config import settings

class Embedder(LLM):
    def __init__(
            self,
            base_url: str = settings.llm.api_base_url,
            api_key: str = settings.llm.api_key,
            model_name: str = settings.llm.embedder_model_name,
        ):
        super().__init__(base_url=base_url, api_key=api_key, model_name=model_name)

    async def embed(self, text: str) -> list[float]:
        response = await self.client.embeddings.create(
            model=self.model_name,
            input=text
        )
        return response.data[0].embedding

if __name__ == "__main__":
    import asyncio

    embedder = Embedder()
    embedding = asyncio.run(embedder.embed("Hello, how are you?"))
    print(embedding)