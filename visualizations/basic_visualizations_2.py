import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from tabulate import tabulate
import os

# ==============================================================
# BASIC CONFIG
# ==============================================================
plt.style.use('seaborn-v0_8-whitegrid')
pd.set_option('display.max_columns', None)

DATA_PATH = r"D:\EmployeeDataAnalysis_Insights_Trends_Visualization\data\processed\employees_unified.csv"
PLOTS_DIR = "outputs/plots"
REPORTS_DIR = "outputs/reports"
os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

print(f"\n📁 Loading data from: {DATA_PATH}")
data = pd.read_csv(DATA_PATH)
print(f"✅ Data loaded successfully: {data.shape[0]} rows × {data.shape[1]} columns\n")


# ==============================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# ==============================================================
print("🔍 Running Exploratory Data Analysis (EDA)...")

eda_summary = {
    "Columns": list(data.columns),
    "Missing Values": data.isnull().sum().to_dict(),
    "Data Types": data.dtypes.astype(str).to_dict(),
    "Numeric Summary": data.describe().to_dict()
}

with open(f"{REPORTS_DIR}/eda_summary.txt", "w", encoding="utf-8") as f:
    f.write("EDA SUMMARY\n\n")
    f.write(tabulate(pd.DataFrame(data.describe()).T, headers="keys", tablefmt="grid"))
print("✅ EDA Summary saved successfully.\n")

# Display summary table in console (short version)
print(tabulate(data.describe().T.head(5), headers="keys", tablefmt="fancy_grid"))


# ==============================================================
# BASIC VISUALIZATIONS
# ==============================================================
print("📊 Generating Basic Visualizations...")

# 1. Gender Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='gender', data=data, hue='gender', palette='Set2', legend=False)
plt.title("Gender Distribution")
plt.savefig(f"{PLOTS_DIR}/gender_distribution.png")
plt.show()

# 2. Salary Distribution
plt.figure(figsize=(6, 4))
sns.histplot(data['salary'], bins=30, kde=True, color='blue')
plt.title("Salary Distribution")
plt.savefig(f"{PLOTS_DIR}/salary_distribution.png")
plt.show()

# 3. Department-wise Average Salary
plt.figure(figsize=(8, 4))
sns.barplot(x='department', y='salary', data=data, hue='department',
            errorbar=None, palette='coolwarm', legend=False)
plt.title("Average Salary by Department")
plt.xticks(rotation=30)
plt.savefig(f"{PLOTS_DIR}/avg_salary_by_department.png")
plt.show()

print("✅ Basic Visualizations Generated Successfully.\n")


# ==============================================================
# STATISTICAL ANALYSIS
# ==============================================================
print("📈 Running Statistical Analysis...")

numeric_cols = data.select_dtypes(include=['number']).columns
stats_summary = data[numeric_cols].describe().T
print(tabulate(stats_summary, headers="keys", tablefmt="fancy_grid", showindex=True))

stats_summary.to_csv(f"{REPORTS_DIR}/statistical_summary.csv", index=True)
print("\n✅ Statistical summary saved successfully.\n")


# ==============================================================
# ADVANCED STATISTICAL ANALYSIS
# ==============================================================
print("📊 Running Advanced Statistical Analysis...")

corr_matrix = data.corr(numeric_only=True)
print("Correlation Matrix:\n")
print(tabulate(corr_matrix, headers="keys", tablefmt="grid", floatfmt=".3f"))

# Save correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig(f"{PLOTS_DIR}/correlation_heatmap.png")
plt.show()

# ANOVA: Salary across departments
anova_result = stats.f_oneway(*[group["salary"].values for name, group in data.groupby("department")])
anova_table = [["F-statistic", anova_result.statistic], ["p-value", anova_result.pvalue]]
print("\nANOVA Salary across Departments:\n")
print(tabulate(anova_table, headers=["Metric", "Value"], tablefmt="fancy_grid", floatfmt=".4f"))
print("✅ Advanced Statistical Analysis Completed.\n")


# ==============================================================
# HYPOTHESIS TESTING
# ==============================================================
print("🧪 Running Hypothesis Testing...")

# Hypothesis: Mean salary of males vs females
male_salaries = data[data['gender'] == 'Male']['salary']
female_salaries = data[data['gender'] == 'Female']['salary']
t_stat, p_val = stats.ttest_ind(male_salaries, female_salaries, equal_var=False)

hypothesis_results = [
    ["Null Hypothesis", "There is no significant difference in mean salary between genders."],
    ["Alternative Hypothesis", "There is a significant difference in mean salary between genders."],
    ["t-statistic", round(t_stat, 4)],
    ["p-value", round(p_val, 4)],
    ["Conclusion", "Reject Null Hypothesis" if p_val < 0.05 else "Fail to Reject Null Hypothesis"]
]

print(tabulate(hypothesis_results, headers=["Test Parameter", "Result"], tablefmt="fancy_grid"))

# Save hypothesis report
with open(f"{REPORTS_DIR}/hypothesis_testing.txt", "w", encoding="utf-8") as f:
    f.write(tabulate(hypothesis_results, headers=["Test Parameter", "Result"], tablefmt="grid"))

print("✅ Hypothesis testing report saved successfully.\n")


# ==============================================================
# TEAM ANALYSIS
# ==============================================================
print("👥 Running Team Analysis...")

team_summary = (
    data.groupby('department')
    .agg(avg_salary=('salary', 'mean'),
         avg_experience=('years_experience', 'mean'),
         employee_count=('employee_id', 'count'))
    .reset_index()
)

print(tabulate(team_summary.head(10), headers="keys", tablefmt="fancy_grid", floatfmt=".2f"))

team_summary.to_csv(f"{REPORTS_DIR}/team_analysis.csv", index=False)
print("\n✅ Team Analysis Completed.\n")

print("🏁 All reports and visualizations generated successfully.")
