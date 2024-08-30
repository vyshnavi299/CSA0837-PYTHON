
positive_count = 0
negative_count = 0


while True:
    number = int(input("Enter an integer (or enter 0 to stop): "))

    if number == 0:
        break

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1


print(f"Number of positive values entered: {positive_count}")
print(f"Number of negative values entered: {negative_count}")
