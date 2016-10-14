from vec import Vec
from mat import Mat

#Print and Accessor Test
M = Mat(({'a', 'b'}, {'@', '#', '?'}), {('a', '@'): 1, ('a', '#'):2, ('a','?'): 3, ('b', '@'): 10, ('b', '#'): 20, ('b', '?'):30 })
N = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
print(M)
print(N)

print(N[1,'a'])
print(N[3,'a'])
print("\n")

#Equality Test
print(Mat(({'a','b'}, {'A','B'}), {('a','B'):0}) == Mat(({'a','b'}, {'A','B'}), {('b','B'):0}))

A = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1})
B = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1, ('b','B'):0})
C = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1, ('b','B'):5})
print(A)
print(B)
print(C)
print(A == B)
print(B == A)
print(A == C)
print(C == A)
print(A == Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1}))
print("\n")

#Mutator Test
M = Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):7})
print(M)
M['b', 5] = 9
M['c', 5] = 13
print(M)
print(M == Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):9, ('c',5):13}))
N = Mat(({((),), 7}, {True, False}), {})
print(N)
N[(7, False)] = 1
N[(((),), True)] = 2
print(N)
print(N == Mat(({((),), 7}, {True, False}), {(7,False):1, (((),), True):2}))
print("\n")

#Addition Test
A1 = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})
print(A1)
A2 = Mat(({3, 6}, {'x','y'}), {(3,'y'):4})
print(A2)
B = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (3,'y'):4, (6,'y'):3})
print(B)
print(A1 + A2 == B)

print(A2 + A1 == B)

print(A1 == Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3}))

zero = Mat(({3,6}, {'x','y'}), {})
print(zero)
print(B + zero == B)

C1 = Mat(({1,3}, {2,4}), {(1,2):2, (3,4):3})
print(C1)
C2 = Mat(({1,3}, {2,4}), {(1,4):1, (1,2):4})
print(C2)
D = Mat(({1,3}, {2,4}), {(1,2):6, (1,4):1, (3,4):3})
print(D)
print(C1 + C2 == D)
print("\n")

#Scalar Mult Test
M = Mat(({1,3,5}, {2,4}), {(1,2):4, (5,4):2, (3,4):3})
print(M)
print(0*M == Mat(({1, 3, 5}, {2, 4}), {}))

print(1*M == M)
N = Mat(({1,3,5}, {2,4}), {(1,2):1.0, (5,4):0.5, (3,4):0.75})
print(N)
print(0.25*M == N)
print("\n")

#Transpose Test
M = Mat(({0,1}, {0,1}), {(0,1):3, (1,0):2, (1,1):4})
print(M)
print(M.transpose())
print(M.transpose() == Mat(({0,1}, {0,1}), {(0,1):2, (1,0):3, (1,1):4}))

M = Mat(({'x','y','z'}, {2,4}), {('x',4):3, ('x',2):2, ('y',4):4, ('z',4):5})
print(M)
Mt = Mat(({2,4}, {'x','y','z'}), {(4,'x'):3, (2,'x'):2, (4,'y'):4, (4,'z'):5})
print(M.transpose())
print(Mt)
print(M.transpose() == Mt)
print("\n")