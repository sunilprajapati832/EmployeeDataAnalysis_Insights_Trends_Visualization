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

### Python Scripts Included 
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

### Key Analytical Techniques
* SQL Queries: Department-wise salary insights, ranking salaries, filtering by performance
* Python EDA: Histograms, boxplots, scatterplots, treemaps, heatmaps
* Statistical Testing: ANOVA, T-tests, Chi-square, Mann-Whitney U Test, Correlation analysis

### Sample Visualizations
* Salary distribution by department
* Bonus % vs Performance Score
* Gender distribution across teams
* Treemaps of salary and employee count
* Correlation heatmaps

# Employee Data Analysis (Insights, Trends & Visualizations) 
Unified Employee Data Analysis — cleaned datasets, SQL integration, EDA, visualizations and insights.

## Project folder tree (Tree/f) 
D:.
├───.idea
│   └───inspectionProfiles
├───assets
├───data
│   ├───processed
│   └───raw
├───notebooks
├───outputs
│   ├───plots
│   └───reports
├───reports
├───scripts
├───sql
│   └───queries
├───src
│   ├───analysis
│   ├───etl
│   │   └───data
│   │       └───processed
│   ├───outputs
│   │   ├───plots
│   │   └───reports
│   └───viz
└───visualizations
    └───outputs
        ├───plots
        └───reports
(venv) PS D:\EmployeeDataAnalysis_Insights_Trends_Visualization> tree /f
Folder PATH listing for volume New Volume
Volume serial number is CEB3-FEDD
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








