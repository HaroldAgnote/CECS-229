from vec import Vec
from mat import Mat

C = {'A','B','C'}   # Columns
R = {'A','B'}       # Rows
m = Mat((R,C), {('A','A'):1,('A','B'):2,('A','C'):3,('B','A'):10,('B','B'):20,('B','C'):30})

print(m)
print(m.transpose())