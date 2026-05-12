from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Bella AI Product"
    debug: bool = True
    api_version: str = "v1"


settings = Settings()