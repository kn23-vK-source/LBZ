#za2
import psycopg2
from faker import Faker
import random

DB_NAME = "Io"
DB_USER = "Triton"
DB_PASS = "satellite"
DB_HOST = "172.18.0.2"
DB_PORT = "5432"

conn = None
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except:
    print("Database not connected successfully")


cur = conn.cursor()

cur.execute("""
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    account_number VARCHAR(50) NOT NULL
);
""")

cur.execute("""
CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    material_name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);
""")

cur.execute("""
CREATE TABLE deliveries (
    delivery_id SERIAL PRIMARY KEY,
    delivery_date DATE NOT NULL,
    supplier_id INT NOT NULL,
    material_id INT NOT NULL,
    delivery_days INT CHECK (delivery_days BETWEEN 1 AND 7),
    quantity INT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id),
    FOREIGN KEY (material_id) REFERENCES materials (material_id)
);
""")

fake = Faker('uk_UA')

materials_data = [
    ("Деревина", random.uniform(10.00, 50.00)),
    ("Лак", random.uniform(5.00, 20.00)),
    ("Сталеві деталі", random.uniform(20.00, 100.00))
]

for material in materials_data:
    cur.execute("INSERT INTO materials (material_name, price) VALUES (%s, %s)", material)

suppliers_data = [
    (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999))),
    (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999))),
    (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999))),
    (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999)))
]

for supplier in suppliers_data:
    cur.execute("INSERT INTO suppliers (company_name, contact_person, phone, account_number) VALUES (%s, %s, %s, %s)", supplier)

deliveries_data = []
for _ in range(22):
    supplier_id = random.randint(1, 4)
    material_id = random.randint(1, 3)
    delivery_date = fake.date_between(start_date='-1y', end_date='today')
    delivery_days = random.randint(1, 7)
    quantity = random.randint(1, 100)
    deliveries_data.append((delivery_date, supplier_id, material_id, delivery_days, quantity))

for delivery in deliveries_data:
    cur.execute("INSERT INTO deliveries (delivery_date, supplier_id, material_id, delivery_days, quantity) VALUES (%s, %s, %s, %s, %s)", delivery)

conn.commit()

cur.close()
conn.close()

print("\n=OK=")
