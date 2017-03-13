#letters in English word that never appear doubled
#e.g, 'qq', 'xx' never appear doubled
import scrabble
import string

for letter in string.ascii_lowercase:
    exists =  False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            break #even if 'ww' for instance, happens once, this case fails our test so we exit the inner-forloop, and move on to the next letter in ascii_lowercase
    if not exists:
        print("There are no English words with a double " + letter)
