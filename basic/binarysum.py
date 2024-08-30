
a = input("Enter the first binary string: ")
b = input("Enter the second binary string: ")

sum = bin(int(a, 2) + int(b, 2))[2:]

print("The sum as a binary string is:", sum)
