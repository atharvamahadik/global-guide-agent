from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    OPENWEATHERMAP_API_KEY: str = "mock_key"
    GOOGLE_PLACES_API_KEY: str = "mock_key"
    
    class Config:
        env_file = ".env"

settings = Settings()