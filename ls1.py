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

 
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]  
# total = 0
# grade_Counter = 0

# for grade in grades:
#    total+=grade
#    grade_Counter += 1

# #Blaks lines are recommended above and below each control statement
# average = total/grade_Counter
# print(f'Class average is {average}')

# total = 0
# grade_counter = 0

# grade = int(input('Enter grade, -1 to end: '))

# while grade != -1:
#    total += grade
#    grade_counter += 1
#    grade = int(input('Enter grade, -1 to end: '))
 

# if grade_counter != 0:
#    average = total / grade_counter
#    print(f'Class average is {average:.2f}')
# else:
#    print('No grades')

#Range in deapth
# for number in range(5):
#    print(number, end=' ')
# print('\n')

# for number in range(5, 10):
#    print(number, end=' ')
# print('\n')

# for number in range(0, 10, 1):
#    print(number, end=' ')
# print('\n')

#Decimal
# amount = 112.12

# print(f'{amount:.20f}')

# #Exemplo: juros compostos
# #a = p(1 + r)**n
# from decimal import Decimal 

# principal = Decimal('100.00')
# rate = Decimal('3.65')

# for year in range(1, 11):
#    amount = principal * (1 + rate) ** year 
#    print(f'{year:>2} {amount:<10.2f}')


# #Mean, median and mode
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 82, 94]  

# sum(grades)/len(grades)

# import statistics

# print(f'{statistics.mean(grades):.3f} {statistics.median(grades)} {statistics.mode(grades)}')

# #Para simplificar: import statistics as stats
#Por segurança: from math import ceil, floor as mth







