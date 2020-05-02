from matplotlib import pyplot

data = open('life-expectancies-usa.txt','r').readlines()

dates = []
male_life_expentancies = []
female_life_expentancies = []

for line in data:
   date, male_life_expentancy, female_life_expentancy = line.split(',')
   dates.append(date)
   male_life_expentancies.append(male_life_expentancy)
   female_life_expentancies.append(female_life_expentancy)

pyplot.plot(dates, male_life_expentancies, 'bo-', label = 'Homens')
pyplot.plot(dates, female_life_expentancies, 'mo-', label = 'Mulheres')

pyplot.legend(loc = 'upper left')
pyplot.ylabel('Idade')
pyplot.xlabel('Anos')
pyplot.title('Expectative de vida nos EUA')

pyplot.show()