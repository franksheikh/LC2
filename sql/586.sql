/*
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
 

Write a solution to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The result format is in the following example.

 

Example 1:

Input: 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
Output: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
Explanation: 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.
*/



-- v2
-- FOR A TIE
SELECT
    O.customer_number
FROM
    Orders O
GROUP BY
    O.customer_number
HAVING
	-- find customers whose total count of orders matches the highest count of orders
	-- could be 1 or more
    Count(*) = (
		-- find the highest count of orders from all users
        SELECT MAX(max_count) as max_count
        FROM
			-- find the total counts of orders for each user
            (SELECT 
                COUNT(*) AS max_counts_by_user
            FROM
                Orders
            GROUP BY 
                customer_number
            ) AS subquery
    )
ORDER BY
    O.customer_number DESC;


-- v1
SELECT 
    O.customer_number
FROM
    Orders O
GROUP BY
    O.customer_number
ORDER BY
    COUNT(O.order_number) DESC
LIMIT
    1;
    
