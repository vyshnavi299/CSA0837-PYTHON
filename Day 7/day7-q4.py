
list1 = input("Enter integers for the first list, separated by spaces: ").split()
list2 = input("Enter integers for the second list, separated by spaces: ").split()

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]


same_length = len(list1) == len(list2)

same_sum = sum(list1) == sum(list2)


common_elements = set(list1) & set(list2)

print("Same length:", same_length)
print("Same sum:", same_sum)
print("Common elements:", common_elements)
