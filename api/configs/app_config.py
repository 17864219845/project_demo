from pydantic_settings import SettingsConfigDict
from configs.pydantic_config import DeploymentConfig, DatabaseConfig


class EnvConfig(
    DeploymentConfig,
    DatabaseConfig
):
    model_config = SettingsConfigDict(
        # read from dotenv format config file
        env_file=".env",
        env_file_encoding="utf-8",
        # ignore extra attributes
        extra="ignore",
    )
