f = open('Notas/Files/countries.txt', 'r')

#Imprimindo arquivo
for line in f:
   line = line.strip()
   print(line)

#Criando uma lista para o conteudo do arquivo
countries_list = []
for line in f:
   countries_list.append(line)

f.close()
#Imprimindo os paises com a letra 'T'
for country in countries_list:
   if country[0] == "T":
      print(country)

#Escrevendo em arquivos
file = open('Notas/Files/scores.txt', 'w')

while True:
   participant = input('\nParticipante: ')

   if participant == 'quit':
      print('Saindo...')
      break

   score = input('Pontos de ' + participant + ':' )

   file.write(participant + ',' + score + '\n')

file.close()

#Salvando arquivo num dicionário
f = open('scores.txt', 'r')

participants = {}

for line in f:
   entry = (line.strip().split(','))
   participant = entry[0]
   score = entry[1]
   participants[participants] = score

f.close()

