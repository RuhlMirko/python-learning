filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for files in filenames:
    file = open(f"files/{files}", 'w')
    file.write("Hello")
    file.close()

