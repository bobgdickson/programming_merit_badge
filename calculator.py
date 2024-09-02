# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")

    choice = input("Enter choice (1/2): ")

    if choice in ['1', '2']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")

    else:
        print("Invalid input")

# Run the calculator
calculator()
