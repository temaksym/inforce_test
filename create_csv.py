import pandas as pd
import random
from faker import Faker

fake = Faker()

data = {
    'user_id': [i for i in range(1, 1501)],
    'name': [fake.name() for _ in range(1500)],
    'email': [fake.email() for _ in range(1500)],
    'signup_date': [fake.date_this_decade() for _ in range(1500)]
}

df = pd.DataFrame(data)
df.to_csv('users.csv', index=False)