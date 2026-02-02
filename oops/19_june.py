#try:
#     variable=int(input("Please enter a number:"))
#     result=variable+100
#     print(result)
#except Exception as e:
#    print(e)
#finally:
#    print("code executed") 
    
def addition(num1,num2):
    print(f"Addition is {num1+num2}")
 
def subtraction(num1,num2):
    print(f"Subtraction  is {num1-num2}")  
    
def division(num1,num2):
    try:
        print(f"Division is {num1/num2}")    
    except ZeroDivisionError:
        print("Second number cannot be zero ")  
    
while True:
    print("[1] perform addition\n[2] perform substraction\n[3] Exit")
    
try:
     choice=int(input("Enter your choice "))
     if Choice!=4:
     
        num1=int(input("Enter 1st number "))
        num2=int(input("Enter 2nd number"))   
    
    
except ValueError as e:
    print("Please enter valid number as a input")       

      
    match choice:
        case 1:
            addition(num1,num2)
        case 2:
            subtraction(num1,num2)
        case 3:
            print("exiting the applicaton... ")   
        
        case _:
            print("Enter a valid number shown above")
                     




            