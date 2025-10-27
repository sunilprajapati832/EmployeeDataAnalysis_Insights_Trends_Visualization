-- Simple create for employees (for other DBs)
CREATE TABLE employees (
employee_id TEXT PRIMARY KEY,
first_name TEXT,
age INTEGER,
gender TEXT,
department TEXT,
job_level TEXT,
years_experience REAL,
salary REAL,
bonus_percent REAL,
performance_score REAL,
source_file TEXT
);