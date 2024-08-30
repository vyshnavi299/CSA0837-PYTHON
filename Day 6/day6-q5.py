nested_lst = [[1, 2], [3], [4, 5, 6]]

total_sum = sum(sum(inner_lst) for inner_lst in nested_lst)

print(total_sum)
