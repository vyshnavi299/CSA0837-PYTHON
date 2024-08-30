total_sum = 0


while True:
    number = int(input("Enter a positive integer (or enter 0 to stop): "))

    if number == 0:
        break

    if number <= 100:
        total_sum += number


print(f"The sum of the entered integers (excluding numbers greater than 100) is: {total_sum}")
