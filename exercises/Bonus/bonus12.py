feet_inches = input("Feet and inches: ")


def convert(imperial):
    feet = float(imperial.split(' ')[0])
    inches = float(imperial.split(' ')[1])

    meters = feet * 0.3048 + inches * 0.0254

    return meters

result = convert(feet_inches)


if result < 1.0:
    print("Too small")
else:
    print("Enjoy the ride")



