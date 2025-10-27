import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED = BASE_DIR / 'data' / 'processed' / 'employees_unified.csv'

def basic_insights():
    df = pd.read_csv(PROCESSED)
    print('Total employees:', len(df))
    print('Average salary:', df['salary'].dropna().mean())
    print('Median salary:', df['salary'].dropna().median())
    print('\nTop departments by headcount:\n', df['department'].value_counts().head())

if __name__ == '__main__':
    basic_insights()