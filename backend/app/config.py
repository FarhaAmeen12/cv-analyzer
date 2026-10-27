from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    database_url: str = 'postgresql+psycopg://cvuser:cvpass@localhost:5432/cvdb'
    jwt_secret: str = 'change-me'
    jwt_expire_minutes: int = 60
    anthropic_api_key: str = ''
    llm_model: str = 'claude-haiku-5-5'
    frontend_origin: str = 'http://localhost:5173'


settings = Settings()