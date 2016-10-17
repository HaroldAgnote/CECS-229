from vec import Vec
from mat import Mat

# Print and Accessor Test
print("Print and Accessor Test")
M = Mat(({'a', 'b'}, {'@', '#', '?'}), {('a', '@'): 1, ('a', '#'):2, ('a','?'): 3, ('b', '@'): 10, ('b', '#'): 20, ('b', '?'):30 })
N = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
print("M\n" + str(M))
print("N\n" + str(N))

print("N[1, 'a'] is " + str(N[1,'a']))
print("N[3,'a'] is " + str(N[3,'a']))
print("\n")

# Equality Test
print("Equality Test")
print("Mat(({'a','b'}, {'A','B'}), {('a','B'):0}) == Mat(({'a','b'}, {'A','B'}), {('b','B'):0}) is " + str(Mat(({'a','b'}, {'A','B'}), {('a','B'):0}) == Mat(({'a','b'}, {'A','B'}), {('b','B'):0})))

A = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1})
B = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1, ('b','B'):0})
C = Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1, ('b','B'):5})
print("A\n" + str(A))
print("B\n" + str(B))
print("C\n" + str(C))
print("A == B is " + str(A == B))
print("B == A is " + str(B == A))
print("A == C is " + str(A == C))
print("C == A is " + str(C == A))
print("A == Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1}) is " + str(A == Mat(({'a','b'}, {'A','B'}), {('a','B'):2, ('b','A'):1})))
print("\n")

# Mutator Test
M = Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):7})
print("M" + str(M))
print("M['b', 5] = 9")
M['b', 5] = 9
print("M['c', 5] = 13")
M['c', 5] = 13
print("M" + str(M))
print("M == Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):9, ('c',5):13}) is " + str(M == Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):9, ('c',5):13})))
N = Mat(({((),), 7}, {True, False}), {})
print("N\n" + str(N))
print("N[(7, False)] = 1")
N[(7, False)] = 1
print("N[(((),), True)] = 2")
N[(((),), True)] = 2
print("N\n" + str(N))
print("N == Mat(({((),), 7}, {True, False}), {(7,False):1, (((),), True):2}) is " + str(N == Mat(({((),), 7}, {True, False}), {(7,False):1, (((),), True):2})))
print("\n")

# Addition Test
A1 = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})
print("A1\n" + str(A1))
A2 = Mat(({3, 6}, {'x','y'}), {(3,'y'):4})
print("A2\n" + str(A2))
B = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (3,'y'):4, (6,'y'):3})
print("B\n" + str(B))
print("A1 + A2\n" + str(A1 + A2))
print("A1 + A2 == B is " + str(A1 + A2 == B))

print("A2 + A1 == B is " + str(A2 + A1 == B))

print("A1 unchanged? " + str(A1 == Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})))

zero = Mat(({3,6}, {'x','y'}), {})
print("zero\n" + str(zero))
print("B + zero\n" + str(B + zero))
print("B + zero == B is " + str(B + zero == B))

C1 = Mat(({1,3}, {2,4}), {(1,2):2, (3,4):3})
print(C1)
C2 = Mat(({1,3}, {2,4}), {(1,4):1, (1,2):4})
print(C2)
D = Mat(({1,3}, {2,4}), {(1,2):6, (1,4):1, (3,4):3})
print(D)
print(C1 + C2 == D)
print("\n")

# Scalar Mult Test
M = Mat(({1,3,5}, {2,4}), {(1,2):4, (5,4):2, (3,4):3})
print(M)
print(0*M == Mat(({1, 3, 5}, {2, 4}), {}))

print(1*M == M)
N = Mat(({1,3,5}, {2,4}), {(1,2):1.0, (5,4):0.5, (3,4):0.75})
print(N)
print(0.25*M == N)
print("\n")

# Transpose Test
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

# Vector Matrix Multiplication
v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
print(v1)
M1 = Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
print(M1)
print(v1*M1)
print(v1*M1 == Vec({'a', 'b', 'c'},{'a': -8, 'b': 2, 'c': 0}))
print(v1 == Vec({1, 2, 3}, {1: 1, 2: 8}))
print(M1 == Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7}))

v2 = Vec({'a','b'}, {})
print(v2)
M2 = Mat(({'a','b'}, {0, 2, 4, 6, 7}), {})
print(M2)
print(v2*M2)
print(v2*M2 == Vec({0, 2, 4, 6, 7},{}))

v3 = Vec({'a','b'},{'a':1,'b':1})
print(v3)
M3 = Mat(({'a', 'b'}, {0, 1}), {('a', 1): 1, ('b', 1): 1, ('a', 0): 1, ('b', 0): 1})
print(M3)
print(v3*M3)
print(v3*M3 == Vec({0, 1},{0: 2, 1: 2}))

# Matrix Vector Multiplication
N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
print(N1)
u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
print(u1)
print(N1*u1)
print(N1*u1 == Vec({1, 3, 5, 7},{1: 3, 3: 9, 5: -2, 7: 3}))

print(N1 == Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1}))

print(u1 == Vec({'a', 'b'}, {'a': 1, 'b': 2}))

N2 = Mat(({('a', 'b'), ('c', 'd')}, {1, 2, 3, 5, 8}), {})
print(N2)
u2 = Vec({1, 2, 3, 5, 8}, {})
print(u2)
print(N2*u2)
print(N2*u2 == Vec({('a', 'b'), ('c', 'd')},{}))

M3 = Mat(({0,1},{'a','b'}),{(0,'a'):1, (0,'b'):1, (1,'a'):1, (1,'b'):1})
print(M3)
v3 = Vec({'a','b'},{'a':1,'b':1})
print(v3)
print(M3*v3)
print(M3*v3 == Vec({0, 1},{0: 2, 1: 2}))

# Matrix Matrix Multiplication
A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
print(A)
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(B)
print(A*B)
print(A*B == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31}))

C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
print(C)
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(D)
print(C*D)
print(C*D == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5}))

M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
print(M)
N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
print(N)
print(M*N)
print(M*N == Mat(({0,1}, {(1,1), (2,2)}), {}))

E = Mat(({'a','b'},{'A','B'}), {('a','A'):1,('a','B'):2,('b','A'):3,('b','B'):4})
print(E)
F = Mat(({'A','B'},{'c','d'}),{('A','d'):5})
print(F)
print(E*F)
print(E*F == Mat(({'a', 'b'}, {'d', 'c'}), {('b', 'd'): 15, ('a', 'd'): 5}))

print(F.transpose())
print(E.transpose())
print(F.transpose()*E.transpose())
print(F.transpose()*E.transpose() == Mat(({'d', 'c'}, {'a', 'b'}), {('d', 'b'): 15, ('d', 'a'): 5}))