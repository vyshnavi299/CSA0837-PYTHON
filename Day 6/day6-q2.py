lst = [1, 2, 3, 4]
cumulative_sum = []

sum_so_far = 0
for num in lst:
    sum_so_far += num
    cumulative_sum.append(sum_so_far)

print(cumulative_sum)
