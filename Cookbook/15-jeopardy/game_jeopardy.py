import sqlite3

c = sqlite3.connect('jeopardy.db')
cursor = c.cursor()

cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")
result = cursor.fetchall()
game_id = result[0][0]

print('Cagories for game #%d' % (game_id))

query = """SELECT name, round FROM category
WHERE game = %d ORDER BY round""" % (game_id,)
cursor.execute(query)
results = cursor.fetchall()

for result in results:
   name, round = result
   print('Round %d: %s' % (round, name))

c.close()