#list = linear, O(n)
#dict = constant, O(1), independent of size of dictionary

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]#extracts words from file and adds them to list called my_words
word_list =[elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_dict = dict((elt, 1) for elt in word_list) # set to one because the quantity is irrelevant
print(word_dict)

print(len([word for word in my_words if word not in word_dict]),'total new words')
