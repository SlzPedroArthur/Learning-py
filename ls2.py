
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

def roll_dice():
   return random.randrange(1, 7)

print("Pressione") 


"""specifying a custom funcion docstring"""