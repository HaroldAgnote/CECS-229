from mat import Mat
from vec import Vec

A = Mat(({0, 1, 2}, {0, 1, 2}), {(0,0):1, (1,1):1})
print(A)
B = A.transpose()
print(B)

print(A*B)
print(B*A)
print(2*A)