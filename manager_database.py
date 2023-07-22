import sqlite3

def connect_db():
    return sqlite3.connect('employee.db')

def add_employee(name, designation, salary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, designation, salary) VALUES (?, ?, ?)', (name, designation, salary))
    conn.commit()
    conn.close()

def get_employee(employee_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    return employee

def get_all_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def update_employee(employee_id, name, designation, salary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE employees SET name=?, designation=?, salary=? WHERE id=?', (name, designation, salary, employee_id))
    conn.commit()
    conn.close()

def delete_employee(employee_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id=?', (employee_id,))
    conn.commit()
    conn.close()


def main():
    while True:
        print("\nEmployee Database Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. View All Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            designation = input("Enter employee designation: ")
            salary = float(input("Enter employee salary: "))
            add_employee(name, designation, salary)
            print("Employee added successfully!")

        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            employee = get_employee(employee_id)
            if employee:
                print(f"Employee ID: {employee[0]}")
                print(f"Name: {employee[1]}")
                print(f"Designation: {employee[2]}")
                print(f"Salary: {employee[3]}")
            else:
                print("Employee not found!")

        elif choice == '3':
            employees = get_all_employees()
            if employees:
                print("All Employees:")
                for employee in employees:
                    print(f"ID: {employee[0]}, Name: {employee[1]}, Designation: {employee[2]}, Salary: {employee[3]}")
            else:
                print("No employees found!")

        elif choice == '4':
            employee_id = int(input("Enter employee ID: "))
            employee = get_employee(employee_id)
            if employee:
                name = input("Enter employee name: ")
                designation = input("Enter employee designation: ")
                salary = float(input("Enter employee salary: "))
                update_employee(employee_id, name, designation, salary)
                print("Employee updated successfully!")
            else:
                print("Employee not found!")

        elif choice == '5':
            employee_id = int(input("Enter employee ID: "))
            employee = get_employee(employee_id)
            if employee:
                delete_employee(employee_id)
                print("Employee deleted successfully!")
            else:
                print("Employee not found!")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
