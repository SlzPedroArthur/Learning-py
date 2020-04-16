def hanoi(n, source, helper, target):
   if n == 1 :
      moves(source, target)
      return
   hanoi(n - 1, source, target, helper)
   moves(source, target)
   hanoi(n - 1, helper, source, target)


def moves(source, target):
   print('Move disco de {} para {}'.format(source, target))

hanoi(4, 'A', 'B', 'C')


