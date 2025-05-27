"""
Main entry point for the FastAPI application. 
path: main.py
"""
import logging
from fastapi import FastAPI
from mcp.router import router as mcp_router
from routers.health_router import router as health_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="MCP Host - Pistil Data",
    version="1.0.0",
    description="MCP host exposing tools to query Pistil Data data securely"
)

app.include_router(mcp_router, prefix="/tools")
app.include_router(health_router)