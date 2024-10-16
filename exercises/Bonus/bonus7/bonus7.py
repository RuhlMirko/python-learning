filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

# print(filenames)


user_entries = ['10', '19.1', '20']

float_conversion = [float(new_number) for new_number in user_entries]
sum_of_num = [sum(float_conversion)]
print(sum_of_num)

