nums = [3, 0, 1]  

n = len(nums)
total_sum = n * (n + 1) // 2  
array_sum = sum(nums)  

missing_number = total_sum - array_sum  
print(missing_number)
