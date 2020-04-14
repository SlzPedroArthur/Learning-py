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

# def fileToDictcionary(file):
#       question_dict = {}
#       for line in file:   
#          entry = line.strip().split(',')
#          question = entry[0]
#          answer = entry[1]
#          question_dict[question] = answer
#          return question_dict

# def writeMyScore(points):
#    file = open('Cookbook/05-Guess-the-countries/scores.txt', 'w')
#    participante = input('\nNome: ')
#    question_dict = fileToDictcionary(file)
   
   
   

# def displayScore(scoreList, position):
#    print('')
   

print ('----Jogo dos paises----\n O jogo consiste em você escrever o maior número de paises diferentes EM INGLES')
print('Você ganha um ponto para cada pais lembrado.')

answers_list = []
points = 0
jogo = True

countries_list = carregaArquivoLista('Cookbook/05-Guess-the-countries/countries.txt')

while(jogo == True):
   jogo = rodadaJogo(countries_list, points, answers_list)
   if jogo:
      points += 1
      print(f'\nBoa moleque!\nPontos: {points}')
   
   else:
      print(f'\nFim de Jogo! Você fez {points}')


print('Salve sua classificação:')

# writeMyScore(points)