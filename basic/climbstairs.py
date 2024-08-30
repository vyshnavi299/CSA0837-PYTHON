
n = int(input("Enter the number of steps: "))

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:

    prev1, prev2 = 1, 2
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current

    

    print(current)
