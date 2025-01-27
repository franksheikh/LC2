/*
	group by -> all unique users
	count user_id for each user_id
	
	group by will take all the user ids, so no need for distinct, and then count will return the count of all follower_ids for each user
*/

SELECT
    user_id,
    COUNT(follower_id) as followers_count
FROM
    Followers
GROUP BY
    user_id
ORDER BY
    user_id ASC;

/*
INPUT
| user_id | follower_id |
| ------- | ----------- |
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |

OUTPUT
| user_id | followers_count |
| ------- | --------------- |
| 0       | 1               |
| 1       | 1               |
| 2       | 2               |
*/