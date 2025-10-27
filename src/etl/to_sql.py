"""
Load processed CSV into SQLite and run example queries
"""
from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / 'data' / 'employee_data.db'
PROCESSED = BASE_DIR / 'data' / 'processed' / 'employees_unified.csv'

if not PROCESSED.exists():
    raise FileNotFoundError(f"Processed file not found: {PROCESSED}\nRun clean_data.py first.")

# Load
df = pd.read_csv(PROCESSED)
conn = sqlite3.connect(DB_PATH)
df.to_sql('employees', conn, if_exists='replace', index=False)
print('Loaded', len(df), 'rows into', DB_PATH)

# Example query
q = '''
SELECT department, COUNT(*) AS total, ROUND(AVG(salary),2) AS avg_salary
FROM employees
GROUP BY department
ORDER BY total DESC
LIMIT 10;
'''

print(pd.read_sql(q, conn))
conn.close()

