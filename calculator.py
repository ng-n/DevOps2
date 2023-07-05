#!/bin/env python3

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return num1/num2

if __name__ == "__main__":
    print("Welcome to the Calculator Program!")

    try: 
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number:"))

        print("Please select an operation")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")

        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            result = addition(num1, num2)
            operation = "addition"
        elif choice == 2:
            result = subtraction(num1, num2)
            operation = "subtraction"
        elif choice == 3:
            result = multiplication(num1, num2)
            operation = "multiplication"
        elif choice == 4:
            result = division(num1, num2)
            operation = "division"
        else:
            raise ValueError("Invalid option. Please selecte a number between 1 and 4.")
        print(f"The result of {operation} is {result}")
    
    except ValueError as ve:
        print("Invalid input: ", str(ve))
    except Exception as e:
        print("An error occured: ", str(e))