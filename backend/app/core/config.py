from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    debug: bool = False

    database_url: str   # ← ADD THIS LINE

   # supabase_url: str
    # supabase_key: str

    claude_api_key: str
    gemini_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"   # ← THIS FIXES YOUR ERROR
    )
settings = Settings()