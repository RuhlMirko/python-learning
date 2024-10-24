def get_average():
    with open('txt_files/data.txt', 'r') as file:
        content = file.readlines()

    values = content[1:]
    values = [float(i) for i in values]

    average_temp = sum(values) / len(values)
    return average_temp


average = get_average()

print(average)
