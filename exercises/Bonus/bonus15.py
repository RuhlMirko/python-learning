import glob

my_files = glob.glob('txt_files/*.txt')

for filepath in my_files:
    with open(filepath, 'r') as file:
        print(file.readlines())

print(my_files)
