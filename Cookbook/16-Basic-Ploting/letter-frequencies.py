from matplotlib import pyplot
import string

data = open('constitution.txt', 'r').read()

letter_counts = {}
for char in string.ascii_lowercase:
   letter_counts[char] = 0

for char in data:
   char = char.lower()
   if char in string.ascii_lowercase:
      letter_counts[char] += 1

frequencies = letter_counts.items() #frequencies contains tuples. Doing it because dict don't guaratee order.
labels = []
counts = []
for letter, count in sorted(frequencies):
   labels.append(letter)
   counts.append(count)

xlocations = range(len(frequencies)) #xlocations is a list from 0 to the number of frequencies.
width = 0.5 #the width of each bar in the chart
pyplot.xticks([elem + width / 2 for elem in xlocations], labels) #calculate where along the x-axis the ticks for each bar should go. I want ticks to be in the center of bars
pyplot.bar(xlocations, counts, width = width)

pyplot.xlabel('Letra')
pyplot.ylabel('Frequency')
pyplot.title('Frequencia das letras na constuicão')
pyplot.show()