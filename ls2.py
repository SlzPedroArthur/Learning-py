
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

#Craps
import random

def roll_dices():
   die1 = random.randrange(1, 7)
   die2 = random.randrange(1, 7)
   return (die1 + die2)

def display_dices(dice):
   die1, die2 = dice
   print(f'Pontos do jogador {die1} + {die2} = {sum(dice)}\n')

def first_round(game_status):
   die_values = roll_dices()
   display_dices(die_values)

   sum_dices = sum(die_values)

   if sum_dices in (7, 11):
      game_status = 'VENCEU'
   elif sum_dices in (2, 3, 12):
      game_status = 'PERDEU'
   else:
      game_status = 'CONTINUE'
      my_points =  sum_dices
      
   return my_points

def other_rounds(my_points):
   die_values = roll_dices()
   display_dice(die_values)

   sum_dices = sum(die_values)

   if sum_dices == my_points:
      game_status = 'VENCEU'
   elif sum_dices == 7:
      game_status = 'PERDEU'

option = int(input('Pressione 1 para jogar e 0 para sair'))
game_status = 'CONTINUE'

while(option != 0 and game_status == 'CONTINUE'):
   first_round(game_status);

   

