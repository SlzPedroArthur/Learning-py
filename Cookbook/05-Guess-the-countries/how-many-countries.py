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

def fileToDictcionary(file):
   scores = {}
   with open(file, mode = 'r') as file:
      for line in file:
         user, score = line.strip().split(',')
         scores[int(user)] = score.lower().strip()
   return scores
         
def writeMyScore(name, points, file):
   with open(file, mode = 'r') as myFile:
      data = myFile.read()
   with open(file, mode ='w') as myFile:
      myFile.write(data)
      myFile.write('\n' + str(points) + ',' + name)


#def sortDictionary(dict):
   

def displayLearderBoard(file):
   scores = fileToDictcionary(file)
   leaderBoard = sorted(scores, reverse = True)

   print(f'{"==>LEADERBOARD<==":>20}')
   for i in range(5):
      print(f'{scores[leaderBoard[i]].upper():<10} {leaderBoard[i]:>10}pts')

      
print ('===>Jogo dos paises<===\n O jogo consiste em você escrever o maior número de paises diferentes EM INGLES. Você ganha um ponto para cada pais lembrado.')

answers_list = []
points = 0
jogo = True

countries_list = carregaArquivoLista('countries.txt')

while(jogo == True):
   jogo = rodadaJogo(countries_list, points, answers_list)
   if jogo:
      points += 1
      print(f'\nBoa moleque!\nPontos: {points}')
   
   else:
      print(f'\nFim de Jogo! Você fez {points} pontos')


nome = input('Salve sua classificação.\nInsira seu nome: ')
writeMyScore(nome, points, 'scores.txt')


displayLearderBoard('scores.txt')
