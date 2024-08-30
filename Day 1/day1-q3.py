
d1 = input("Enter the 1st binary digit (0 or 1): ")
d2 = input("Enter the 2nd binary digit (0 or 1): ")
d3 = input("Enter the 3rd binary digit (0 or 1): ")
d4 = input("Enter the 4th binary digit (0 or 1): ")


binary_number = d1 + d2 + d3 + d4

decimal_value = int(binary_number, 2)

print("The value in base 10 is:", decimal_value)
