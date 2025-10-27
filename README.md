Tree/f D:.
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
│   │       summary_insights.py
│   │       
│   ├───etl
│   │   │   clean_data.py
│   │   │   to_sql.py
│   │   │   
│   │   └───data
│   │       └───processed
│   └───viz
│           charts.py
│           
└───visualizations
