words = input("Enter a list of words separated by spaces: ").split()

anagram_dict = {}
for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]

for anagrams in anagram_dict.values():
    if len(anagrams) > 1:
        print(anagrams)
