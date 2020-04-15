import sys
import PalavrasCruzadas

#Salva as letras da mão numa lista e verifica letra por letra se ela pode ser formada
def valid_word(word, rack):
   available_letters = rack[:] #selecionando lista inteira

   for letter in word:
      if letter not in available_letters:
         return False
      
   return True

#Calcula os pontos para a palavra recebida
def compute_score(word):
   score = 0
   for letter in word:
      score = score + PalavrasCruzadas.scores[letter]
   return score

#Esse script recebe como argumento na linha de comando  as letras que você possui na sua mão durante o jogo
if len(sys.argv) < 2:
   print('Usage: scrabble.py [RACK]')
   sys.exit(1)

   #Salva as palavras disponíveis do usuário numa lista
   rack = list(sys.argv[1].lower())
   valid_words = []

   for word in PalavrasCruzadas.wordlist:
      if valid_word(word, rack): #se 'word' pode ser feito com 'rack'
         score = compute_score(word)
         valid_words.append([score, word]) #Guarda as palavras disponíveis numa lista
   
   valid_words.sort() #Temos a palavras com mais pontos primeiro
   for play in valid_words:
      score = play[0]
      word = play[1]
      print(word + ': ' + str(score))