temperatures = [10, 12, 14]

file = open("file.txt", 'w')
temperatures = [str(item)+'\n' for item in temperatures]
file.writelines(temperatures)
file.close()

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)
