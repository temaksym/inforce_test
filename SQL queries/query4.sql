-- 4. Query 4: Find the user(s) with the most common email domain.

SELECT *
FROM users
WHERE domain = (
    SELECT domain
    FROM users
    GROUP BY domain
    ORDER BY COUNT(domain) DESC
    LIMIT 1
);