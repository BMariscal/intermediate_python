import scrabble

longest = ''
for word in scrabble.wordlist:
    new_word = word[::-1]
    if new_word == word:
        if len(word) > len(longest):
            longest = word

print(longest)


