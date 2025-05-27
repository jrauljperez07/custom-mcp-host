"""
Config module for the application.
path: core/config.py
"""

from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    snowflake_user: str = Field(..., env="SNOWFLAKE_USER")
    snowflake_password: str = Field(..., env="SNOWFLAKE_PASSWORD")
    snowflake_account: str = Field(..., env="SNOWFLAKE_ACCOUNT")
    snowflake_warehouse: str = Field(..., env="SNOWFLAKE_WAREHOUSE")
    snowflake_database: str = Field(..., env="SNOWFLAKE_DATABASE")
    snowflake_schema: str = Field(..., env="SNOWFLAKE_SCHEMA")
    snowflake_role: str = Field(..., env="SNOWFLAKE_ROLE")

    app_name: str = "MCP Host"
    environment: str = Field("development", env="ENVIRONMENT")

    class Config:
        env_file = ".env"

settings = Settings()
