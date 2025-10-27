SELECT gender, COUNT(*) as total
FROM employees
GROUP BY gender;