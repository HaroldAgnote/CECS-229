# Homework 8
# Harold Agnote
# Harvey Han
# Ivan Kim
# Professor Tyler Nguyen
# CECS 229 - Sec. 01
# 12/15/2016

from mat import Mat
from matutil import *
from GF2 import *
from triangular import *

def is_echelon(A):
    currCol = 0
    columns = mat2coldict(A)
    # print("Columns: " + str(columns))
    for x in A.D[0]:
        if A[x, currCol] != 1:
            if A[x, currCol] == 0:
                currCol += 1
                print(len(A.D[1]))
                while currCol < len(A.D[1]):
                    if A[x, currCol] != 0 and A[x, currCol] != 1 :
                        return False
                    else:
                        for y in list(columns[currCol].f.values())[currCol + 1:]:
                            if y != 0:
                                return False
                        currCol += 1
            else:
                return False
        else:
            for y in list(columns[currCol].f.values())[currCol + 1:]:
                if y != 0:
                    return False
        currCol += 1
    return True

L = listlist2mat([[1,1,3], [0,0,1]])
print(L)
print("Is L echelon: " + str(is_echelon(L)) )

L = listlist2mat([[1,1,3], [0,0,2]])
print(L)
print("Is L echelon: " + str(is_echelon(L)) )

L = listlist2mat([[1,2,3], [0,1,2]])
print(L)
print("Is L echelon: " + str(is_echelon(L)) )

L = listlist2mat([[1,0,1,2],[0,1,1,1],[0,0,0,1]])
print(L)
print("Is L echelon: " + str(is_echelon(L)) )


def echelon_solve(row_list, label_list, b):
    for x in row_list:
        deleteRow = True
        for y in list(row_list[x].f.values()):
            if y != 0:
                deleteRow = False
        if deleteRow:
            row_list.pop(x)
            b.pop(x)
            x -= 1

    print(row_list)
    print(label_list)
    print(b)

    return triangular_solve(row_list, sorted(list(label_list)), b)

L = listlist2mat([[one, 0, one, one, 0],[0,one,0,0,one],[0,0,one,0,one],[0,0,0,0,one]])

print(L)
print(echelon_solve(mat2rowdict(L), L.D[1], [one, 0, one, one]))