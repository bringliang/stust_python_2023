class employee():
    def __init__(self,emp_name,emp_id,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department

    def calculate_emp_salary(self,emp_salary,hours_worked):
        self.emp_salary=emp_salary
        self.hour_worked=hours_worked
        if hours_worked>50:
            return f"Salary: {(self.hour_worked-50)*(self.emp_salary/50)+emp_salary}"
        else:
            return f"Salary: {self.emp_salary}"

    def print_employee_details(self):
        print(f"Name: {self.emp_name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: {self.emp_salary}")
        print(f"Department: {self.emp_department}")

    def emp_assign_department(self,emp_department):
        self.emp_department=emp_department

emp1=employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp1.print_employee_details()
emp1.emp_assign_department("OPERATIONS")
emp1.print_employee_details()
print(emp1.calculate_emp_salary(5000,60))
print(emp1.calculate_emp_salary(5000,40))