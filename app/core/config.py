from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Online Shop App"
    debug: bool = True

settings = Settings()
