#list = linear, O(n)
#dict = constant, O(1), independent of size of dictionary

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]#extracts words from file and adds them to list called my_words
word_list =[elt.strip() for elt in open("sowpods.txt", "r").readlines()]

# dict vs set
word_dict = dict((elt, 1) for elt in word_list) # set to one because the quantity is irrelevant

word_set = set(word_list) # It's better to use a set for this. Given that we only care about the items present, not the key value relationships(frequency in which an item occurs)

print(word_set)
print(len([word for word in my_words if word not in word_set]),'total new words')
