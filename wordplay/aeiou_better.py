# english word that contains all vowels A,E,I, O,U
import scrabble

vowels = 'aeiou'
def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word: # if it doesn't have a (but has eiou) then we can stop the loop and return False, because our requirement dictates that it needs to have all the vowels
            return False
    return True


for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)
