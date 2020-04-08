import getch

def carregaArquivoLista(caminhoDoArquivo):

   countries = open(caminhoDoArquivo, 'r')
   countries_list = []
   print(countries_list)
   
   countries.close()
   return countries_list   

def listaPaises(countries_list):
   print('Escolha uma letra: ')
   letter = getch.getch()
   print('\n')
   print (f'Paises com a letra {letter}\n:')

   for country in countries_list:
      if country[0] == letter:
         print(country)

def rodadaJogo(countries_list, points, answers_list):
   
   answer = []
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
#    participante = input('Nome: ')
#    f.write(participante + ',' + points + '\n')
#    for line in f:

print ('----Jogo dos paises----\n O jogo consiste em você escrever o maior número de paises diferentes EM INGLES')
print('Você ganha um ponto para cada pais lembrado')

answers_list = []
points = 0
jogo = True

countries_list = carregaArquivoLista('Notas/countries.txt')

print(countries_list)
while(jogo == True):
   jogo = rodadaJogo(countries_list, points, answers_list)
   if jogo:
      points += 1
      print(f'\nBoa moleque!\nPontos: {points}')
   
   else:
      print('\nPerdeu!')

print('Fim de Jogo!')

print('Salve sua classificação:')