import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='students',
    user='postgres',
    password='080808'
)

# create cursor to work with the database 
cur = conn.cursor()

# create new table
cur.execute("""CREATE TABLE students_data(
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(20)
);
""")

# create new students
cur.execute("""INSERT INTO students_data (name, id, phone_number) VALUES
            ('Nuray', '1', '+7 777 208 08 08'),
            ('Islam', '2', '+7 700 777 77 77')
""")

conn.commit()