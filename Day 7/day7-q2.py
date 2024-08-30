
input_list = input("Enter a list of integers separated by spaces: ").split()
int_list = [int(x) for x in input_list]

result_list = ['over' if x > 100 else x for x in int_list]

print(result_list)
