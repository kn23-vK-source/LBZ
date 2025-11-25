#zav3
import psycopg2

def sql_table(cur, sql_str):
    cur.execute(sql_str)

    max_size_rows = []
    column_names = [desc[0] for desc in cur.description]

    for name in column_names:
        max_size_rows.append(len(name)+2)

    rows = cur.fetchall()

    for data in rows:
        for i in range(len(data)):
            max_size_rows[i] = max(max_size_rows[i], len(str(data[i]))+2)

    for i in range(sum(max_size_rows)+len(column_names)):
        print("=", end="")
    print("")

    print(end="|")
    for i in range(len(column_names)):
        print(column_names[i].center(max_size_rows[i]), end="|")
    print("")

    for data in rows:
        print(end="|")
        for i in range(len(data)):
            print(str(data[i]).ljust(max_size_rows[i]), end="|")
        print("")

    for i in range(sum(max_size_rows)+len(column_names)):
        print("=", end="")
    print("")

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

print("materials:")
sql_table(cur,
"""
SELECT * FROM public.materials
ORDER BY material_id ASC           
""")

print("suppliers:")
sql_table(cur,
"""
SELECT * FROM public.suppliers
ORDER BY supplier_id ASC          
""")

print("deliveries:")
sql_table(cur,
"""
SELECT * FROM public.deliveries
ORDER BY delivery_id ASC           
""")

print("Відобразити всі поставки, які здійснюються за 3 або менше днів, відсортувати назви постачальників за алфавітом:")
sql_table(cur,
"""
SELECT d.delivery_id, d.delivery_date, s.company_name, m.material_name, d.quantity, d.delivery_days
FROM deliveries d
JOIN suppliers s ON d.supplier_id = s.supplier_id
JOIN materials m ON d.material_id = m.material_id
WHERE d.delivery_days <= 3
ORDER BY s.company_name;            
""")

print("Порахувати суму, яку треба сплатити за кожну поставку (запит з обчислювальним полем):")
sql_table(cur,
"""
SELECT d.delivery_id, d.delivery_date, s.company_name, m.material_name, d.quantity, d.delivery_days, (d.quantity * m.price) AS total_cost
FROM deliveries d
JOIN suppliers s ON d.supplier_id = s.supplier_id
JOIN materials m ON d.material_id = m.material_id;         
""")

material_name = "Деревина"
print(f"Відобразити всі поставки обраного матеріалу({material_name}) (запит з параметром):")
sql_table(cur,
f"""
SELECT d.delivery_id, d.delivery_date, s.company_name, m.material_name, d.quantity, d.delivery_days
FROM deliveries d
JOIN suppliers s ON d.supplier_id = s.supplier_id
JOIN materials m ON d.material_id = m.material_id
WHERE m.material_name = '{material_name}';         
""")

print("Порахувати загальну кількість кожного матеріалу (підсумковий запит):")
sql_table(cur,
"""
SELECT m.material_name, SUM(d.quantity) AS total_quantity
FROM deliveries d
JOIN materials m ON d.material_id = m.material_id
GROUP BY m.material_name;      
""")

print("Порахувати кількість поставок від кожного постачальника (підсумковий запит):")
sql_table(cur,
"""
SELECT s.company_name, COUNT(d.delivery_id) AS delivery_count
FROM deliveries d
JOIN suppliers s ON d.supplier_id = s.supplier_id
GROUP BY s.company_name;    
""")

conn.commit()

cur.close()
conn.close()
print("\n=OK=")
