import getch

def carregaArquivoLista(caminhoDoArquivo):

   countries = open(caminhoDoArquivo, 'r')
   countries_list = []
   for line in countries:
      line = line.strip()
      countries_list.append(line)

   countries.close()
   return countries_list   

def rodadaJogo(countries_list, points, answers_list):
   
   op = 'n'

   while op != 'y':
      answer = input('\n Resposta: ')

      print('\nSua resposta é \'' + answer + '\' deseja confirmá-la? (y/n)')
      op = getch.getch()

   if answer in answers_list:
      print('\nJá colocou esse, espertão!')
      return True

   if answer in countries_list:
      answers_list.append(answer)
      return True
   else:
      return False


# def writeMyScore(points):
#    f = open('scores.txt', 'w')
#    participante = input('\nNome: ')
#    f.write('\n' + points + ',' + participante)
   
   

# def displayScore(scoreList, position):
#    print('')
   

print ('----Jogo dos paises----\n O jogo consiste em você escrever o maior número de paises diferentes EM INGLES')
print('Você ganha um ponto para cada pais lembrado.')

answers_list = []
points = 0
jogo = True

countries_list = carregaArquivoLista('Cookbook/Guess-the-countries/countries.txt')

while(jogo == True):
   jogo = rodadaJogo(countries_list, points, answers_list)
   if jogo:
      points += 1
      print(f'\nBoa moleque!\nPontos: {points}')
   
   else:
      print('\nPerdeu!')

print('Fim de Jogo!')

print('Salve sua classificação:')