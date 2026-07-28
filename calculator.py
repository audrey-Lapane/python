#This program takes two input and performs four basi arithmetic calculation.

num1 = float(input("Enter number a:"))
num2 = float(input("Enter number b:"))

sum = num1 + num2
subtraction = num1 - num2
multiply = num1 * num2

print(f"Addition of : {num1} + {num2} = {round(sum,2)} ")
print(f"Subtraction of: {num1} - {num2} = {round(subtraction,2)}")
print(f"Multiplication of: {num1} * {num2} = {round(multiply,2)}")

if num2 != 0:
    division = num1 / num2 
    print(f"Division of: {num1} / {num2} = {round(division,2)}")
    floor_div = num1 // num2
    mod = num1 % num2
    print(f"Floor_division of: {num1} // {num2} = {round(floor_div,2)}")
    print(f"Modulus of: {num1} % {num2} = {round(mod,2)}")
else:
    print("Division by zero.....")

floor_div = num1 // num2
mod = num1 % num2
print(f"Floor_division of: {num1} // {num2} = {round(floor_div,2)}")
print(f"Modulus of: {num1} % {num2} = {round(mod,2)}")