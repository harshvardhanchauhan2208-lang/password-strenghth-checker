import re

password = input("Enter password: ")

length = len(password) >= 8
upper = re.search("[A-Z]", password)
digit = re.search("[0-9]", password)
symbol = re.search("[@#$%^&*!]", password)

if length and upper and digit and symbol:
    print("Strong password")
else:
    print("Weak password")