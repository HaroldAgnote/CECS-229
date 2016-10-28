from vec import Vec
from mat import Mat
from matutil import *

C = {'A','B','C'}   # Columns
R = {'A','B'}       # Rows
m = Mat((R,C), {('A','A'):1,('A','B'):2,('A','C'):3,('B','A'):10,('B','B'):20,('B','C'):30})
v = Vec(C, {'A': 7, 'B': 0, 'C': 4})
v2 = Vec(R, {'A': 3, 'B': 4})

print(m)
print(v)
print(v2)

print(m*v)

print()
print(v2*m)


A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
print(A)
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(B)
print(A*B)
