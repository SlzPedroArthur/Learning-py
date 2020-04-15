import sys 
import Scrabble

if __name__ == '__main__': #Verifica se esse é a main????
    if len(sys.argv) < 2:
      print('Use: cheater.py [SUAS_LETRAS]')
      sys.exit(1)

    #Recebendo o argumento do usuário
    userLetters = list(sys.argv[1].lower())
    #Criando lista para salvar as palavras válidas
    validWords = []

    for word in Scrabble.wordlist:
      #Fazendo uma cópia das letras disponíveis para cada nova palavra. 
      # Assim, podemos manipular sem perder as lista original
      availableLetters = userLetters[:]
      status = True
      for letter in word.lower():
        if letter not in availableLetters:
          status = False
          break
        availableLetters.remove(letter)

      #Calcula os pontos para cada palavra
      if status:
        score = 0
        for letter in word:
          score = score + Scrabble.scores[letter]
        validWords.append((score, word))

    for play in sorted(validWords):
      print("%d %s" % (play[0], play[1]))    