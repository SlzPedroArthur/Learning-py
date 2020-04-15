import sys 
import Scrabble

if __name__ == "__main__":
  #Se o número de argumentos for menor que 2
  if len(sys.argv) < 2:
    print('Use: cheater.py [LETRAS]')
    sys.exit(1)

  letrasUsuario = list(sys.argv[1].lower())
  palavrasValidas = []

  for palavra in Scrabble.wordlist:
    
    letrasDisponiveis = letrasUsuario[:]
    deuMatch = True

    for letra in palavra.lower():
      if letra not in letrasDisponiveis:
        deuMatch = False
        break
      letrasDisponiveis.remove(letra)

    if deuMatch:
      pontos = 0
      for letra in palavra:
        pontos = pontos + Scrabble.pontos[letra]
      palavrasValidas.append((pontos, palavra))
  
  for jogada in sorted(palavrasValidas):
    print("%d %s" % (jogada[0], jogada[1]))
