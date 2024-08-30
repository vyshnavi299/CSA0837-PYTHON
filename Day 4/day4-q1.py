
a = 27
b = 3

if b == 1:
    result = (a == 1)
else:
    
    if b <= 0:
        result = False
    else:
    
        temp = a
        while temp > 1:
            if temp % b != 0:
                result = False
                break
            temp //= b
        else:
            result = (temp == 1)

print(result)
