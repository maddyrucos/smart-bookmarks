import asyncio

from openai import AsyncOpenAI, OpenAIError

from smart_bookmarks.config import settings


class LLM:
    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        model_name: str | None = None,
    ) -> None:
        self.model_name = model_name or settings.llm.model_name
        self.client = AsyncOpenAI(
            base_url=base_url if base_url is not None else settings.llm.api_base_url,
            api_key=api_key if api_key is not None else settings.llm.api_key,
        )

    async def invoke(self, prompt: str) -> str:
        try:
            response = await self.client.responses.create(
                model=self.model_name,
                input=prompt,
            )
        except OpenAIError:
            raise

        answer = response.output_text
        if not answer or not answer.strip():
            raise RuntimeError("The LLM response did not contain text.")

        return answer.strip()

    async def close(self) -> None:
        await self.client.close()


async def main() -> None:
    llm = LLM()
    try:
        answer = await llm.invoke("Hello, how are you?")
        print(answer)
    finally:
        await llm.close()


if __name__ == "__main__":
    asyncio.run(main())