import json
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'solarcar'
}

# Establish database connection
try:
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    print("Successfully connected to the database.")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL Database: {e}")
    exit()

# Function to read JSON data from a file
def read_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# List of table names and their corresponding JSON files
tables_files = {
    'battery': 'battery.json',
    'brake': 'brake.json',
    'cabin': 'cabin.json',
    'motor_controller': 'motor_controller.json',
    'mppt': 'mppt.json',
    'wheel': 'wheel.json'
}

# Insert data into the database from JSON
for table, file_name in tables_files.items():
    data = read_json_data(file_name)
    for record in data:
        placeholders = ', '.join(['%s'] * len(record))
        columns = ', '.join(record.keys())
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        values = tuple(record.values())
        try:
            cursor.execute(sql, values)
            db.commit()
            print(f"Record inserted successfully into {table} table")
        except mysql.connector.Error as e:
            print(f"Failed to insert record into {table} table: {e}")
            db.rollback()

# Close the database connection
cursor.close()
db.close()
