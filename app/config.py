from string import ascii_letters, digits

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings"""

    model_config = SettingsConfigDict(
        env_prefix="SHORTLINK_",
        secrets_dir="/run/secrets",  # Support container secrets when available
        env_file=".env",  # For local development
        env_file_encoding="utf-8",
    )

    db_driver: str = "postgresql+asyncpg"
    db_host: str
    db_port: int = 5432
    db_user: str
    db_name: str
    db_password: SecretStr
    log_sql: bool = False


settings = Settings()

# The characters allowed to be present in the short url id.
SHORT_LINK_CHARACTERS = ascii_letters + digits
