import pandas as pd
from pathlib import Path

path = Path(r"D:\EmployeeDataAnalysis_Insights_Trends_Visualization\data\processed\employees_unified.csv")
df = pd.read_csv(path)

print(df.columns)
print(df['performance_score'].head(20))
print(df['performance_score'].describe())
