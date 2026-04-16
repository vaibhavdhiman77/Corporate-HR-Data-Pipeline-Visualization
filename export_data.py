import sqlite3
import csv

# 1. Database se connect karo
conn = sqlite3.connect('EMS_Database.db')
cursor = conn.cursor()

# 2. Saara data fetch karo
cursor.execute("SELECT * FROM employees")
records = cursor.fetchall()

# 3. CSV file mein write karo
with open('Clean_HR_Data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Pehle Headers (Column names) daalo
    writer.writerow(['Employee_ID', 'Name', 'Age', 'Department', 'Salary'])
    # Phir saara data daal do
    writer.writerows(records)

print("✅ Data successfully 'Clean_HR_Data.csv' mein export ho gaya!")
conn.close()