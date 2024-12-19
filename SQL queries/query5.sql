-- 5. Query 5: Delete records where the email domain is not from a specific list
-- (e.g., keep only emails from `gmail.com`, `yahoo.com`, and `example.com`)

DELETE FROM users
WHERE domain NOT IN ('gmail.com', 'yahoo.com', 'example.com');