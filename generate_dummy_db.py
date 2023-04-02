import sqlite3
import random
import string
import faker
from datetime import datetime, timedelta

fake = faker.Faker()
# Connect to database and create tables
conn = sqlite3.connect('bike_store.db')
c = conn.cursor()

# Create customers table
c.execute('''CREATE TABLE customers
             (id INTEGER PRIMARY KEY, customer_id INTEGER, name TEXT, email TEXT, phone TEXT)''')

# Create sales table
c.execute('''CREATE TABLE sales
             (id INTEGER PRIMARY KEY, customer_id INTEGER, bike TEXT, sale_date DATE, price INTEGER)''')

# Create sales person table
c.execute('''CREATE TABLE sales_person
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)''')

# Generate and insert dummy customer data
for i in range(100):
    # Generate random real names using Faker
    first_name = fake.first_name()
    customer_id = random.randint(1, 100)
    name = f'{first_name} {fake.last_name()}'
    email = f'{first_name.lower()}@example.com'
    phone = f'+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}'
    c.execute(f"INSERT INTO customers VALUES ({i+1}, {customer_id}, '{name}', '{email}', '{phone}')")
    
    bike = random.choice(['Road Bike', 'Mountain Bike', 'Hybrid Bike', 'Electric Bike'])
    sale_date = datetime.now() - timedelta(days=random.randint(1, 365))
    price = random.randint(100, 5000)
    c.execute(f"INSERT INTO sales VALUES ({i+1}, {customer_id}, '{bike}', '{sale_date.date()}', {price})")

# Commit changes and close connection
conn.commit()
conn.close()
