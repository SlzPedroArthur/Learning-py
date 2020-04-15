#Backtraking CS

grid = [
   [5,3,0,0,7,0,0,0,0],
   [6,0,0,1,9,5,0,0,0],
   [0,9,8,0,0,0,0,6,0],
   [8,0,0,0,6,0,0,0,3],
   [4,0,0,8,0,3,0,0,1],
   [7,0,0,0,2,0,0,0,6],
   [0,6,0,0,0,0,2,8,0],
   [0,0,0,4,1,9,0,0,5],
   [0,0,0,0,8,0,0,7,9]
]

def possible(x, y, n):
   global grid

   j = 0
   for i in range(9):
      if grid[i][j] == n:
         return False
      for j in range(9):
         if grid[x][y] == n:
            return False
   x0 = (x // 3) * 3
   y0 = (y // 3) * 3

   for x0 in range(3):
      for y0 in range(3):
         if grid[x0][y0] == n:
            return False
   return True

print(possible(4, 4, 5))