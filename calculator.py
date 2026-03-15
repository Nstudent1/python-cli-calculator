print("Welcome to the Calculator App!\n")

# Function to get a valid operation from the user
def get_valid_operation():
    while True:
        operation = input("Would you like to add, subtract, multiply, or divide? Type add for addition, sub for subtraction, mul for multiplication, and div for division:\n")
        if operation in ("add", "sub", "mul", "div"):
            return operation
        else:
            print("Invalid operation. Please try again.")

# Function to perform calculation based on operation
def calculate(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mul":        
        return num1 * num2
    else:
        return num1 / num2

# Main program loop
iterate = True
while iterate:
    # Get operation for this calculation
    operation = get_valid_operation()

    # Get numbers for the calculation
    while True:
        try:
            num1 = float(input("Enter the first number to perform operation: "))
            num2 = float(input("Enter the second number to perform operation: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    result_of_calculation = calculate(operation, num1, num2)
    print(f"The result is: {result_of_calculation}")

    # Ask if user wants to continue
    while True:
        repete = input("Would you like to perform another calculation? Type yes to continue or no to exit:\n")
        
        if repete.lower() == "no":
            iterate = False
            print("Thank you for using the Calculator App. Goodbye!")
            break
        elif repete.lower() == "yes":
            break
        else:
            print("Invalid input. Please type yes or no.")


