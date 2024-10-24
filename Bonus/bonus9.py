password = input("Enter a new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

#  Checks if it has at least three digits
counter = 0
for i in password:
    if i.isdigit():
        counter += 1

if counter >= 3:
    result["digits"] = True
else:
    result["digits"] = False

upper_char = False
for char in password:
    if char.isupper():
        upper_char = True

result["upper"] = upper_char

if all(result.values()):
    print("Strong password")
else:
    print("Weak Password")

