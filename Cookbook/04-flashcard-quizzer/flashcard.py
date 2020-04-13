#Da acesso aos comandos da linha de comando
import sys
import random


if len(sys.argv) < 2:
   print("Insira o arquivo flashcard: ")

flashcard_filename = sys.argv[1]
file = open(flashcard_filename, 'r')

question_dict = {}

for line in file:
   entry = line.strip().split(',')
   question = entry[0]
   answer = entry[1]
   question_dict[question] = answer

file.close()

print('Meu programa de FlashCards com Python!\n')
print('A qualquer momento escreva \'sair\' para sair\n')

questions = list(question_dict.keys())

while True:
   question = random.choice(questions)
   answer = question_dict[question]

   print('Pergunta: ' + question)
   user_input = input('Resposta: ')
   if user_input == 'sair':
      print('Até a próxima! ;)')
      break
   elif user_input == answer:
      print('Correcto!')
   else: 
      print('BAH! A resposta era: ' + answer)

