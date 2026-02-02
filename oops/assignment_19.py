# Q.1

import math

def calculator():
    try:
        print("1.Add 2.Sub 3.Mul 4.Div 5.Sqrt")
        ch = input("Choose: ")
        if ch == '5':
            n = float(input("Number: "))
            if n < 0:
                raise ValueError("Negative sqrt!")
            print("Result:", math.sqrt(n))
        else:
            a = float(input("A: "))
            b = float(input("B: "))
            if ch == '1': print("Sum:", a + b)
            elif ch == '2': print("Sub:", a - b)
            elif ch == '3': print("Mul:", a * b)
            elif ch == '4':
                if b == 0: raise ZeroDivisionError("Can't divide by 0")
                print("Div:", a / b)
            else: print("Invalid choice")
    except Exception as e:
        print("Error:", e)
   
    

# Q.2

def read_file():
    try:
        name = input("Filename: ")
        with open(name, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("No permission.")


# Q.3

class QuantityError(Exception): pass

class Item:
    def __init__(self, name, qty, price):
        if price <= 0: raise ValueError("Price > 0")
        self.name, self.qty, self.price = name, qty, price

    def update(self, qty, price):
        if price <= 0: raise ValueError("Price > 0")
        if self.qty + qty < 0: raise QuantityError("Qty < 0")
        self.qty += qty
        self.price = price

class Inventory:
    def __init__(self): self.items = []
    def add(self, item): self.items.append(item)


# Q.4

def grade_check():
    try:
        name = input("Name: ")
        marks = [int(input(f"Mark {i+1}: ")) for i in range(5)]
        if any(m < 0 or m > 100 for m in marks):
            raise ValueError("Marks 0-100 only")
        print("Average:", sum(marks) / 5)
    except Exception as e:
        print("Error:", e)


# Q.5

def login():
    try:
        user = input("Username: ")
        pwd = input("Password: ")
        if not user or not pwd:
            raise ValueError("Empty username or password")
        print("Login successful.")
    except ValueError as e:
        print("Error:", e)



