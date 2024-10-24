# try:
#     width = float(input("width: "))
#     length = float(input("length: "))
#
#     if width == length:
#         exit("This is a square")
#     else:
#         area = width * length
#         print(area)
#
# except ValueError:
#     print("Enter only digits")
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    result = value / total_value * 100
    print(f"That is {result}%")
except ValueError:
    print("You need to enter a number. Run the program again")
