print "1."
print (673 + 909)//3 == 0

print "2."
print {2**x for x in {0, 1, 2, 3, 4}}

print "3."
print {x*y for x in {4, 5, 6} for y in {7, 8, 9}}

print "4."
A = ['A', 'B', 'C']
B = [1, 2, 3]
print [x + ", " + str(y) for x in A for y in B]
S = {-4, -2, 1, 2, 5, 0}

print "5."
print "a."
print [(i, j, k) for i in S for j in S for k in S if (i + j + k) == 0]
print "b."
print [(i, j, k) for i in S for j in S for k in S if ((i + j + k) == 0) and (((i != 0) or (j != 0)) or (k != 0))]
print "c."
print [(i, j, k) for i in S for j in S for k in S if (i + j + k) == 0 and (i == 0 and j == 2 and k == -2)]
print [(i, j, k) for i in S for j in S for k in S if ((i + j + k) == 0) and (((i != 0) or (j != 0)) or (k != 0))][0]

