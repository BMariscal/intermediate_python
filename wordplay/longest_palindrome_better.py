import scrabble
import time


start = time.time()
longest =""

for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
            is_palindrome = False
    if is_palindrome and len(word) > len(longest):
        longest = word

print(longest)

# too slow: second slowest
stop = time.time()
print("time elapsed: %.1f seconds"%(stop-start))
