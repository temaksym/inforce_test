-- 1. Query 1: Retrieve the count of users who signed up on each day.

SELECT signup_date, count(user_id) as count
FROM users
GROUP BY signup_date
ORDER BY signup_date;