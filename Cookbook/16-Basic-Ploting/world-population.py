from matplotlib import pyplot 

data = open('world-population.txt', 'r' ).readlines()
years = []
populations = []
for point in data:
   year, population = point.split()
   years.append(year)
   populations.append(population)

pyplot.plot(years, populations, 'o-')
pyplot.xlabel('Populacao mundial')
pyplot.ylabel('Anos')
pyplot.title('Demograia mundial\nEm milhões')
pyplot.show()


