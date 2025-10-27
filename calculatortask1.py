
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def calcu():
    while True:
        print("\n=== Simple Calculator ===")
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting Calculator... ")
            print("Thanks for using Calculator")
            break

 
        try:
            num1 = float(input("Enter Your first number: "))
            num2 = float(input("Enter Your second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

      
        if choice == '1':
            result = addition(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == '2':
            result = subtraction(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

        else:
            print("Invalid choice! Please select a valid operation.")


calcu()
