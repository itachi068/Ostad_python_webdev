print("Choose an operation:")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")

# Get user input
operation = int(input("Enter the operation: "))


# Perform calculation based on the operation
if operation == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print("Addition is : " + str(result))
elif operation == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 - num2
    print("Subtraction is : " + str(result))
elif operation == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    print("Multiplication is : " + str(result))
elif operation == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Division is : " + str(result))
else:
    print("Invalid operation.")


