import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

# TODO: process results

for clue in results:
    # text = clue[0]
    # answer = clue[1]
    # value = clue[2]

    text, answer, value = clue #more idiomatic. Called 'tuple unpacking'

    #[$200]
    #Question: asdfghjkl
    #Answer: What is 'asdfghjkl'?

    print("[$%s]"%(value,))
    print("Question: %s" % (text,))
    print("Answer:  What is '%s'?" % (answer,))
    print("")


connection.close()
