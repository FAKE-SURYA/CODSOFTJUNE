operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print(f"Operator '{operator}' is invalid.")
