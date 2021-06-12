num1 = float(input("Enter first number:"))
operator = input("Enter operation sign (multiplicate = *; addition = +; subtraction = -; division = /; potentiation = ^):")
num2 = float(input("Enter second number:"))
if operator == "*":
    num3 = num1 * num2
elif operator == "+":
    num3 = num1 + num2
elif operator == "-":
    num3 = num1 - num2
elif operator == "/":
    num3 = num1 / num2
elif operator == "^":
    num3 = pow(num1, num2)
else:
    print("invalid input, restart programm")
print(f"The result is {num3}")
