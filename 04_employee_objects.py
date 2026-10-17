class Employee:
    def __init__(self, employee_name, employee_salary):
        self.employee_name = employee_name
        self.employee_salary = employee_salary

    def display(self):
        print("Name:", self.employee_name)
        print("Salary:", self.employee_salary)

first_employee = Employee("Amit", 20000)
second_employee = Employee("Priya", 25000)
first_employee.display()
second_employee.display()
