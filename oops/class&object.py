class Student:
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    def greet(self):
        print("Welcome to my Home")    
        
obj1=Student("Varsha",20)
obj2=Student("Radhe",19)
obj3=Student("Ritika",21)
obj4=Student("Neha",20)
obj5=Student("Jyoti",22)


print(obj1.name)
print(obj1.age)
print(obj2.name)
print(obj2.age)
print(obj3.name)
print(obj3.age)
print(obj4.name)
print(obj4.age)
print(obj5.name)
print(obj5.age)

obj1.greet()


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
