#log2 N
import random 

def binary_search(list, key):
   low = 0   
   high = len(list) 
   steps = 0

   while low <= high:
      mid = (low + high) // 2
      if list[mid] == key:
         print('Interações ' + str(steps))
         return mid
      elif key > list[mid]:
         low = mid + 1
      else:
         high = mid - 1
      steps += 1

   return None

tam = int(input('Tamanho da lista: '))
my_list = list(range(tam))   

key = int(input('Número para encontrar:'))
pos  = binary_search(my_list, key)

if pos != None:
   print('Seu número está na posição ' + str(pos))
