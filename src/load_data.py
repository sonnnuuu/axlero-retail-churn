"""Load the raw Online Retail II CSV into a local PostgreSQL database.

Usage (from the project root, in Git Bash or cmd):
    set PGPASSWORD=your_password      (cmd)
    export PGPASSWORD=your_password   (Git Bash)
    python src/load_data.py
"""
import os
import re

import pandas as pd
from sqlalchemy import create_engine, text

# ---- Settings: change these if yours are different ----
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "retail_db"
TABLE_NAME = "online_retail_raw"
CSV_PATH = os.path.join("data", "raw", "online_retail_II.csv")
CHUNK_SIZE = 50_000


def clean_column_name(name: str) -> str:
    """Turn 'Customer ID' into 'customer_id' so SQL queries are easy to write."""
    name = name.strip().lower()
    return re.sub(r"[^a-z0-9]+", "_", name).strip("_")


def main() -> None:
    password = os.environ.get("PGPASSWORD")
    if not password:
        raise SystemExit("Set the PGPASSWORD environment variable first.")

    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Start fresh so re-running the script does not duplicate rows
    with engine.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {TABLE_NAME}"))

    total = 0
    for chunk in pd.read_csv(CSV_PATH, chunksize=CHUNK_SIZE, encoding="latin-1"):
        chunk.columns = [clean_column_name(c) for c in chunk.columns]
        chunk.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
        total += len(chunk)
        print(f"Loaded {total:,} rows...")

    with engine.connect() as conn:
        count = conn.execute(text(f"SELECT COUNT(*) FROM {TABLE_NAME}")).scalar()
    print(f"Done. {TABLE_NAME} now has {count:,} rows.")


if __name__ == "__main__":
    main()
