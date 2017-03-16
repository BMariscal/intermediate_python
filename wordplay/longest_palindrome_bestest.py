#find the longest palindrome using list comprehension
import time
import scrabble
start = time.time()
print((sorted([word for word in scrabble.wordlist if word == word[::-1]], key=len))[-1])

stop = time.time()
print("time elapsed: %.1f seconds"%(stop-start))

#list comprehension goes as follows:
#list=[]
# for word in scrabble.wordlist:
#      if word == word[::-1]:
#            list.append(word)
# sorted(list, key=len) <---sort the list by length, from smallest to largest
#print(the last word in the sorted list, which would be the longest palindrone in the whole list)
