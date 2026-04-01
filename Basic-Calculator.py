def add(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b

print("1. Add")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while True:
    calculation_type = input("Please choose the calculation type.(1-4)")
    options = ("1","2","3","4")
    if calculation_type in options:

        if calculation_type == "1":
            a = int(input("Please enter the first number for addition. "))
            b = int(input("Please enter the second number for addition. "))
            print(add(a,b))
            kill_calculation = input("If you want to quit, please press 'q' ")
            if kill_calculation == "q":
                print("Thank you for using IamOzansson's basic Python calculation. Have a great day!")
                break

        elif calculation_type == "2":
            a = int(input("Please enter the first number for subtraction. "))
            b = int(input("Please enter the second number for subtraction. "))
            print(subtraction(a,b))
            kill_calculation = input("If you want to quit, please press 'q' ")
            if kill_calculation == "q":
                print("Thank you for using IamOzansson's basic Python calculation. Have a great day!")
                break

        elif calculation_type == "3":
            a = int(input("Please enter the first number for multiplication. "))
            b = int(input("Please enter the second number for multiplication. "))
            print(multiplication(a,b))
            kill_calculation = input("If you want to quit, please press 'q' ")
            if kill_calculation == "q":
                print("Thank you for using IamOzansson's basic Python calculation. Have a great day!")
                break
            
        elif calculation_type == "4":
            a = int(input("Please enter the first number for division. "))
            b = int(input("Please enter the second number for division. "))
            print(division(a,b))
            kill_calculation = input("If you want to quit, please press 'q' ")
            if kill_calculation == "q":
                print("Thank you for using IamOzansson's basic Python calculation. Have a great day!")
                break
