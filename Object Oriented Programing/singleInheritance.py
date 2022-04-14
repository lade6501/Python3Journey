import random

# Creating a Super class
class Oragnization:
    def __init__(self):
        print(f'self of org {id(self)}')
        self.oragnization_name = 'ABC limited'
    
    def assign_HR_to_employee(self):
        # Assigning HR based on employee's deputed location 
        if self.employee_location == 'Nagpur':
            self.hr_name = 'Nagpur HR'
        if self.employee_location == 'Pune':
            self.hr_name = 'Pune HR' 
        if self.employee_location == 'Chennai':
            self.hr_name = 'Chennai HR'
    
    def assign_salary_to_employee(self):
        # Salary for IT Domain
        if self.domain == 'IT' and self.degree == 'BE':
            self.salary = '3.6 lpa'
        if self.domain == 'IT' and (self.degree == 'BSC' or self.degree == 'BCA'):
            self.salary = '2.5 lpa'

        # Salary for BPS domain
        if self.domain == 'BPS' and self.degree == 'BE':
            self.salary = '2.4 lpa'
        if self.domain == 'BPS' and (self.degree == 'BSC' or self.degree == 'BCA'):
            self.salary = '1.89 lpa'

# Creating a subclass 
class Employee(Oragnization):
    employee_id = 1
    def __init__(self,name,degree):
        # print(f'self of emp {id(self)}')
        super().__init__()
        self.employee_id = Employee.employee_id
        self.employee_name = name     
        self.domain = random.choice(['IT','BPS'])
        self.degree = degree
        Employee.employee_id += 1

    def create_employee_profile(self):
        Employee.assign_location_to_employee(self)
        super().assign_HR_to_employee()
        super().assign_salary_to_employee()


    def assign_location_to_employee(self):
        location = random.choice(['Nagpur','Pune','Chennai'])
        self.employee_location = location

# Creating Instance of Employee class
employee_1 = Employee('XYZ','BE')
employee_1.create_employee_profile()

employee_2 = Employee('XYZ','BSC')
employee_2.create_employee_profile()

print('\t\t\t----------Employee 1 profile----------')
print(f'Employee Id \t\t\t: {employee_1.employee_id} ')
print(f'Employee Name \t\t\t: {employee_1.employee_name}')
print(f'Organization Name \t\t: {employee_1.oragnization_name}')
print(f'Employees Deputed location \t: {employee_1.employee_location}')
print(f'Employees HR Name \t\t: {employee_1.hr_name}')
print(f'Employee Domain \t\t: {employee_1.domain}')
print(f'Employee Salary \t\t: {employee_1.salary}')

print('\t\t\t----------Employee 2 profile----------')
print(f'Employee Id \t\t\t: {employee_2.employee_id} ')
print(f'Employee Name \t\t\t: {employee_2.employee_name}')
print(f'Organization Name \t\t: {employee_2.oragnization_name}')
print(f'Employees Deputed location \t: {employee_2.employee_location}')
print(f'Employees HR Name \t\t: {employee_2.hr_name}')
print(f'Employee Domain \t\t: {employee_2.domain}')
print(f'Employee Salary \t\t: {employee_2.salary}')
