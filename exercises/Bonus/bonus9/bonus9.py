password = input("Enter a new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

#  Checks if it has at least three digits
counter = 0
for i in password:
    if i.isdigit():
        counter += 1

if counter >= 3:
    result.append(True)
else:
    result.append(False)

upper_char = False
for char in password:
    if char.isupper():
        upper_char = True

result.append(upper_char)

if all(result):
    print("Strong password")
else:
    print("Weak Password")

