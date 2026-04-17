def add(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b

operations = { "1": add,
               "2": subtraction,
               "3": multiplication,
               "4": division
               }
print("Welcome to IamOzansson's basic calculator program.")

while True:
    calculation_type = input("Please choose the calculation type.(1-4): ")

    if calculation_type in operations:
        a = float(input("Please enter your first number: "))
        b = float(input("Please enter your second number: "))

        result = operations[calculation_type](a, b)
        print(result)
        quit_calculator = input("If you want to quit the program, " \
        "please press q to quit or press Enter to continue: ")

        if quit_calculator == "q":
            print("Thank you for using IamOzansson's calculator. Have a great day!")
            break
    else:
        print("Your input is invalid. Please try again.")
