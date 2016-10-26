from vec import Vec
from mat import Mat

# Problem 4.17.13

def lin_comb_mat_vec_mult(M, v):
    assert M.D[1] == v.D
    result = Vec(M.D[0], { })
    for y in M.D[0]:
        for x in v.D:
            result[y] += M[y, x] * v[x]
    return result

# Problem 4.17.14

def lin_comb_vec_mat_mult(v, M):
    assert M.D[0] == v.D
    result = Vec(M.D[1], { })
    for x in v.D:
        for y in M.D[1]:
            result[y] += v[x] * M[x, y]
    return result

# Problem 4.17.15

def dot_product_mat_vec_mult(M,v):


# Problem 4.17.16
def dot_product_vec_mat_mult(M,v):
    return 'hi'

# Problem 4.17.17
def Mv_mat_mat_mult(A, B):
    return 'hi'

# Problem 4.17.18
def vM_mat_mat_mult(A, B):
    return 'hi'

# Problem 4.17.20

def dictlist_helper(dlist, k):
    return [x.get(k) for x in dlist]

dlist = [{'a':'apple', 'b':'bear'}, {'a': 1, 'b':2}]
k = 'a'

print(dictlist_helper(dlist, k))