# Simple Calculator Program in Python

# Step 1: Ask the user to input two numbers

num1 = float(input("Enter first number: "))  # Convert input to float to allow decimal numbers

num2 = float(input("Enter second number: ")) 

# Step 2: Ask the user to input the operation they want to perform

operation = input("Enter operation (add, subtract, multiply, divide): ")  # User inputs +, -, * or /

# Step 3: Use conditional statements to perform the operation based on user input

if operation == 'add':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")  # Display addition result


elif operation == 'subtract':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")  # Display subtraction result

elif operation == 'multiply':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")  # Display multiplication result

elif operation == 'divide':
    # Step 4: Handle division carefully
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} divided by {num2} = {result}")  # Display division result

    else:
        print("Error: Cannot divide by zero.")  # Avoid division by zero error

else:
    # Step 5: If user inputs invalid operation symbol
    print("Invalid operation. Please enter one of add, subtract, multiply, divide")
