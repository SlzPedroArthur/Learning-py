# #Lists

# c = [-45, 6, 3.4223, 'Smith', 123]

# len(c)

# s = 'Hello' #String imutável

# for number in range(1, 6):
#    a_list += [number]

# print(a_list)

# #Concatenando
# lista1 = [10, 20, 30]

# lista2 = [40, 50]

# cat_listas = lista1 + lista2

# print(cat_listas)

# for i in range(len(cat_listas)):
#    print(f'{i}: {cat_listas[i]}')

# a = [1, 2, 3]

# b = [1, 2, 3]

# c = [1, 2, 3, 4]

# a == b
# a == c
# a < c
# c >= b

# #Tuplas

# student_tuple = 'John', 'Green', 3.3

# print(student_tuple[2] * 3600, student_tuple[0])

# tupla1 = (10, 20, 30)
# tupla2 = tupla1

# tupla1 += (20, 20)

# print(tupla1, tupla2)

# numbers = [1, 2, 3, 4, 5]

# numbers += (6, 7)

# student_tuple = ('Amanda', [98, 61, 49])

# first_name, grade = student_tuple

# first, second = 'hi'

# number1 = 99
# number2 = 22

# number1, number2 = (number2, number1)

# #enumerate

# colors = ['red', 'orange', 'green']

# #Cria uma lista de uma sequencia
# list(enumerate(colors))

# #Cria uma tupla de uma sequencia
# tuple(enumerate(colors))

# # Criando bar chart

# numbers = [19, 3, 15, 7, 11]

# print('\nCriando um gráfico de barras: ')
# print (f'Index{"Value":>7}  Barra')

# for index, value in enumerate(numbers):
#    print(f'{index:>5}{value:>6}   {"*" * value}')

# #sclicing

# numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# numbers[2:6]

# numbers[:6]

# numbers[6:len(numbers)]

# # Though slices create new objects, slices make shallow copies of the elements—that is, they copy the elements’ references but not the objects they point to.

# #cria uma nova lista em ordem reversa
# print (numbers[::-1])

# numbers[0:3] = [111, 111, 111]

# print(numbers)

# numbers[::2] = [100, 100, 100, 100]

# numbers[:] = []
# #note, acima estamos deletando o conteudo de numbers. Para add a numbers uma lista vazia devemos fazer:
# numbers = []


# #Del statement
# numbers = list(range(0,   10))

# del numbers[-1]
# print(numbers)

# del numbers[0:2]
# print(numbers)

# del numbers[::2]
# print(numbers)

# del numbers[:]
# print(numbers)

# del numbers
# #print(numbers)

# #Sorting 
# numbers = list(range(0,   10))

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)

# ascending_numbers = sorted(numbers)

# letters = 'asdkflqwekr'

# ascending_letters = sorted(letters)

# print(ascending_letters,ascending_numbers)

# #Searching sequences

# ##index: retorna o indice do primeiro elemento que encontrar
# numbers = [2, 3, 4, 5, 3, 22, 7, 5]
# print (numbers.index(5)) 

# numbers *=2 #concatenando a lista nela mesma
# print(numbers)

# print (numbers.index(5, 7)) #busca '5' a partir do oitavo elemento

# numbers.index(3, 0, 4) #busca '3' no intervalo entre o primeiro e o quinto elemento

# #Automaticamente verifica a presença de um elemento na sequencia
# print (1000 in numbers)
# print (22 in numbers)
# print (1000 not in numbers)

# #Podemos usar o operador in para evitar erros
# key = 22
# if key in numbers:
#    print(f'Found {key} at index {numbers.index(key)}')
# else:
#    print(f'{key} not found')

#Outras funções uteis
##insert
color_names = ['orange', 'yellow', 'green']

color_names.insert(0, 'red') #insere sem remover qualquer elemento

color_names.append('gray') #concatena






