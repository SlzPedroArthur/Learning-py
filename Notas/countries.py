import getch

countries = open('Notas/countries.txt', 'r')
countries_list = []

for line in countries:
   line = line.strip()
   countries_list.append(line)
   
countries.close()

print('Escolha uma letra: ')
letter = getch.getch()
print('\n')
print (f'Paises com a letra {letter}\n:')


for country in countries_list:
   if country[0] == letter:
      print(country)

