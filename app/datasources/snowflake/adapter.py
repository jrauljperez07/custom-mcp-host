"""
Python script to establish a connection to Snowflake using credentials stored in environment variables.
path: datasources/snowflake/adapter.py
"""
import logging
import snowflake.connector
from core.config import settings

logger = logging.getLogger(__name__)

def get_connection(schema: str = None):
    """Establish a connection to Snowflake using credentials from environment variables."""
    try:
        conn = snowflake.connector.connect(
            user=settings.snowflake_user,
            password=settings.snowflake_password,
            account=settings.snowflake_account,
            warehouse=settings.snowflake_warehouse,
            database=settings.snowflake_database,
            schema=schema or settings.snowflake_schema,
            role=settings.snowflake_role
        )
        return conn
    except Exception as e:
        logger.error("Failed to connect to Snowflake: %s", e, exc_info=True)
        raise
