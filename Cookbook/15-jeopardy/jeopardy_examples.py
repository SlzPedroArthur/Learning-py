import sqlite3

c = sqlite3.connect("jeopardy.db")
cursor = c.cursor()

cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()

print("Example categories:\n")
for category in results:
   print(category[0])

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

for clue in results:
   question, answer, value = clue
   print('[$%s]' % (value,))
   print('Question: %s' % (question,))
   print('Answer: What is %s ?' % (answer,))
   print('')
   


c.close()