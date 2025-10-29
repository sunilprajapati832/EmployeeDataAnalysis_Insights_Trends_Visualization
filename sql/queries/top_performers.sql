SELECT employee_id, first_name, department, performance_score, salary
FROM employees
WHERE performance_score IS NOT NULL
ORDER BY performance_score DESC, salary DESC
LIMIT 10;
