import random

class Greeter(object):
   def __init__(self, name):
      self.name = name
   def hello(self):

      print('Hei ' + self.name + '! :)')

   def goodbye(self):
      print('Bye bye!')

#Criando uma instância   
g = Greeter('Anna')

g.hello()
g.goodbye()

#Deck of Cards class
class Deck(object):
   def shuffle(self):
      naipes = ['Espada', 'Copa', 'Ouro','Paus']
      valores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
      
      #Permite que 'cartas' seja exposta pelo resto da classe
      self.cartas = []
      
      for naipe in naipes:
         for valor in valores:
            self.cartas.append(valor + ' de ' + naipe)

      random.shuffle(self.cartas)
   
   def deal(self):
      return self.cartas.pop()

d = Deck()
d.shuffle()
print(d.deal())   