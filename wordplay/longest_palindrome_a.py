#find longest palindrome in the English language

#I decided to use a deque, because you can pull items from both ends

from deque import Deque
import scrabble

def is_palindrome(wordlist):

    def create_deque(word):
        chardeque = Deque()

        for char in word:
            chardeque.addRear(char)
        return chardeque


    pal_list = []
    for word in wordlist:
        # print(word)
        newdeque = create_deque(word)
        # print(newdeque.display())
        backward_word = ''.join(newdeque.display())
        if backward_word == word:
            pal_list.append(word)
    return max(pal_list, key=len)







print(is_palindrome(scrabble.wordlist))
