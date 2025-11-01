# Employee Data Analysis (Insights, Trends & Visualizations)

Welcome to my flagship data analysis project — a comprehensive exploration of employee data using Python, SQL and statistical techniques. This repository consolidates five smaller projects I created during my early learning journey into one unified, insightful case study.

## Project Purpose
The goal of this project is to merge multiple employee-related datasets and analytical approaches into a single, high-quality repository that showcases:
* SQL query integration
* Python-based data cleaning and visualization
* Statistical hypothesis testing
* Business insights across departments, gender, salary and performance
This project reflects my belief in quality over quantity and serves as a milestone in my data analytics journey.

## Data used from Merged Repositories

### Origin: Merged Repositories
This project combines the following five repositories:

| **S.No..** | **Project Name**                    | **Description**                                                                                   |
|------------| ----------------------------------- | ------------------------------------------------------------------------------------------------- |
|1.          | `Employee Data Insights Project 1`  | Used employees.csv with multiple Python scripts for EDA, hypothesis testing and visualization     |
|2.          | `Data Visualization Employee Analysis`  | Used employees_cleaned_data.csv with SQL queries and matplotlib/seaborn visualizations        |
|3.          | `Sales Data Insights Project 1`     | Blank project created to learn GitHub repository setup                                            |
|4.          | `Employee Data Analysis 2`          | Used employees_project_cleaned.csv with main.py                                                   |
|5.          | `Employee Data Analysis 3`          | Same as Project`Employee Data Analysis 2` — same dataset and script                               |

### Datasets Used

| **EmployeeDataInsightsProject1**    |**DataVisualizationEmployeeAnalysis**| **EmployeeDataAnalysis2**     |
|-------------------------------------| ----------------------------------- | ----------------------------- |
|employees.csv <br> (raw data used for hypothesis testing and EDA)  | employees_project_cleaned.csv <br> (used for SQL queries and visualizations) | employees_project_cleaned.csv <br> (used in Projects 2 & 3 for performance and salary analysis) |

### Python Scripts Used 
From various projects, the following scripts are integrated and modularized:
| **EmployeeDataInsightsProject1**    |**DataVisualizationEmployeeAnalysis**| **EmployeeDataAnalysis2**|
|-------------------------------------| ----------------------------------- | ------------------------ |
|DataVisualization.py                 | mysql_upload1.py                    | main.py                  |
|EmployeeDataAnalysis1.py             | mysql_upload.py                     |                          |
|DataVisualizationFinal.py            | script.py                           |                          |
|ExploratoryDataAnalysis2.py          |                                     |                          |
|DataAnalysisHypothesisTesting.py     |                                     |                          |
|ProgrammingApproachesInDataAnalysis.py|                                    |                          |
|exploratoryDataAnalysisEDA.py        |                                     |                          |
|StatisticalAnalysis.py               |                                     |                          |

### Key Analytical Techniques Used
* SQL Queries: Department-wise salary insights, ranking salaries, filtering by performance
* Python EDA: Histograms, boxplots, scatterplots, treemaps, heatmaps
* Statistical Testing: ANOVA, T-tests, Chi-square, Mann-Whitney U Test, Correlation analysis
* Sample Visualizations: Salary distribution by department, Bonus % vs Performance Score, Gender distribution across teams, Treemaps of salary and employee count, Correlation heatmaps
---

# Employee Data Analysis (Insights, Trends & Visualizations) 
Unified Employee Data Analysis — This project focuses on **analyzing and uncovering insights from a synthetic employee dataset** containing demographics, compensation and performance metrics.
A complete end-to-end Employee Data Analytics & Insights Visualization Project built in Python, designed to demonstrate real-world data cleaning, EDA, statistical hypothesis testing, analysis and visualization skills. 
It provides insightful business trends, statistical reports, and data-driven recommendations for HR and management teams. <br>
**Domain** — **Human Resource / Workforce Analytics**

📁 **Core Python File:** `basic_visualizations.py`  
📂 **Outputs:** `/outputs/plots/` (All plots auto-saved & displayed live in PyCharm) <br>
🧰 **Tools & Technologies:** (Language) Python 3.11+ , (Libraries) pandas, numpy, scipy, matplotlib, tabulate ,  (Environment) PyCharm IDE , (Visualization) Matplotlib plots (saved + live) 


| **UpdatedDataset**   |**New Python Scripts**| **Plots(Graphs)**                  |**Database**         | **SQL_Files**       | **Reports**             |
|--------------------- | -------------------- | -----------------------------------|---------------------|---------------------|-------------------------|
|employees_unified.csv |basic_visualizations.py|avg_salary_by_department.png       |employee_data.db     |create_schema.sql    |eda_summary.txt          |
|                      |basic_visualizations_1.py |correlation_heatmap.png         |                     |avg_salary_by_dept.sql|hypothesis_testing_report.txt|
|                      |basic_visualizations_2.py|distribution_comparison.png      |                     |gender_distribution.sql|statistical_summary.csv  |
|                      |  run_sql_queries.py  |gender_distribution.png             |                     |   top_performers.sql| team_analysis_report.txt|
|                      |   summary_insights.py|gender_distribution_by_department.png|                    |                     | insights_summary.md     |
|                      |   clean_data.py      |pairplot_relationships.png          |                     |                     |                         |  
|                      |data_cleaning_methods_demo.py |salary_boxplot.png          |                     |                     |                         |
|                      |  to_sql.py           |salary_distribution.png             |                     |                     |                         |
|                      |   main.py            |salary_violin_by_department.png     |                     |                     |                         |
|                      |  test.py             |salary_violin_department.png        |                     |                     |                         |
|                      |  charts.py           |salary_vs_bonus.png                 |                     |                     |                         |
|                      |                      |salary_vs_performance.png           |                     |                     |                         |
|                      |                      |team_avg_salary_by_department.png   |                     |                     |                         |
|                      |                      |team_gender_distribution_by_department.png|               |                     |                         |
|                      |                      |anova_salary_by_department.png      |                     |                     |                         |
|                      |                      |chi_square_department_gender.png    |                     |                     |                         |
|                      |                      |correlation_salary_bonus.png        |                     |                     |                         |
|                      |                      |mannwhitney_salary_by_gender.png    |                     |                     |                         |
|                      |                      |ttest_salary_by_gender.png          |                     |                     |                         |
|                      |                      |team_gender_distribution_by_department.png|               |                     |                         |

## Project Workflow
1. **Data Loading & Cleaning** – Load and preprocess unified HR data.  
2. **Exploratory Data Analysis (EDA)** – Statistical summary, type detection, and structure insights.
3. **Basic Visualizations** – salary, gender, and department trends
4. **Visualization & Reporting** – Saved professional plots and generated summary tables for insights.
5. **Statistical Analysis** – mean, std, skewness, kurtosis, etc.
6. **Advanced Analysis** – ANOVA, correlation matrix, violin plots
7. **Hypothesis Testing** – Validated assumptions using multiple statistical tests (T-Test, Chi-Square, Mann-Whitney U).  
8. **Team-level Insights** – salary averages and gender distribution
9. **Automated report saving** – in /outputs/reports and /outputs/plots

## Exploratory Data Analysis (EDA) Summary

| Metric | Details |
|:--|:--|
| **Total Rows** | 4000 |
| **Total Columns** | 11 |
| **Numeric Columns** | ['age', 'job_level', 'years_experience', 'salary', 'bonus_percent', 'performance_score'] |
| **Categorical Columns** | ['employee_id', 'first_name', 'gender', 'department', 'source_file'] |

### Numeric Summaries
| Column | Mean | Median | Std | Min | Max | Count |
|:--|--:|--:|--:|--:|--:|--:|
| age | 40.81 | 41.00 | 11.08 | 22.00 | 59.00 | 3999 |
| salary | 88 360.85 | 87 713.00 | 34 462.23 | 30 138.00 | 149 863.00 | 4000 |
| bonus_percent | 12.48 | 12.51 | 4.32 | 5.00 | 19.99 | 4000 |
| performance_score | 79.93 | 80.00 | 11.81 | 60.00 | 100.00 | 4000 |

### Categorical Insights
| Column | Top 3 Values |
|:--|:--|
| gender | female (1382), other (1309), male (1309) |
| department | Finance (745), HR (692), Operations (684) |
| source_file | employees_cleaned_data.csv (2000), employees_project_cleaned.csv (1999), employees.csv (1) |

### Missing Values
| Column | Missing Count |
|:--|--:|
| first_name | 3999 |
| age | 1 |
| job_level | 4000 |
| years_experience | 4000 |

## Visualization (Basic & Reporting)

<table><tr><td><img src="outputs/plots/avg_salary_by_department.png"></td> <td><img src="outputs/plots/salary_distribution.png"></td></tr></table>
<table><tr><td><img src="outputs/plots/gender_distribution_by_department.png"></td> <td><img src="outputs/plots/gender_distribution.png"></td></tr></table>
<table><tr><td><img src="outputs/plots/correlation_heatmap.png"></td> <td><img src="outputs/plots/pairplot_relationships.png"></td></tr></table>
<table><tr><td><img src="outputs/plots/salary_boxplot.png"></td> <td><img src="outputs/plots/distribution_comparison.png"></td></tr></table>
<table><tr><td><img src="outputs/plots/salary_violin_by_department.png"></td> <td><img src="outputs/plots/salary_violin_department.png"></td></tr></table>
<table><tr><td><img src="outputs/plots/salary_vs_bonus.png"></td> <td><img src="outputs/plots/salary_vs_performance.png"></td></tr></table>
<table><tr><td><img src="outputs/plots/team_avg_salary_by_department.png"></td> <td><img src="outputs/plots/team_gender_distribution_by_department.png"></td></tr></table>

## Statistical Summary (Distribution Insights)

| Column | Mean | Median | Std | Skew | Kurtosis |
|:--|--:|--:|--:|--:|--:|
| age | 40.81 | 41.00 | 11.08 | −0.05 | −1.23 |
| salary | 88 360.85 | 87 713.00 | 34 462.23 | 0.06 | −1.19 |
| bonus_percent | 12.48 | 12.51 | 4.32 | −0.01 | −1.20 |
| performance_score | 79.93 | 80.00 | 11.81 | 0.02 | −1.20 |

*All key metrics show near-normal distribution with mild negative kurtosis (light tails).*

## Advanced Analysis 

<table><tr><td><img src="src/outputs/plots/anova_salary_by_department.png"></td> <td><img src="src/outputs/plots/correlation_salary_bonus.png"></td></tr></table>
<table><tr><td><img src="src/outputs/plots/chi_square_department_gender.png"></td> <td><img src="src/outputs/plots/mannwhitney_salary_by_gender.png"></td></tr></table>
<table><tr><td><img src="src/outputs/plots/ttest_salary_by_gender.png"></td> <td><img src=""></td></tr></table>

## Hypothesis Testing Report

| Test | Statistic | P-Value | Result | Insight |
|:--|--:|--:|:--|:--|
| **ANOVA (Salary vs Department)** | F = 0.455 | 0.8102 | ❌ Not Significant | No salary difference across departments |
| **T-Test (Salary by Gender)** | t = −0.385 | 0.7004 | ❌ Not Significant | Gender has no impact on salary |
| **Chi-Square (Dept vs Gender)** | χ² = 20.201 | 0.0274 | ✅ Significant | Department & gender are related |
| **Correlation (Salary vs Bonus)** | r = 0.001 | 0.9430 | ❌ Not Significant | No linear relationship |
| **Mann-Whitney U (Non-parametric)** | U = 896 162 | 0.6783 | ❌ Not Significant | No rank-based difference detected |

## Team-level Insights

| Metric | Insight |
|:--|:--|
| **Total Teams** | 6 |
| **Departments** | Finance, Engineering, Sales, Marketing, Operations, HR |

| Average Salary by Department  | Gender Distribution by Department (Sample) |
|-------------------------------|--------------------------------------------|
| <table> <tr><th>Department</th><th>Avg Salary</th></tr><tr><td>HR</td><td>₹ 89 784</td></tr><tr><td>Sales</td><td>₹ 88 750</td></tr><tr><td>Operations</td><td>₹ 88 698</td></tr><tr><td>Engineering</td><td>₹ 87 941</td></tr><tr><td>Finance</td><td>₹ 87 533</td></tr><tr><td>Marketing</td><td>₹ 87 462</td></tr> </table> | <table> <tr><th>Department</th><th>Male</th><th>Female</th><th>Other</th></tr><tr><td>Engineering</td><td>222</td><td>200</td><td>224</td></tr><tr><td>Finance</td><td>230</td><td>240</td><td>275</td></tr><tr><td>HR</td><td>250</td><td>250</td><td>192</td></tr><tr><td>Marketing</td><td>230</td><td>188</td><td>210</td></tr><tr><td>Operations</td><td>242</td><td>232</td><td>210</td></tr><tr><td>Sales</td><td>208</td><td>199</td><td>198</td></tr> </table> |

## Key Insights

- **Salary equality** observed across genders and departments.  
- **No strong correlation** between salary and bonus percentage.  
- **Department–gender relationship exists**, suggesting departmental gender skew.  
- Data distribution shows balanced spread but incomplete job level & experience data.  
- Clean, modular codebase ready for **further ML or dashboard integration**.

## Business Insights & Recommendations
1. **Gender–Department Diversity**
* Significant relation (p=0.0274) → gender distribution varies by department.
* Action: Focus hiring diversity efforts in Engineering & Operations to achieve balance.

2. **Salary Equity Across Organization**
* No significant differences between departments or genders.
* Action: Maintain this fair pay structure as a strong employer-branding message.

3. **Bonus Structure**
* Salary and bonus have no correlation (r≈0).
* Action: Evaluate if the bonus system is effectively driving performance or needs restructuring.

4. **Departmental Averages**

| Department | Avg. Salary (₹) | Key Insight|
|:--|--:|--:|
| HR	| 89,784  | Highest average salary, likely senior positions |
| Sales | 88,750  | Incentive-driven compensation |
| Engineering / Operations	 | ~88,000 | Core technical stability|
| Finance / Marketing | ~87,000 | May require motivation or rewards review |

6. **Workforce Profile**
* Mid-aged (avg 41 years), high-performing (avg 80/100).
* Action: Introduce mentorship and leadership training to retain experience and motivate youth hires.

7. **Data Quality Gaps**
* Missing job_level, years_experience, first_name.
* Action: Enforce data validation and completeness checks in HR systems for accurate analytics.

## Project folder tree (Tree/f) 
D:.
│   .gitignore
│   LICENSE
│   main.py
│   README.md
│   requirements.txt
│   test.py
│   
├───.idea
│   │   .gitignore
│   │   EmployeeDataAnalysis_Insights_Trends_Visualization.iml
│   │   misc.xml
│   │   modules.xml
│   │   vcs.xml
│   │   workspace.xml
│   │   
│   └───inspectionProfiles
│           profiles_settings.xml
│           Project_Default.xml
│           
├───assets
├───data
│   │   employee_data.db
│   │   
│   ├───processed
│   │       employees_unified.csv
│   │       
│   └───raw
│           employees.csv
│           employees_cleaned_data.csv
│           employees_project_cleaned.csv
│           
├───notebooks
│       01_data_cleaning.ipynb
│       02_sql_analysis.ipynb
│       03_visualizations.ipynb
│       
├───outputs
│   ├───plots
│   │       avg_salary_by_department.png
│   │       correlation_heatmap.png
│   │       distribution_comparison.png
│   │       gender_distribution.png
│   │       gender_distribution_by_department.png
│   │       pairplot_relationships.png
│   │       salary_boxplot.png
│   │       salary_distribution.png
│   │       salary_violin_by_department.png
│   │       salary_violin_department.png
│   │       salary_vs_bonus.png
│   │       salary_vs_performance.png
│   │       team_avg_salary_by_department.png
│   │       team_gender_distribution_by_department.png
│   │       
│   └───reports
│           eda_summary.txt
│           hypothesis_testing_report.txt
│           statistical_summary.csv
│           team_analysis_report.txt
│           
├───reports
│       insights_summary.md
│       
├───scripts
├───sql
│   │   create_schema.sql
│   │   
│   └───queries
│           avg_salary_by_dept.sql
│           gender_distribution.sql
│           top_performers.sql
│           
├───src
│   ├───analysis
│   │       run_sql_queries.py
│   │       summary_insights.py
│   │       
│   ├───etl
│   │   │   clean_data.py
│   │   │   data_cleaning_methods_demo.py
│   │   │   to_sql.py
│   │   │   
│   │   └───data
│   │       └───processed
│   ├───outputs
│   │   ├───plots
│   │   │       anova_salary_by_department.png
│   │   │       chi_square_department_gender.png
│   │   │       correlation_salary_bonus.png
│   │   │       mannwhitney_salary_by_gender.png
│   │   │       ttest_salary_by_gender.png
│   │   │       
│   │   └───reports
│   │           hypothesis_testing_report.txt
│   │           
│   └───viz
│           charts.py
│           
└───visualizations
    │   basic_visualizations.py
    │   basic_visualizations_1.py
    │   basic_visualizations_2.py
    │   
    └───outputs
        ├───plots
        │       avg_salary_by_department.png
        │       correlation_heatmap.png
        │       gender_distribution.png
        │       gender_distribution_by_department.png
        │       salary_boxplot.png
        │       salary_distribution.png
        │       salary_violin_by_department.png
        │       salary_vs_bonus.png
        │       
        └───reports
                eda_summary.txt
                hypothesis_testing.txt
                hypothesis_testing_report.txt
                statistical_summary.csv
                team_analysis.csv

## PythonFile(basic_visualization.py) for Execution this Project
### See other files(.sqlfiles, reports etc.) also in folders
```
python
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
```


## How to Run the Project
* Clone the repository: git clone https://github.com/sunilprajapati832/EmployeeDataAnalysis_Insights_Trends_Visualization.git
* Install dependencies: pip install -r requirements.txt
* Run notebooks or scripts from the /notebooks or /scripts folder.

## About Me
I'm Sunil Prajapati — a data analyst, machine learning enthusiast and educational content creator. This project reflects my growth from beginner to practitioner and my passion for turning data into insights.
If you found this project interesting, let’s connect!  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20Me-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/sunil-prajapati832)

---
🛠 Built by: Sunil Prajapati |  Github + Data + Python + PyCharm + Canva 
---


















































