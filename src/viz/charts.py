import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED = BASE_DIR / 'data' / 'processed' / 'employees_unified.csv'

def plot_headcount_by_dept():
    df = pd.read_csv(PROCESSED)
    counts = df['department'].fillna('Unknown').value_counts().head(20)
    plt.figure(figsize=(10,5))
    counts.plot.bar()
    plt.title('Headcount by Department')
    plt.xlabel('Department')
    plt.ylabel('Employees')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_headcount_by_dept()