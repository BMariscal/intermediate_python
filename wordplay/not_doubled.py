#letters in English word that never appear doubled
#e.g, 'qq', 'xx' never appear doubled
import scrabble
import string

letters = string.ascii_lowercase
dict={}
for letter in letters:
    for item in scrabble.wordlist:
        if letter + letter not in item:
            dict[letter] = dict.get(letter,0)
        else:
            dict[letter] = dict.get(letter,0)+1


a=[key for key, val in dict.items() if val == 0]
b=' and '.join(a)
print('{0} are letters that do not double in the English language'.format(b))



