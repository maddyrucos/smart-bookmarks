from pydantic import Field
from pydantic_settings import BaseSettings

from dotenv import load_dotenv
load_dotenv()

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


class BackendSettings(BaseSettings):
    host: str = Field(default="0.0.0.0", validation_alias="BACKEND_HOST")
    port: int = Field(default=8000, validation_alias="BACKEND_PORT")
    reload: bool = Field(default=True, validation_alias="BACKEND_RELOAD")

class Settings(BaseSettings):
    llm: LLMSettings = LLMSettings()
    backend: BackendSettings = BackendSettings()

settings = Settings()