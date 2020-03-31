"""Conceitos básico da linguagem Python"""








#Mínimo de Três valores
# n1 = int(input('Insira três números: '));
# n2 = int(input());
# n3 = int(input());

# minimum = n1
# if n2 < n1:
#    minimum = n2;
# if n3 < n1:
#    minimum = n3;
# print('Menor:', minimum) 

# #Lists and interators
# for numbers in [2, -3, 0, 17]:
#    print(numbers)

# for counter in range(10):
#    print(counter, end=' ')

 
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]  
total = 0
grade_Counter = 0

for grade in grades:
   total+=grade
   grade_Counter += 1

#Blaks lines are recommended above and below each control statement
average = total/grade_Counter
print('Class average is ', average)


