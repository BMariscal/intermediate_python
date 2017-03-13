#find words that contain all vowels A,E,I,O,U
#use function
import scrabble

def all_vowels(words):
    newlist=[]
    for word in words:
        if 'a' in word and \
        'e' in word and \
        'i' in word and \
        'o' in word and \
        'u' in word:
            newlist.append(word)
    return newlist








if __name__ == "__main__":
    final_list=all_vowels(scrabble.wordlist)
    print('\n'.join(final_list))
