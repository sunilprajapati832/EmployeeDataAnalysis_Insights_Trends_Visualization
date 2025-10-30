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
A complete end-to-end Employee Data Analytics & Insights Visualization Project built in Python, designed to demonstrate real-world data cleaning, EDA, statistical hypothesis testing, analysis and visualization skills. It provides insightful business trends, statistical reports, and data-driven recommendations for HR and management teams.
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
1. **Data Loading & Cleaning** – Combined multiple CSV sources and handled missing values.  
2. **Exploratory Data Analysis (EDA)** – Statistical summary, type detection, and structure insights.  
3. **Hypothesis Testing** – Validated assumptions using multiple statistical tests (ANOVA, T-Test, Chi-Square, Mann-Whitney U, Correlation).  
4. **Visualization & Reporting** – Saved professional plots and generated summary tables for insights.  

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

## Team & Department Analysis

| Metric | Insight |
|:--|:--|
| **Total Teams** | 6 |
| **Departments** | Finance, Engineering, Sales, Marketing, Operations, HR |

### Average Salary by Department
| Department | Avg Salary |
|:--|--:|
| HR | ₹ 89 784 |
| Sales | ₹ 88 750 |
| Operations | ₹ 88 698 |
| Engineering | ₹ 87 941 |
| Finance | ₹ 87 533 |
| Marketing | ₹ 87 462 |

### Gender Distribution by Department (Sample)
| Department | Female | Male | Other |
|:--|--:|--:|--:|
| Engineering | 222 | 200 | 224 |
| Finance | 230 | 240 | 275 |
| HR | 250 | 250 | 192 |
| Marketing | 230 | 188 | 210 |
| Operations | 242 | 232 | 210 |
| Sales | 208 | 199 | 198 |

## Hypothesis Testing Report

| Test | Statistic | P-Value | Result | Insight |
|:--|--:|--:|:--|:--|
| **ANOVA (Salary vs Department)** | F = 0.455 | 0.8102 | ❌ Not Significant | No salary difference across departments |
| **T-Test (Salary by Gender)** | t = −0.385 | 0.7004 | ❌ Not Significant | Gender has no impact on salary |
| **Chi-Square (Dept vs Gender)** | χ² = 20.201 | 0.0274 | ✅ Significant | Department & gender are related |
| **Correlation (Salary vs Bonus)** | r = 0.001 | 0.9430 | ❌ Not Significant | No linear relationship |
| **Mann-Whitney U (Non-parametric)** | U = 896 162 | 0.6783 | ❌ Not Significant | No rank-based difference detected |

## Statistical Summary (Distribution Insights)

| Column | Mean | Median | Std | Skew | Kurtosis |
|:--|--:|--:|--:|--:|--:|
| age | 40.81 | 41.00 | 11.08 | −0.05 | −1.23 |
| salary | 88 360.85 | 87 713.00 | 34 462.23 | 0.06 | −1.19 |
| bonus_percent | 12.48 | 12.51 | 4.32 | −0.01 | −1.20 |
| performance_score | 79.93 | 80.00 | 11.81 | 0.02 | −1.20 |

*All key metrics show near-normal distribution with mild negative kurtosis (light tails).*

## Key Insights

- **Salary equality** observed across genders and departments.  
- **No strong correlation** between salary and bonus percentage.  
- **Department–gender relationship exists**, suggesting departmental gender skew.  
- Data distribution shows balanced spread but incomplete job level & experience data.  
- Clean, modular codebase ready for **further ML or dashboard integration**.   

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


























