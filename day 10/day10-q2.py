import string


file_name = 'example.txt'
with open(file_name, 'r') as file:
    for line in file:
    
        words = line.split()
    
        processed_words = [word.strip(string.punctuation).lower() for word in words]
        print(processed_words)
