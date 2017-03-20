[This script](https://github.com/BMariscal/intermediate_python/blob/master/wordplay/longest_palindrome_bestest.py) finds
the longest palindrome in the English language(or at least the longest English word in the sowpods.txt file) by using the scrabble wordlist found in scrabble.py(data to make wordlist comes from sowpods.txt).Using a list comprehension, each word in wordlist is reversed and if the reversed word matches the unreversed word, the word is added to a new list. After the list is completed, it's then sorted by length and the last word(the longest word) is selected.

