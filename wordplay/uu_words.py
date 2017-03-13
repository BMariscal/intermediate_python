import scrabble

#print all words containing "uu"
count = 0
for item in scrabble.wordlist:
    if "uu" in item:
        print(item)
        count+=1
print(str(count) , "words have 'uu'")
