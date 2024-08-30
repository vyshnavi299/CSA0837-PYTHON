
file_name = 'example.txt'  
with open(file_name, 'r') as file:
    lines = file.readlines()


print("Number of lines in the file:", len(lines))
