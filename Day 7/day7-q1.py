
elements = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


values_even_keys = [value for key, value in elements.items() if key % 2 == 0]

print(values_even_keys) 
