import csv
import psycopg2
from psycopg2 import OperationalError

def connect_db():
    try:
        return psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="suppliers",
            user="postgres",
            password="080808"
        )
    except OperationalError as e:
        # Print an error message if connection fails
        print(f"Error connecting to the database: {e}")
        return None

def create_table():
    # Attempt to establish a connection
    conn = connect_db()
    if conn is None:
        return

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    try:
        # Create the phonebook table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone VARCHAR(15) UNIQUE NOT NULL
            );
        """)
        conn.commit()
        print("Table created successfully.")
    except OperationalError as e:
        # Print an error message if table creation fails
        print(f"Error creating table: {e}")
    finally:
        # Close cursor and connection
        cur.close()
        conn.close()

def load_from_csv():
    # Attempt to establish a connection
    conn = connect_db()
    if conn is None:
        return

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    try:
        # Open the CSV file and insert data into the database
        with open('/Users/nuraiaitbazar/Desktop/pp2/Lab10/phonebook.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
                    row
                )
        conn.commit()
        print("Data loaded from CSV successfully.")
    except (OperationalError, FileNotFoundError, IOError) as e:
        # Print an error message if data loading fails
        print(f"Error loading data from CSV: {e}")
    finally:
        # Close cursor and connection
        cur.close()
        conn.close()

def main():
    create_table()
    while True:
        print("1. Load data from CSV")
        print("2. Add data via console")
        print("3. Update data")
        print("4. View all records")
        print("5. Delete data")
        print("6. Exit")
        choice = input("Choose an action: ")
        
        if choice == '1':
            load_from_csv()
        # Add other options similarly...
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()