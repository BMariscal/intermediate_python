import scrabble
import time


start = time.time()
longest = ''
for word in scrabble.wordlist:
    new_word = word[::-1]
    if new_word == word:
        if len(word) > len(longest):
            longest = word

print(longest)


stop = time.time()
print("time elapsed: %.1f seconds"%(stop-start))
