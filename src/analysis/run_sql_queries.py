"""
Run all SQL files (schema + analytical queries) on employee_data.db
"""
from pathlib import Path
import sqlite3
import pandas as pd

# --- Define paths ---
BASE_DIR = Path(__file__).resolve().parents[2]  # Go 2 levels up from src/analysis
SQL_DIR = BASE_DIR / "sql"
QUERIES_DIR = SQL_DIR / "queries"
DB_PATH = BASE_DIR / "data" / "employee_data.db"

# --- Connect to database ---
conn = sqlite3.connect(DB_PATH)
print(f"✅ Connected to database: {DB_PATH}")

# --- Step 1: Run schema file (optional if already created) ---
schema_path = SQL_DIR / "create_schema.sql"
if schema_path.exists():
    try:
        with open(schema_path, "r") as file:
            schema_sql = file.read()
        conn.executescript(schema_sql)
        print("📄 Executed create_schema.sql")
    except sqlite3.OperationalError as e:
        if "already exists" in str(e):
            print("⚠️ Table already exists, skipping schema creation.")
        else:
            raise


# --- Step 2: Function to run query files ---
def run_sql(filename):
    sql_path = QUERIES_DIR / filename
    if not sql_path.exists():
        print(f"⚠️ File not found: {sql_path}")
        return
    with open(sql_path, "r") as file:
        query = file.read()
    print(f"\n▶️ Running: {filename}")
    df = pd.read_sql_query(query, conn)
    print(df.head())
    return df

# --- Step 3: Execute all .sql query files ---
queries = ["avg_salary_by_dept.sql", "gender_distribution.sql", "top_performers.sql"]
for q in queries:
    run_sql(q)

# --- Step 4: Close connection ---
conn.close()
print("\n✅ All queries executed successfully!")
