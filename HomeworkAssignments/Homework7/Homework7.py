# Harold Agnote
# Harvey Han
# Ivan Kim
# Professor Tyler Nguyen
# CECS 229 - Sec. 01
# 11/17/2016
# Homework #7

# Problem #6.7.6

from mat import Mat
from matutil import mat2coldict
from matutil import mat2rowdict
from matutil import listlist2mat
from vecutil import list2vec
from independence import rank
from independence import is_independent
from GF2 import one

def my_is_independent(L):
    return rank(L) == len(L)

L = [[2,4,0], [8,16,4], [0,0,7]]
M = [[2,4,0], [8,16,4]]
N = [[1,3,0,0],[2,1,1,0],[0,0,1,0],[1,1,4,-1]]
O = [[one, 0, one, 0],[0, one, 0, 0], [one, one, one, one], [one, 0, 0, one]]
print(listlist2mat(L))
print("Matrix is Independent: ")
print(my_is_independent([list2vec(v) for v in L]))
print(listlist2mat(M))
print("Matrix is Independent: ")
print(my_is_independent([list2vec(v) for v in M]))
print(listlist2mat(N))
print("Matrix is Independent: ")
print(my_is_independent([list2vec(v) for v in N]))
print(listlist2mat(O))
print("Matrix is Independent: ")
print(my_is_independent([list2vec(v) for v in O]))

# Problem #6.7.7
def my_rank(L):
    rank = len(L)

    rank -= 1
    while rank > 0:
        temp = L.copy()
        for x in range(0, len(L)):
            temp.remove(temp[x])
            if (is_independent(temp)):
                return rank
            temp = L.copy()
        rank -= 1

    if (is_independent(L)):
        return rank
    return rank


P = [[1,2,3],[4,5,6],[1.1,1.1,1.1]]
Q = [[1,3,0,0],[2,0,5,1],[0,0,1,0],[0,0,7,-1]]
R = [[one, 0, one, 0],[0, one, 0, 0], [one, one, one, one], [0,0,0,one]]

print(listlist2mat(P))
print("Rank: ")
print(my_rank([list2vec(v) for v in P]))
print(listlist2mat(Q))
print("Rank: ")
print(my_rank([list2vec(v) for v in Q]))
print(listlist2mat(R))
print("Rank: ")
print(my_rank([list2vec(v) for v in R]))

# Problem #6.7.12
def is_invertible(M):
    numCol = len(M.D[1])
    # print(numCol)
    # print(rank(list((mat2coldict(M)).values())))
    # print(rank(list((mat2rowdict(M)).values())))
    colRank = rank(list((mat2coldict(M)).values()))
    rowRank = rank(list((mat2rowdict(M)).values()))

    if (numCol - colRank) == 0:
        return True
    elif (numCol - rowRank) == 0:
        return True
    else:
        return False

A = [[1,2,3],[3,1,1]]
B = [[1,0,1,0],[0,2,1,0],[0,0,3,1],[0,0,0,4]]
C = [[1,0],[0,1],[2,1]]
D = [[1,0],[0,1]]
E = [[1,0,1],[0,1,1],[1,1,0]]
F = [[one,0,one],[0,one,one],[one,one,0]]
G = [[one, one],[0,one]]
print(listlist2mat(A))
print("Matrix is invertible: ")
print(is_invertible(listlist2mat(A)))
print(listlist2mat(B))
print("Matrix is invertible: ")
print(is_invertible(listlist2mat(B)))
print(listlist2mat(C))
print("Matrix is invertible: ")
print(is_invertible(listlist2mat(C)))
print(listlist2mat(D))
print("Matrix is invertible: ")
print(is_invertible(listlist2mat(D)))
print(listlist2mat(E))
print("Matrix is invertible: ")
print(is_invertible(listlist2mat(E)))
print(listlist2mat(F))
print("Matrix is invertible: ")
print(is_invertible(listlist2mat(F)))
print(listlist2mat(G))
print("Matrix is invertible: ")
print(is_invertible(listlist2mat(G)))
