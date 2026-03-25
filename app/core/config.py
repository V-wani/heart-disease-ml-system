from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Heart ML System"
    DEBUG: bool = True

settings = Settings()
