# path: datasources/snowflake/services.py
from fastapi import HTTPException
from datasources.snowflake.queries import TABLE_COLUMN_WHITELIST
from datasources.snowflake.adapter import get_connection

def validate_dataset(dataset: str):
    """Validate the dataset name against the whitelist."""
    key = dataset.upper()
    if key not in TABLE_COLUMN_WHITELIST:
        raise HTTPException(status_code=404, detail=f"Dataset '{dataset}' not found.")
    return key

def validate_table(dataset_key: str, table: str):
    """Validate the table name against the whitelist for the given dataset."""
    table_key = table.upper()
    tables = TABLE_COLUMN_WHITELIST[dataset_key]
    if table_key not in tables:
        raise HTTPException(status_code=404, detail=f"Table '{table}' not found in dataset '{dataset_key}'.")
    return table_key, tables[table_key]

def list_datasets():
    """List all datasets in the whitelist."""
    return list(TABLE_COLUMN_WHITELIST.keys())

def list_tables(dataset_key: str):
    """List all tables in the given dataset."""
    return list(TABLE_COLUMN_WHITELIST[dataset_key].keys())

def get_table_columns(dataset_key: str, table_key: str):
    """Get the columns for the given table in the dataset."""
    return TABLE_COLUMN_WHITELIST[dataset_key][table_key]

def execute_query(sql: str):
    """Execute a SQL query and return the results."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                columns = [desc[0] for desc in cur.description]
                rows = cur.fetchall()
                return {
                    "columns": columns,
                    "data": [dict(zip(columns, row)) for row in rows]
                }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
