import sqlite3

connection = sqlite3.connect("jeopardy.db")
# print (type(connection))

cursor = connection.cursor()

cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()

# print(results)
# print(results[0])
# print(results[0][0])
# print(results[1][0])
print("Example categories:\n")
for category in results: #for tuple in this list
    print(category[0])

connection.close()



