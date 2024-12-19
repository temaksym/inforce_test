import psycopg2


# Connecting to DB
db_config = {
    'dbname': 'users_inforce',
    'user': 'postgres',
    'password': '2504',
    'host': 'localhost',
    'port': '5432'
}
conn = psycopg2.connect(**db_config)
curr = conn.cursor()

# Creating the table
create_table_query = """
    CREATE TABLE IF NOT EXISTS inforce.users (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE NOT NULL,
        signup_date DATE,
        domain VARCHAR(100)
    );
"""
curr.execute(create_table_query)
conn.commit()

# Check if the table was created
tables_query = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'inforce'
"""
curr.execute(tables_query)


tables = curr.fetchall()
for table in tables:
    print(table[0])

curr.close()