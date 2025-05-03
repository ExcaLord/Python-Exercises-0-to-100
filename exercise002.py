# Basic Calculator, include addition, subtraction, multiplication, and division

operations = input("Enter one of the following math operations: +, -, *, / ")
num1 = float(input("Enter the first number to operate with: "))
num2 = float(input("Enter the second number to operate with: "))

if operations == "+":
    print(f"{num1} + {num2} is equal to = {num1 + num2}, that was easy!")
elif operations == "-":
    print(f"{num1} - {num2} is equal to = {num1 - num2}, that was easy!")
elif operations == "*":
    print(f"{num1} * {num2} is equal to = {num1 * num2}, that was easy!")
elif operations == "/":
    print(f"{num1} / {num2} is equal to = {num1 / num2}, that was easy!")
else:
    print("Invalid operator")
