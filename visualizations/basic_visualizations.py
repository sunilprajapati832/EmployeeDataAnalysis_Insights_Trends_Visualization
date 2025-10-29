import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------------------
def load_data(file_path):
    print(f"Loading data from: {file_path}")
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully: {df.shape[0]} rows × {df.shape[1]} columns\n")
    return df


def save_report(content, filename):
    output_dir = Path("outputs/reports")
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / filename
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Report saved at: {file_path}\n")


# ---------------------------------------------------------------------
# Exploratory Data Analysis (EDA)
# ---------------------------------------------------------------------
def exploratory_data_analysis(df):
    print("Running Exploratory Data Analysis (EDA)...")
    report = []
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_cols:
        print("No numeric columns found for EDA.")
        return

    report.append(f"Numeric columns with valid data: {numeric_cols}\n")

    for col in numeric_cols:
        series = df[col].dropna()
        if not series.empty:
            report.append(
                f"{col}: Mean={series.mean():.2f}, Median={series.median():.2f}, "
                f"Std={series.std():.2f}, Var={series.var():.2f}"
            )

    eda_path = Path("outputs/reports/eda_summary.txt")
    eda_path.parent.mkdir(parents=True, exist_ok=True)
    with open(eda_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print("EDA Summary Completed Successfully.\n")
    print(f"EDA summary saved at: {eda_path}\n")
    return numeric_cols


# ---------------------------------------------------------------------
# Basic Visualizations
# ---------------------------------------------------------------------
def basic_visualizations(df):
    print("Generating Basic Visualizations...")
    output_dir = Path("outputs/plots")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Salary Distribution
    if "salary" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df["salary"], bins=30, kde=True, color="skyblue")
        plt.title("Salary Distribution")
        plt.xlabel("Salary")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(output_dir / "salary_distribution.png")
        plt.close()

        # Salary Boxplot
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df["salary"], color="lightgreen")
        plt.title("Salary Boxplot")
        plt.tight_layout()
        plt.savefig(output_dir / "salary_boxplot.png")
        plt.close()

    # Bonus vs Salary
    if {"bonus_percent", "salary"}.issubset(df.columns):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x="bonus_percent", y="salary", data=df, alpha=0.6)
        plt.title("Salary vs Bonus Percent")
        plt.tight_layout()
        plt.savefig(output_dir / "salary_vs_bonus.png")
        plt.close()

    # Gender Count
    if "gender" in df.columns:
        plt.figure(figsize=(6, 4))
        df["gender"].value_counts().plot(kind="bar", color="salmon", edgecolor="black")
        plt.title("Gender Distribution")
        plt.tight_layout()
        plt.savefig(output_dir / "gender_distribution.png")
        plt.close()

    print("Basic Visualizations Generated Successfully.\n")


# ---------------------------------------------------------------------
# Statistical Analysis
# ---------------------------------------------------------------------
def statistical_analysis(df):
    print("Running Statistical Analysis...")
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    summary_data = []
    for col in numeric_cols:
        series = df[col].dropna()
        if series.empty:
            continue
        summary_data.append({
            "Column": col,
            "Mean": series.mean(),
            "Median": series.median(),
            "StdDev": series.std(),
            "Skewness": series.skew(),
            "Kurtosis": series.kurt()
        })

    summary_df = pd.DataFrame(summary_data)
    output_path = Path("outputs/reports/statistical_summary.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(output_path, index=False)

    print("Statistical summary saved successfully.\n")
    return summary_df


# ---------------------------------------------------------------------
# Advanced Statistical Analysis
# ---------------------------------------------------------------------
def advanced_statistical_analysis(df):
    print("Running Advanced Statistical Analysis...")
    output_dir = Path("outputs/plots")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Correlation Matrix
    corr = df.corr(numeric_only=True)
    print("\nCorrelation Matrix:")
    print(corr, "\n")

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_dir / "correlation_heatmap.png")
    plt.close()

    # Violin Plot: Salary distribution by department
    if "department" in df.columns and "salary" in df.columns:
        plt.figure(figsize=(10, 6))
        sns.violinplot(x="department", y="salary", data=df, inner="quartile", palette="cool")
        plt.title("Salary Distribution by Department")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_dir / "salary_violin_by_department.png")
        plt.close()

    # ANOVA: Salary across departments
    if "department" in df.columns and "salary" in df.columns:
        groups = [vals["salary"].dropna().values for _, vals in df.groupby("department")]
        if len(groups) > 1:
            f_stat, p_val = stats.f_oneway(*groups)
            print(f"ANOVA Salary across Departments: F={f_stat:.2f}, p={p_val:.4f}")
        else:
            print("ANOVA skipped: Not enough departments.")
    print("Advanced Statistical Analysis Completed.\n")


# ---------------------------------------------------------------------
# Hypothesis Testing
# ---------------------------------------------------------------------
def hypothesis_testing(df):
    print("Running Hypothesis Testing...")
    report = []

    # Salary by gender
    if {"gender", "salary"}.issubset(df.columns):
        male_salary = df[df["gender"] == "Male"]["salary"].dropna()
        female_salary = df[df["gender"] == "Female"]["salary"].dropna()
        if len(male_salary) > 1 and len(female_salary) > 1:
            t_stat, p_val = stats.ttest_ind(male_salary, female_salary, equal_var=False)
            result = "Reject H0 (Significant Difference)" if p_val < 0.05 else "Fail to Reject H0 (No Significant Difference)"
            report.append(f"Hypothesis Test: Male vs Female Salary\nT={t_stat:.2f}, P={p_val:.4f}, Conclusion: {result}\n")

    output_path = Path("outputs/reports/hypothesis_testing_report.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print("Hypothesis testing report saved successfully.\n")


# ---------------------------------------------------------------------
# Team Analysis
# ---------------------------------------------------------------------
def team_analysis_tools(df):
    print("Running Team Analysis...")
    output_dir = Path("outputs/plots")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Average salary by department
    if {"department", "salary"}.issubset(df.columns):
        avg_salary = df.groupby("department")["salary"].mean().sort_values()
        plt.figure(figsize=(8, 5))
        avg_salary.plot(kind="bar", color="skyblue")
        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Average Salary")
        plt.tight_layout()
        plt.savefig(output_dir / "avg_salary_by_department.png")
        plt.close()

    # Gender distribution by department
    if {"department", "gender"}.issubset(df.columns):
        gender_dist = pd.crosstab(df["department"], df["gender"])
        gender_dist.plot(kind="bar", stacked=True, figsize=(10, 6))
        plt.title("Gender Distribution by Department")
        plt.xlabel("Department")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(output_dir / "gender_distribution_by_department.png")
        plt.close()

    print("Team Analysis Completed.\n")


# ---------------------------------------------------------------------
# Main Function
# ---------------------------------------------------------------------
def main():
    base_dir = Path(__file__).resolve().parents[1]
    data_path = base_dir / "data" / "processed" / "employees_unified.csv"

    df = load_data(data_path)

    exploratory_data_analysis(df)
    basic_visualizations(df)
    statistical_analysis(df)
    advanced_statistical_analysis(df)
    hypothesis_testing(df)
    team_analysis_tools(df)

    print("All reports and visualizations generated successfully.")


# ---------------------------------------------------------------------
if __name__ == "__main__":
    main()
