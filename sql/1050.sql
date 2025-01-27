SELECT
    actor_id,
    director_id
FROM
    ActorDirector AD
GROUP BY
    AD.actor_id, AD.director_id
HAVING
    Count(AD.actor_id) >= 3 AND Count(AD.director_id) >= 3;