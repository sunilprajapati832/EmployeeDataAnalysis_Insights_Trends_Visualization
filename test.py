# visualizations/basic_visualizations.py
"""
Professional single-file pipeline for Employee Data Analysis:
- Loads processed dataset (employees_unified.csv)
- Runs EDA and saves eda_summary.txt
- Generates & saves basic visualizations (also displays them)
- Runs statistical summaries and saves statistical_summary.csv
- Runs advanced statistical analysis (correlation, ANOVA, violin plots)
- Runs hypothesis tests and saves hypothesis_testing_report.txt
- Runs team-level analyses and saves plots & report
- Minimal, clean console output with section timings
- Uses only standard data-science libraries + colorama for colored but professional logs
"""

import time
from pathlib import Path
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from colorama import init as colorama_init, Fore, Style
from datetime import datetime

# Initialize colorama (keeps output professional and readable)
colorama_init(autoreset=True)
# Suppress numpy/pandas runtime warnings that don't affect outputs
warnings.filterwarnings("ignore")

# -----------------------
# Configuration / Paths
# -----------------------
BASE_DIR = Path.cwd()

DATA_PATH = BASE_DIR / "data" / "processed" / "employees_unified.csv"

OUTPUT_PLOTS = BASE_DIR / "outputs" / "plots"
OUTPUT_REPORTS = BASE_DIR / "outputs" / "reports"

# Create output directories if missing
OUTPUT_PLOTS.mkdir(parents=True, exist_ok=True)
OUTPUT_REPORTS.mkdir(parents=True, exist_ok=True)

# Matplotlib styling
sns.set(style="whitegrid")


# -----------------------
# Utility helpers
# -----------------------
def _log(msg: str, level: str = "info"):
    """Minimal colored logging: info, ok, warn, err."""
    if level == "ok":
        print(Fore.GREEN + msg + Style.RESET_ALL)
    elif level == "warn":
        print(Fore.YELLOW + msg + Style.RESET_ALL)
    elif level == "err":
        print(Fore.RED + msg + Style.RESET_ALL)
    else:
        print(msg)


def _timeit(func):
    """Decorator to print start/end and duration for steps."""
    def wrapper(*args, **kwargs):
        name = func.__name__.replace("_", " ").title()
        _log(f"STEP: {name} - started", "info")
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        _log(f"STEP: {name} - completed in {t1 - t0:.2f}s", "ok")
        print("")  # blank line between steps
        return result
    return wrapper


# -----------------------
# Core pipeline pieces
@_timeit
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Processed file not found at: {path}")
    df = pd.read_csv(path)
    # Basic canonicalization: lower-case column names and strip
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df


@_timeit
def exploratory_data_analysis(df: pd.DataFrame) -> None:
    """Saves a compact EDA summary to outputs/reports/eda_summary.txt"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = [c for c in df.columns if c not in numeric_cols]

    lines = []
    lines.append("Exploratory Data Analysis (EDA) Summary")
    lines.append("=" * 60)
    lines.append(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    lines.append(f"Numeric columns: {numeric_cols}")
    lines.append(f"Categorical columns: {categorical_cols}")
    lines.append("")

    # Numeric summaries
    if numeric_cols:
        lines.append("Numeric summaries (mean, median, std, min, max, non-null):")
        for col in numeric_cols:
            s = df[col].dropna()
            if s.empty:
                lines.append(f"{col}: no valid numeric values")
                continue
            lines.append(
                f"{col}: mean={s.mean():.2f}, median={s.median():.2f}, std={s.std():.2f}, "
                f"min={s.min():.2f}, max={s.max():.2f}, count={s.count()}"
            )
        lines.append("")

    # Categorical summaries (top values)
    if categorical_cols:
        lines.append("Categorical summaries (top 3 values):")
        for col in categorical_cols:
            top = df[col].value_counts(dropna=True).head(3)
            top_str = "; ".join([f"{idx}({val})" for idx, val in top.items()])
            lines.append(f"{col}: {top_str}")
        lines.append("")

    # Missing values overview
    lines.append("Missing values (per column):")
    mv = df.isna().sum()
    for col, cnt in mv.items():
        if cnt > 0:
            lines.append(f"{col}: {cnt}")

    # Write to file
    out = OUTPUT_REPORTS / "eda_summary.txt"
    with out.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    _log(f"EDA summary written: {out}", "ok")

@_timeit
def basic_visualizations(df: pd.DataFrame, show: bool = True) -> None:
    """Generate and save basic visualizations. Optionally plt.show() them."""
    # Salary distribution histogram
    if "salary" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df["salary"].dropna(), bins=30, kde=True)
        plt.title("Salary Distribution")
        plt.xlabel("Salary")
        plt.tight_layout()
        p = OUTPUT_PLOTS / "salary_distribution.png"
        plt.savefig(p)
        if show:
            plt.show()
        plt.close()
        _log(f"Saved: {p}", "ok")

        # Boxplot
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df["salary"].dropna())
        plt.title("Salary Boxplot")
        plt.tight_layout()
        p = OUTPUT_PLOTS / "salary_boxplot.png"
        plt.savefig(p)
        if show:
            plt.show()
        plt.close()
        _log(f"Saved: {p}", "ok")

    # Salary vs Bonus scatter
    if {"salary", "bonus_percent"}.issubset(df.columns):
        plt.figure(figsize=(7, 5))
        sns.scatterplot(x="bonus_percent", y="salary", data=df, alpha=0.6)
        plt.title("Salary vs Bonus Percent")
        plt.tight_layout()
        p = OUTPUT_PLOTS / "salary_vs_bonus.png"
        plt.savefig(p)
        if show:
            plt.show()
        plt.close()
        _log(f"Saved: {p}", "ok")

    # Gender distribution bar
    if "gender" in df.columns:
        plt.figure(figsize=(6, 4))
        vc = df["gender"].value_counts(dropna=True)
        sns.barplot(x=vc.index, y=vc.values)
        plt.title("Gender Distribution")
        plt.ylabel("Count")
        plt.tight_layout()
        p = OUTPUT_PLOTS / "gender_distribution.png"
        plt.savefig(p)
        if show:
            plt.show()
        plt.close()
        _log(f"Saved: {p}", "ok")

@_timeit
def statistical_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Create a CSV summary for numeric columns (mean, median, std, skew, kurt)."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    rows = []
    for col in numeric_cols:
        s = df[col].dropna()
        if s.empty:
            continue
        rows.append({
            "column": col,
            "mean": s.mean(),
            "median": s.median(),
            "std": s.std(),
            "skew": s.skew(),
            "kurtosis": s.kurt()
        })
    summary_df = pd.DataFrame(rows)
    out = OUTPUT_REPORTS / "statistical_summary.csv"
    summary_df.to_csv(out, index=False)
    _log(f"Statistical summary saved: {out}", "ok")
    return summary_df


@_timeit
def advanced_statistical_analysis(df: pd.DataFrame, show: bool = True) -> None:
    """
    Correlation matrix, ANOVA across departments (salary),
    violin plot per department, and a correlation pair check.
    """
    # Correlation matrix
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        corr = numeric_df.corr()
        _log("Correlation matrix (numeric columns):", "info")
        print(corr.to_string())
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".3f")
        plt.title("Correlation Heatmap (numeric features)")
        plt.tight_layout()
        p = OUTPUT_PLOTS / "correlation_heatmap.png"
        plt.savefig(p)
        if show:
            plt.show()
        plt.close()
        _log(f"Saved: {p}", "ok")

    # Violin plot salary by department
    if {"department", "salary"}.issubset(df.columns):
        plt.figure(figsize=(10, 6))
        sns.violinplot(x="department", y="salary", data=df, inner="quartile", palette="cool")
        plt.title("Salary Distribution by Department (violin)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        p = OUTPUT_PLOTS / "salary_violin_by_department.png"
        plt.savefig(p)
        if show:
            plt.show()
        plt.close()
        _log(f"Saved: {p}", "ok")

        # ANOVA: salary across departments
        groups = [g["salary"].dropna().values for _, g in df.groupby("department") if not g["salary"].dropna().empty]
        if len(groups) > 1:
            f_stat, p_val = stats.f_oneway(*groups)
            _log(f"ANOVA (salary by department): F={f_stat:.4f}, p={p_val:.4f}", "info")
        else:
            _log("ANOVA not performed: not enough groups with data.", "warn")

    # Additional advanced checks: correlation between years_experience and performance_score
    if {"years_experience", "performance_score"}.issubset(df.columns):
        xe = df["years_experience"].dropna()
        yp = df["performance_score"].dropna()
        # align indexes
        common_idx = xe.index.intersection(yp.index)
        if len(common_idx) > 0:
            r, p = stats.pearsonr(xe.loc[common_idx], yp.loc[common_idx])
            _log(f"Pearson r (years_experience vs performance_score): r={r:.4f}, p={p:.4f}", "info")
        else:
            _log("No overlapping data for experience vs performance correlation.", "warn")




# === Utility Decorator & Logger ===
def _timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f"\n⏱️ {func.__name__} completed in {duration:.2f}s\n")
        return result
    return wrapper

def _log(message: str, status="info"):
    tag = {"ok": "✅", "warn": "⚠️", "err": "❌"}.get(status, "ℹ️")
    print(f"{tag} {message}")

# === Output Folder Setup ===
OUTPUT_REPORTS = Path("outputs/reports")
OUTPUT_REPORTS.mkdir(parents=True, exist_ok=True)

# === Hypothesis Testing Function ===
@_timeit
def hypothesis_tests(df: pd.DataFrame) -> None:
    """Perform multiple hypothesis tests and save a textual report."""
    lines = []
    lines.append("🧠 EMPLOYEE HYPOTHESIS TESTING REPORT")
    lines.append("=" * 60)

    # ANOVA Test: Salary difference across departments
    if {"department", "salary"}.issubset(df.columns):
        try:
            anova = stats.f_oneway(
                *[df.loc[df["department"] == d, "salary"].dropna()
                  for d in df["department"].unique()]
            )
            conclusion = "Reject H0 (Significant difference)" if anova.pvalue < 0.05 else "Fail to Reject H0"
            lines.append("\n[ANOVA Test: Salary by Department]")
            lines.append(f"F-statistic = {anova.statistic:.3f}, p-value = {anova.pvalue:.4f}, conclusion = {conclusion}")
        except Exception as e:
            lines.append(f"ANOVA Test Error: {e}")
    else:
        lines.append("ANOVA skipped (missing department or salary column).")

    # T-Test: Salary by Gender
    if {"gender", "salary"}.issubset(df.columns):
        male = df.loc[df["gender"].str.lower() == "male", "salary"].dropna()
        female = df.loc[df["gender"].str.lower() == "female", "salary"].dropna()
        if len(male) > 1 and len(female) > 1:
            t_stat, p_val = stats.ttest_ind(male, female, equal_var=False)
            conclusion = "Reject H0 (Significant difference)" if p_val < 0.05 else "Fail to Reject H0"
            lines.append("\n[T-Test: Salary by Gender]")
            lines.append(f"T-statistic = {t_stat:.3f}, p-value = {p_val:.4f}, conclusion = {conclusion}")
        else:
            lines.append("T-Test skipped (not enough gender samples).")
    else:
        lines.append("T-Test skipped (gender/salary missing).")

    # Chi-Square Test: Department vs Gender
    if {"department", "gender"}.issubset(df.columns):
        contingency = pd.crosstab(df["department"], df["gender"])
        try:
            chi2, p, dof, exp = stats.chi2_contingency(contingency)
            conclusion = "Reject H0 (Relationship exists)" if p < 0.05 else "Fail to Reject H0"
            lines.append("\n[Chi-Square Test: Department vs Gender]")
            lines.append(f"Chi2 = {chi2:.3f}, p-value = {p:.4f}, conclusion = {conclusion}")
        except Exception as e:
            lines.append(f"Chi-Square Test Error: {e}")
    else:
        lines.append("Chi-Square skipped (department/gender missing).")

    # Correlation: Salary vs Bonus
    if {"salary", "bonus"}.issubset(df.columns):
        corr, p_corr = stats.pearsonr(df["salary"], df["bonus"])
        conclusion = "Reject H0 (Significant correlation)" if p_corr < 0.05 else "Fail to Reject H0"
        lines.append("\n[Correlation: Salary vs Bonus]")
        lines.append(f"Pearson r = {corr:.3f}, p-value = {p_corr:.4f}, conclusion = {conclusion}")
    else:
        lines.append("Correlation skipped (salary/bonus missing).")

    # Mann-Whitney U Test (Non-parametric)
    if {"gender", "salary"}.issubset(df.columns):
        male = df.loc[df["gender"].str.lower() == "male", "salary"].dropna()
        female = df.loc[df["gender"].str.lower() == "female", "salary"].dropna()
        if len(male) > 1 and len(female) > 1:
            u_stat, p_u = stats.mannwhitneyu(male, female)
            conclusion = "Reject H0 (Difference detected)" if p_u < 0.05 else "Fail to Reject H0"
            lines.append("\n[Mann-Whitney U Test]")
            lines.append(f"U-statistic = {u_stat:.3f}, p-value = {p_u:.4f}, conclusion = {conclusion}")
        else:
            lines.append("Mann-Whitney U skipped (insufficient samples).")
    else:
        lines.append("Mann-Whitney skipped (gender/salary missing).")

    # === Write to Report File ===
    out = OUTPUT_REPORTS / "hypothesis_testing_report.txt"
    with out.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    _log(f"Hypothesis Testing Report saved at: {out}", "ok")

# Example run:
# df = pd.read_csv("data/cleaned_employee_data.csv")
# hypothesis_tests(df)

# === Utility Decorator & Logger ===
def _timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f"\n⏱️ {func.__name__} completed in {duration:.2f}s\n")
        return result
    return wrapper

def _log(message: str, status="info"):
    tag = {"ok": "✅", "warn": "⚠️", "err": "❌"}.get(status, "ℹ️")
    print(f"{tag} {message}")

# === Output Folder Setup ===
OUTPUT_REPORTS = Path("outputs/reports")
OUTPUT_REPORTS.mkdir(parents=True, exist_ok=True)

# === Hypothesis Testing Function ===
@_timeit
def hypothesis_tests(df: pd.DataFrame) -> None:
    """Perform multiple hypothesis tests and save a textual report."""
    lines = []
    lines.append("🧠 EMPLOYEE HYPOTHESIS TESTING REPORT")
    lines.append("=" * 60)

    # ANOVA Test: Salary difference across departments
    if {"department", "salary"}.issubset(df.columns):
        try:
            anova = stats.f_oneway(
                *[df.loc[df["department"] == d, "salary"].dropna()
                  for d in df["department"].unique()]
            )
            conclusion = "Reject H0 (Significant difference)" if anova.pvalue < 0.05 else "Fail to Reject H0"
            lines.append("\n[ANOVA Test: Salary by Department]")
            lines.append(f"F-statistic = {anova.statistic:.3f}, p-value = {anova.pvalue:.4f}, conclusion = {conclusion}")
        except Exception as e:
            lines.append(f"ANOVA Test Error: {e}")
    else:
        lines.append("ANOVA skipped (missing department or salary column).")

    # T-Test: Salary by Gender
    if {"gender", "salary"}.issubset(df.columns):
        male = df.loc[df["gender"].str.lower() == "male", "salary"].dropna()
        female = df.loc[df["gender"].str.lower() == "female", "salary"].dropna()
        if len(male) > 1 and len(female) > 1:
            t_stat, p_val = stats.ttest_ind(male, female, equal_var=False)
            conclusion = "Reject H0 (Significant difference)" if p_val < 0.05 else "Fail to Reject H0"
            lines.append("\n[T-Test: Salary by Gender]")
            lines.append(f"T-statistic = {t_stat:.3f}, p-value = {p_val:.4f}, conclusion = {conclusion}")
        else:
            lines.append("T-Test skipped (not enough gender samples).")
    else:
        lines.append("T-Test skipped (gender/salary missing).")

    # Chi-Square Test: Department vs Gender
    if {"department", "gender"}.issubset(df.columns):
        contingency = pd.crosstab(df["department"], df["gender"])
        try:
            chi2, p, dof, exp = stats.chi2_contingency(contingency)
            conclusion = "Reject H0 (Relationship exists)" if p < 0.05 else "Fail to Reject H0"
            lines.append("\n[Chi-Square Test: Department vs Gender]")
            lines.append(f"Chi2 = {chi2:.3f}, p-value = {p:.4f}, conclusion = {conclusion}")
        except Exception as e:
            lines.append(f"Chi-Square Test Error: {e}")
    else:
        lines.append("Chi-Square skipped (department/gender missing).")

    # Correlation: Salary vs Bonus
    if {"salary", "bonus"}.issubset(df.columns):
        corr, p_corr = stats.pearsonr(df["salary"], df["bonus"])
        conclusion = "Reject H0 (Significant correlation)" if p_corr < 0.05 else "Fail to Reject H0"
        lines.append("\n[Correlation: Salary vs Bonus]")
        lines.append(f"Pearson r = {corr:.3f}, p-value = {p_corr:.4f}, conclusion = {conclusion}")
    else:
        lines.append("Correlation skipped (salary/bonus missing).")

    # Mann-Whitney U Test (Non-parametric)
    if {"gender", "salary"}.issubset(df.columns):
        male = df.loc[df["gender"].str.lower() == "male", "salary"].dropna()
        female = df.loc[df["gender"].str.lower() == "female", "salary"].dropna()
        if len(male) > 1 and len(female) > 1:
            u_stat, p_u = stats.mannwhitneyu(male, female)
            conclusion = "Reject H0 (Difference detected)" if p_u < 0.05 else "Fail to Reject H0"
            lines.append("\n[Mann-Whitney U Test]")
            lines.append(f"U-statistic = {u_stat:.3f}, p-value = {p_u:.4f}, conclusion = {conclusion}")
        else:
            lines.append("Mann-Whitney U skipped (insufficient samples).")
    else:
        lines.append("Mann-Whitney skipped (gender/salary missing).")

    # === Write to Report File ===
    out = OUTPUT_REPORTS / "hypothesis_testing_report.txt"
    with out.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    _log(f"Hypothesis Testing Report saved at: {out}", "ok")

# Example run:
# df = pd.read_csv("data/cleaned_employee_data.csv")
# hypothesis_tests(df)





def main(show_plots: bool = True):
    total_start = time.perf_counter()
    _log("Employee Data Analysis pipeline starting...", "info")

    # Load
    df = load_data(DATA_PATH)

    # Clean a few expected columns: ensure lower-case gender/department
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    if "department" in df.columns:
        df["department"] = df["department"].astype(str).str.strip()

    exploratory_data_analysis(df)
    basic_visualizations(df, show=show_plots)
    statistical_summary(df)
    advanced_statistical_analysis(df, show=show_plots)
    hypothesis_tests(df)

    total_end = time.perf_counter()
    _log(f"Pipeline completed in {total_end - total_start:.2f} seconds", "ok")


if __name__ == "__main__":
    # show_plots=True will both save and display each plot (good for PyCharm)
    main(show_plots=True)
