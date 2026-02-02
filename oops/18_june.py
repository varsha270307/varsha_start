 

# Q.1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

s = Student("Varsha", 20, "CS09")
s.display()

# Q.2

class Vehicle:
    def __init__(self):
        self.type = "Transport"

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__()
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, brand, battery_range):
        super().__init__(brand)
        self.battery_range = battery_range

    def display(self):
        print(f"Type: {self.type}, Brand: {self.brand}, Range: {self.battery_range} km")

ec = ElectricCar("TATA_NEXON", 400)
ec.display()


# Q.3

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand)
        self.model = model
        self.year = year

c = Car("TATA", "Nexon", 2023)
print(c.brand, c.model, c.year)


# Q.4

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(150)
print("Total pages:", b1 + b2)


# Q.5

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started with key")

c = Car()
c.start()

# Q.6

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

s = Student("Varsha", 85)
print(s.get_name(), s.get_marks())
s.set_marks(90)
print("Updated Marks:", s.get_marks())

# Q.7

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Price: {self.price}"

b = Book("Python Basics", "John Doe", 499)
print(b)


