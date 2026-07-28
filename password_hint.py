#This script helps users ro remember their passwords by showing a secure  hint.

user = input("Enter your secret password: ").strip()

first_char = user[0]
last_char = user[-1]

print(f'"Your password hint: It starts with {first_char} and ends with {last_char}"')