from vec import Vec
from mat import Mat
from matutil import *

# Harold Agnote
# Harvey Han
# Ivan Kim
#
# Professor Tyler Nguyen
# CECS 229 - Sec. 01
# 10/27/2016
# Homework #6 Problems

# Problem 4.17.13

def lin_comb_mat_vec_mult(M, v):
    assert M.D[1] == v.D
    result = Vec(M.D[0], { })
    for y in M.D[0]:
        for x in v.D:
            result[y] += M[y, x] * v[x]
    return result

N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
print(N1)
u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
print(u1)
print(lin_comb_mat_vec_mult(N1, u1))

# Problem 4.17.14

def lin_comb_vec_mat_mult(v, M):
    assert M.D[0] == v.D
    result = Vec(M.D[1], { })
    for x in v.D:
        for y in M.D[1]:
            result[y] += v[x] * M[x, y]
    return result

v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
print(v1)
M1 = Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
print(M1)
print(lin_comb_vec_mat_mult(v1, M1))
print(lin_comb_vec_mat_mult(v1, M1) == Vec({'a', 'b', 'c'},{'a': -8, 'b': 2, 'c': 0}))
print(v1 == Vec({1, 2, 3}, {1: 1, 2: 8}))
print(M1 == Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7}))

# Problem 4.17.15

def dot_product_mat_vec_mult(M,v):
    assert M.D[1] == v.D
    result = Vec(M.D[0], {})
    for x in M.D[0]:
        m = Vec(M.D[1], {})
        for y in v.D:
            m[y] = M[x,y]
        for y in v.D:
            result[x] = m*v
    return result



N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
print(N1)
u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
print(u1)
print(dot_product_mat_vec_mult(N1, u1))



# Problem 4.17.16
def dot_product_vec_mat_mult(M,v):
    assert M.D[0] == v.D
    result = Vec(M.D[1], { })
    for x in M.D[1]:
        m = Vec(M.D[0], { })
        for y in M.D[0]:
            m[y] = M[y, x]
        for y in M.D[0]:
            result[x] = v * m

    return result


v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
print(v1)
M1 = Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
print(M1)
print(dot_product_vec_mat_mult(M1, v1))
print(dot_product_vec_mat_mult(M1, v1) == Vec({'a', 'b', 'c'},{'a': -8, 'b': 2, 'c': 0}))
print(v1 == Vec({1, 2, 3}, {1: 1, 2: 8}))
print(M1 == Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7}))

# Problem 4.17.17
def Mv_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    result = dict()
    b = mat2coldict(B)
    for x in b.keys():
        result.update( {x: A*b.get(x)})

    return coldict2mat(result)



C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
print(C)
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(D)
print(C*D)
print(C*D == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5}))

C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
print(C)
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(D)
print(Mv_mat_mat_mult(C,D))

# Problem 4.17.18
def vM_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    result = dict()
    a = mat2rowdict(A)
    for x in a.keys():
        result.update({x:a.get(x)*B})

    return rowdict2mat(result)

C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
print(C)
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(D)
print(C*D)
print(C*D == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5}))

C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
print(C)
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(D)
print(vM_mat_mat_mult(C,D))

# Problem 4.17.20

def dictlist_helper(dlist, k):
    return [x.get(k) for x in dlist]

dlist = [{'a':'apple', 'b':'bear'}, {'a': 1, 'b':2}]
k = 'a'

print(dictlist_helper(dlist, k))