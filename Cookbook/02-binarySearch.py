"""
Uma abordagem muito comum para buscas lineares é o algoritmo de busca binária. Sua complexidade é de O(log n) em listas ordenadas, ou seja, em listas com muitos valores é melhor utilizar a busca binária.
"""
import random

"""Busca binária"""
def binarySearch(inputList, key):
   first = 0
   last = len(inputList) - 1
   sts = False
   
   while(first <= last and sts == False):
      mid = (first + last) // 2
      
      if inputList[mid] == key:
         sts = True
      elif key < inputList[mid]:
         last = mid - 1
      else: first = mid + 1
   return sts

"""Aplicação"""

#Criando lista com valores 'aleatórios'
numbers = list(range(100))

numbers.sort()
print(numbers)

#Recebendo entrada do usuário
key = int(input('Selecione um número: '))

result = binarySearch(numbers, key)

if result: print('Found!')
else: print('Not Found!')

