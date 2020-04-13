"""
Text.
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
      elif

"""Aplicação"""

#Criando lista com valores 'aleatórios'
numbers = list(range(100))
for i in range(100):
   numbers[i] = random.randrange(1,10000)

numbers.sort()
print(numbers)

#Recebendo entrada do usuário
key = int(input('Selecione um número: '))

result = binarySearch(numbers, len(numbers), key)

print(f'\nResultado: {numbers[result]}')

