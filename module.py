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
