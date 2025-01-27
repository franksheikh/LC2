-- v2
SELECT
    U.name,
    IFNULL(SUM(distance),0) AS travelled_distance 
FROM
    Users U
LEFT JOIN
    Rides R
ON
    U.id = R.user_id
GROUP BY
    U.id
ORDER BY
    travelled_distance DESC, U.name ASC
	
-- v1
SELECT
    U.name,
    IFNULL(SUM(distance),0) AS travelled_distance 
FROM
    Rides R
RIGHT JOIN
    Users U
ON
    R.user_id = U.id
GROUP BY
    R.user_id
ORDER BY
    travelled_distance DESC, U.name ASC