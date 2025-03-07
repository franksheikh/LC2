-- IF statement
-- IF (<logic>, true value, false value) AS <variable name>

-- ORDER BY <property> ASC/DESC;
SELECT 
    employee_id, 
    IF (employee_id % 2 != 0 AND name NOT LIKE "M%", salary, 0) AS bonus
FROM Employees
ORDER BY employee_ID ASC;