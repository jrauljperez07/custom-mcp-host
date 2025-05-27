"""FastAPI router for the MCP application."""
from fastapi import APIRouter
from datasources.snowflake.tools import router as snowflake_router

# You can include other routers here as needed
# from datasources.postgres.tools import router as postgres_router

router = APIRouter()


router.include_router(snowflake_router)
