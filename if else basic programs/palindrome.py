
s = input("Enter a string: ")


modified_s = s.replace(" ", "").lower()


rev = modified_s[::-1]


if modified_s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

