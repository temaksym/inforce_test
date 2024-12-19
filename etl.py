import pandas as pd
import re
from sqlalchemy import create_engine


FILE_NAME = 'users.csv'

DB_CONFIG = {
    'dbname': 'users_inforce',
    'user': 'postgres',
    'password': '********',
    'host': 'localhost',
    'port': '5432'
}



def load(df):

    engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")
    with engine.connect() as connection:
        df.to_sql('users', con=connection, if_exists='replace', index=False)


def extract(FILE_NAME):
    
    try:
        df = pd.read_csv(FILE_NAME)

        # Convert signup_date to standard format
        df['signup_date'] = pd.to_datetime(df['signup_date']).dt.strftime('%Y-%m-%d')

        # Filtering emails with invalid addresses
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        df = df[df['email'].apply(lambda x: re.match(email_pattern, x) is not None)]

        # Adding 'domain' column
        df['domain'] = df['email'].apply(lambda x: x.split('@')[1])
    
    except Exception as e:
        print(f"Extraction failed.\n{str(e)}")
        return
    
    try:
        load(df)
    except Exception as e:
        print(f"Loading failed.\n{str(e)}")


try:
    extract(FILE_NAME)
except:
    print("ETL process failed.")