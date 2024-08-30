
names = input("Enter a list of first names separated by spaces: ").split()

count_a = sum(name.count('a') for name in names)

print(f"The letter 'a' appears {count_a} times in the list.")
