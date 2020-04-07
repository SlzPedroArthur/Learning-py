capital_dic={
    'Acre': 'Rio Branco',
    'Alagoas': 'Marceió',
    'Amapá':'Macapá',
    'Amazonas':'Manaus',
    'Bahia': 'Salvador',
    'Ceará':'Fortaleza',
    'Distrito Federal':'Brasília',
    'Espírito Santo':'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Bel´m',
    'Pernanbuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte' : 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Santa Catarina',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantis': 'Palmas'
}


import random

capital_list = list(capital_dic.keys())

op = 0
op = input('\nPressione 1 para jogar: ')

while op != 0:
   
   estado = random.choice(capital_list)
   respostaCorreta = capital_dic[estado]
      
   repostaUsuario = input('Qual a capital do estado de ' + estado + '?\n')

   if repostaUsuario == respostaCorreta:
      print('\nBoa moleque!')
   else:
      print('\nNão foi dessa vez :(')
   
   op = input('\nPressione 1 para jogar novamente: ')

print('DONE!')