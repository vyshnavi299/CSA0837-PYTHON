
file_name = input("Enter the file name: ")

with open(file_name, 'r') as file:
    for line in file:
    
        if '#' in line:
            print(line.strip())
