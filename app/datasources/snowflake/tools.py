from fastapi import APIRouter, Query
from schemas.sql import RunSQLRequest
from datasources.snowflake.services import (
    list_datasets,
    list_tables,
    validate_dataset,
    validate_table,
    get_table_columns,
    execute_query
)

router = APIRouter()

@router.post("/run_custom_query")
def run_custom_query(request: RunSQLRequest):
    return execute_query(request.sql)

@router.get("/schema/datasets")
def get_datasets():
    return {"datasets": list_datasets()}


@router.get("/schema/tables")
def get_tables(dataset: str = Query(..., description="Dataset name")):
    dataset_key = validate_dataset(dataset)
    return {
        "dataset": dataset_key,
        "tables": list_tables(dataset_key)
    }


@router.get("/schema/columns")
def get_columns(
    dataset: str = Query(...),
    table: str = Query(...)
):
    dataset_key = validate_dataset(dataset)
    table_key, _ = validate_table(dataset_key, table)
    return {
        "dataset": dataset_key,
        "table": table_key,
        "columns": get_table_columns(dataset_key, table_key)
    }
