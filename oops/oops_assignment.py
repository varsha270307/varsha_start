#1
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")



student1 = Student("Alice", 101, 89)
student2 = Student("Bob", 102, 92)
student3 = Student("Charlie", 103, 76)


student1.display_details()
student2.display_details()
student3.display_details()

# Q.2
class Employee:
    company_name = "C-DAC Patna"  

    def __init__(self, emp_name):
        self.emp_name = emp_name  



emp1 = Employee("Raj")
emp2 = Employee("Priya")

print(f"Employee 1: {emp1.emp_name}, Company: {Employee.company_name}")
print(f"Employee 2: {emp2.emp_name}, Company: {Employee.company_name}")

# Q.3

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Engine started for {self.brand} {self.model}")



car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)


car1.start_engine()
car2.start_engine()

# Q.4

class Employee:
    company_name = "CDAC"  
    def __init__(self, emp_name, emp_id, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary

    def show_employee(self):
        print(f"Name: {self.emp_name}, ID: {self.emp_id}, Salary: {self.salary}, Company: {Employee.company_name}")



emp1 = Employee("Amit", 201, 50000)
emp2 = Employee("Neha", 202, 60000)


emp1.show_employee()
emp2.show_employee()


Employee.company_name = "CDAC Noida"


emp1.show_employee()
emp2.show_employee()


# exception handling

