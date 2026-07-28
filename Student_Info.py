#Student info Formatter
import math

Greeting = "Welcome to Student info Formatter"
plan = "Please enter all that follow:"

print(Greeting)
print(plan)

fname = input("Enter you first name: ")
surname = input("Enter your Surmane: ")
age = int(input("Enter Age: "))
Fnumber = float(input("Enter favourite number: "))

print(f"Welcome, {fname} {surname}!")
print(fname.upper(), fname.title())

age_in_months = age * 12

print(f"Your age in months {age_in_months}")
round(Fnumber, 2)
print(f"Favourite number rounded: {Fnumber}")
print(type(fname))
print(type(surname))
print(type(age))
print(type(Fnumber))



