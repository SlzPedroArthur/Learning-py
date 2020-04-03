
# #max and min
# max('yellow', 'red', 'orange', 'blue', 'green')

# min(15, 9, 27, 14)

# #Random 
# import random

# f1 = 0
# f2 = 0
# f3 = 0
# f4 = 0
# f5 = 0
# f6 = 0

# for roll in range(600_000):
#    face = random.randrange(1, 7)

#    if face == 1:
#       f1 += 1
#    elif face == 2:
#       f2 += 1
#    elif face == 3:
#       f3 += 1
#    elif face == 4:
#       f4 += 1
#    elif face == 5:
#       f5 += 1
#    elif face == 6:
#       f6 += 1   

# print(f'Face{"Frequency":>13}')
# print(f'{1:>4}{f1:>13}')
# print(f'{2:>4}{f2:>13}')
# print(f'{3:>4}{f3:>13}')
# print(f'{4:>4}{f4:>13}')
# print(f'{5:>4}{f5:>13}')
# print(f'{6:>4}{f6:>13}')


# #Random seed
# import random

# random.seed(32)

# for roll in range(10):
#       print(random.randrange(1, 7), end=' ')
# print('\n')

# for roll in range(10):
#    print(random.randrange(1, 7),end=' ')
# print('\n')

# random.seed(32)

# for roll in range(10):
#    print(random.randrange(1, 7), end=' ')
# print('\n')

# #Craps
# import random

# def roll_dices():
#    die1 = random.randrange(1, 7)
#    die2 = random.randrange(1, 7)
#    return (die1, die2)

# def display_dices(dice):
#    die1, die2 = dice
#    print(f'Pontos do jogador: {die1} + {die2} = {sum(dice)}\n')

# def first_round(game_status, my_points):
#    die_values = roll_dices()
#    display_dices(die_values)

#    sum_dices = sum(die_values)

#    if sum_dices in (7, 11):
#       game_status = 'VENCEU'
#    elif sum_dices in (2, 3, 12):
#       game_status = 'PERDEU'
#    else:
#       game_status = 'CONTINUE'
#       my_points =  sum_dices
      
#    return my_points

# def other_rounds(game_status, my_points):
#    die_values = roll_dices()
#    display_dices(die_values)

#    sum_dices = sum(die_values)

#    if sum_dices == my_points:
#       game_status = 'VENCEU'
#    elif sum_dices == 7:
#       game_status = 'PERDEU'
#    return game_status
   

# option = int(input('Pressione 1 para jogar e 0 para sair\n'))
# my_points = 0

# while(option != 0):
#    game_status = 'CONTINUE'
#    my_points = 0

#    my_points = first_round(game_status, my_points)
#    print(f'{game_status}\n')

#    while game_status == 'CONTINUE':
#       game_status = other_rounds(game_status, my_points)
        
   
#    if (game_status == 'VENCEU'):
#       print('Parabens! Você venceu!\n')
#    else:
#       print('Parabens! Você PERDEU!\n')

#    option = int(input('Deseja jogar novamente?\n'))


# #Default parameter value

# def rectangle_area(length = 2, width = 3):
#    return length * width

# print (f'{rectangle_area()} {rectangle_area(10)} {rectangle_area(1,4)}\n')

# #Arbitrary argument list

# def average(*args):
#    return sum(args) / len(args)

# print(f'{average(1, 4, 3, 3, 5, 3, 3):.3f}\n')

# grades = [88, 75, 96, 55, 83]
# print(f'{average(*grades):.3f}\n')

# #Métodos: uma função que podemos chamar num objeto
# #object_name.method_name(arguments)

# s = 'Hei!'

# s.lower()
# s.upper()
# print(s)

# #Scopes
# #Local scope: definida naquele bloco somente
# #Global scope: pode ser usada em qualquer função ou classe

# x = 21;

# def access_global():
#    print(f'Acessando x global: {x} \n') 

# access_global()

# def try_to_modify_global():
#    x = 3.333  #Py criou uma variavel local 
#    print(f'X de try_to_modify: {x}\n')

# try_to_modify_global()

# x = 44

# try_to_modify_global()

# access_global()

# def modify():
#    global x
#    x = 9999
#    print(f'{x}\n')

# modify()

# print(f'{x}\n')

#Observação: caso eu utilize o nome de uma built-in function (eg. sum) como nome de variável, não poderei mais usar a função.

# #Passando referencias
# x = 4
# print(f'\nId de x: {id(x)}')

# def cube(number):
#    print('\nid number before:', id(number))
#    number **= 3
#    print('\nid number after: ', id(number))

#    return number

# x = cube(x)

# print(f'\nId de x: {id(x)}\n')

# print(x)

# #Recursão
# #Indirect recursion
# def factorial(number):
#    if number != None and number > 0:
#       if number <= 1:
#          return 1
#       return number * factorial(number -1)

# input_number = int(input('\nInsira um número: '))
# print(f'\nFatorial de {input_number} é : {factorial(input_number)}')      


#Declarative proraming, immutability and interna interation

#Measures of dispersion
import statistics as sts
import math 

population = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print(sts.mean(population))
print('\n')
#Deviation: 
def mypVariance(population):
   pVariance = 0
   
   for i in range(0, len(population)):
      pVariance += pow(population[i] - sts.mean(population),2)
   
   pVariance = pVariance/len(population)

   return pVariance

print(sts.pvariance(population))
print('\n')

print(mypVariance(population))
print('\n')
 

#Calcula o desvio padrão da população
print(sts.pstdev(population))
print('\n')
#O desvio padrão é a raiz quadrada da variação, isso dimiui o efeito dos valores exremos. Quanto menor a variação e o desvio padrão, mais próximo os valores dos dados estão da média e menor a dispersão geral entre os valores e amédia.


