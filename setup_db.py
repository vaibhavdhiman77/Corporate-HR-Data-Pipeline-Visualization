import sqlite3
import os

# Check karne ke liye ki file kahan hai
if not os.path.exists('employees_500.txt'):
    print("Error: 'employees_500.txt' nahi mili! Please use sahi folder mein rakho.")
else:
    conn = sqlite3.connect('EMS_Database.db')
    cursor = conn.cursor()

    # Table creation
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL
        )
    ''')

    # Data loading
    with open('employees_500.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 5:
                cursor.execute('INSERT INTO employees VALUES (?,?,?,?,?)', 
                               (int(data[0]), data[1], int(data[2]), data[3], float(data[4])))
    
    conn.commit()
    print("Success! 500 records insert ho gaye hain.")
    conn.close()