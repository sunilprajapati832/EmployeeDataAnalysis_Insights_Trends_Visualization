SELECT department, ROUND(AVG(salary),2) as avg_salary, COUNT(*) as headcount
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;