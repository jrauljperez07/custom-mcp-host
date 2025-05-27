# path: datasources/snowflake/introspection.py
from datasources.snowflake.adapter import get_connection

def get_columns(table_name: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f'DESCRIBE TABLE {table_name}')
            return [row[0] for row in cur.fetchall()]