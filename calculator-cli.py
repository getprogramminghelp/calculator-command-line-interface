from decimal import Decimal

# Function definitions for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Display the welcome message
print("Welcome to the calculator program!")

while True:
    # Display the menu
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get user choice
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        # Exit the program if choice is 5
        print("Thank you for using the calculator program. Goodbye!")
        break

    try:
        # Get the input numbers
        num1 = Decimal(input("Enter the first number: "))
        num2 = Decimal(input("Enter the second number: "))

        if choice == "1":
            # Perform addition
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == "2":
            # Perform subtraction
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == "3":
            # Perform multiplication
            result = multiply(num1, num2)
            print("Result: ", result)
        elif choice == "4":
            # Perform division
            result = divide(num1, num2)
            print("Result: ", result)
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

        # Prompt the user to press Enter to clear the screen
        input("Press Enter to clear the previous screen...")

        # Clear the screen
        print("\033c")

    except ValueError:
        # Invalid input
        print("Invalid input. Please enter numbers only.")

# This code is developed by domyprogramminghomework.io
