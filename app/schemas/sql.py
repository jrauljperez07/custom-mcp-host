"""
Schemas for SQL requests.
path: schemas/sql.py
"""
from pydantic import BaseModel, validator
import re

class RunSQLRequest(BaseModel):
    sql: str

    @validator("sql")
    def validate_select_only(cls, value):
        cleaned = value.strip().lower()

        if not cleaned.startswith("select"):
            raise ValueError("Only SELECT statements are allowed.")

        forbidden = r"\b(insert|update|delete|drop|alter|create|grant|revoke|truncate|merge|call|copy|put|remove)\b"
        if re.search(forbidden, cleaned):
            raise ValueError("Only safe read-only SELECT queries are permitted.")

        return value
