
s = "hello world"


frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1


sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)


for char, freq in sorted_chars:
    print(f"{char}: {freq}")
