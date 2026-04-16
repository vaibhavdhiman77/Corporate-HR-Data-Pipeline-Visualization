import sqlite3

# Database connection helper
def connect_db():
    return sqlite3.connect('EMS_Database.db')

# 1. READ: View Employees
def view_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees LIMIT 10")
    records = cursor.fetchall()
    print("\n" + "="*50)
    print("📋 TOP 10 EMPLOYEE RECORDS")
    print("="*50)
    for row in records:
        print(f"ID: {row[0]} | Name: {row[1]:<15} | Dept: {row[3]:<10} | Salary: ₹{row[4]}")
    conn.close()

# 2. READ: Search Employee
def search_employee():
    emp_id = input("\n🔍 Enter Employee ID to search: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    row = cursor.fetchone()
    if row:
        print("\n✅ Record Found!")
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Dept: {row[3]} | Salary: ₹{row[4]}")
    else:
        print("\n❌ Koi record nahi mila!")
    conn.close()

# 3. CREATE: Add New Employee
def add_employee():
    print("\n➕ Add New Employee")
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO employees VALUES (?,?,?,?,?)", (emp_id, name, age, dept, salary))
        conn.commit()
        print(f"\n✅ {name} successfully add ho gaya!")
    except sqlite3.IntegrityError:
        print("\n❌ Error: Is ID ka employee pehle se exist karta hai!")
    conn.close()

# 4. UPDATE: Edit Employee Details [cite: 27]
def update_employee():
    emp_id = input("\n✏️ Jis employee ko update karna hai uski ID dalein: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    if cursor.fetchone():
        new_salary = input("Nayi Salary enter karein: ")
        new_dept = input("Naya Department enter karein: ")
        cursor.execute("UPDATE employees SET salary=?, department=? WHERE id=?", (new_salary, new_dept, emp_id))
        conn.commit()
        print("\n✅ Record successfully update ho gaya!")
    else:
        print("\n❌ Is ID ka koi record nahi mila.")
    conn.close()

# 5. DELETE: Remove Employee [cite: 28]
def delete_employee():
    emp_id = input("\n🗑️ Jis employee ko delete karna hai uski ID dalein: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
        conn.commit()
        print("\n✅ Record hamesha ke liye delete ho gaya!")
    else:
        print("\n❌ Is ID ka koi record nahi mila.")
    conn.close()

# MAIN MENU
def main_menu():
    while True:
        print("\n" + "*"*50)
        print("🏢 EMPLOYEE MANAGEMENT SYSTEM (EMS) - FULL CRUD")
        print("*"*50)
        print("1. View Employees")
        print("2. Search Employee by ID")
        print("3. Add New Employee")
        print("4. Update Employee Details")
        print("5. Delete Employee")
        print("6. Exit Application")
        
        choice = input("\nApna option chuniye (1-6): ")
        
        if choice == '1': view_employees()
        elif choice == '2': search_employee()
        elif choice == '3': add_employee()
        elif choice == '4': update_employee()
        elif choice == '5': delete_employee()
        elif choice == '6': 
            print("\n👋 System closing... Bye!")
            break
        else: print("\n❌ Galat option! Kripya 1 se 6 ke beech chunein.")

if __name__ == "__main__":
    main_menu()