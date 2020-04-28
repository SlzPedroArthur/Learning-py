import sqlite3

c = sqlite3.connect('jeopardy.db')
cursor = c.cursor()

def queryGame():
   cursor.execute('SELECT game FROM category ORDER BY RANDOM() LIMIT 1')
   result = cursor.fetchall()
   game_id = result[0][0]
   
   cursor.execute('SELECT name FROM category WHERE game = %d' % (game_id,))
   result = cursor.fetchall()
   name = result[0][0]

   query = 'SELECT text, answer, value FROM clue WHERE game = %d' % (game_id,)
   cursor.execute(query)
   result = cursor.fetchall()
   
   return (game_id, name, result)
   
game_id, name, result = queryGame()

print('======>Joepardy GAME<=====')
print('Primeira pergunta!')

for game_round in result:
   text, answer, value = game_round
   print('Pergunta: %s' % (text,))
   print(answer)
   
   op = 'n'
   while op == 'n':
      user_answer = str(input('Sua resposta: '))
      op = str(input("Tem certeza que '%s' é a resposta? (y/n)"))

   if user_answer == answer:
      print('Certa resposta!')
      continue
   else:
      print('PERDEU!')
      break

print(text)   

c.close()
