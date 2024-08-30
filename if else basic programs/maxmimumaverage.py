nums = [1, 12, -5, -6, 50, 3]
k = 4

current_sum = sum(nums[:k])
max_sum = current_sum


for i in range(k, len(nums)):
    current_sum += nums[i] - nums[i - k]  
    if current_sum > max_sum:
        max_sum = current_sum


max_average = max_sum / k


print(f"{max_average:.5f}")  
