feet_inches = input("Feet and inches: ")


def parse(imperial):
    feet = float(imperial.split(' ')[0])
    inches = float(imperial.split(' ')[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_r = parse(feet_inches)['feet']
inches_r = parse(feet_inches)['inches']
result = convert(feet_r, inches_r)
print(f"{feet_r} feet and {inches_r} is equal to {result}")

if result < 1.0:
    print("Too small")
else:
    print("Enjoy the ride")
