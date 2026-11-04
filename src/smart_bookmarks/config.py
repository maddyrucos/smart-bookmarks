from pydantic_settings import BaseSettings, Field

class LLMSettings(BaseSettings):
    model_name: str = Field(
        default="openai/gpt-oss-20b", 
        validation_alias="LLM_MODEL_NAME"
    )
    embedder_model_name: str = Field(
        default="text-embedding-3-small", 
        validation_alias="EMBEDDER_MODEL_NAME"
    )
    api_key: str | None = Field(None, validation_alias="LLM_API_KEY")
    api_base_url: str | None = Field(None, validation_alias="LLM_API_BASE_URL")

class Settings(BaseSettings):
    llm: LLMSettings = LLMSettings()

settings = Settings()