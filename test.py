from pathlib import Path

RAW_DIR = Path(r"D:\EmployeeDataAnalysis_Insights_Trends_Visualization\data\raw")

print("Checking files in:", RAW_DIR)
for f in RAW_DIR.glob("*"):
    print(f.name)
