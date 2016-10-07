from plotting import plot
from vec import Vec
from vecutil import zero_vec

#Procedure multiplies the vector v by the scalar a
def scalar_vector_mult(a, v):
	return [a*v[i] for i in range(len(v))]

#Procedure computes the sum of two vectors
def addVectors(v, w):
	return [v[i] + w[i] for i in range(len(v))]

#2.14.8a
pt1 = [-1.5, 2]
pt2 = [3, 0]

plot([addVectors(scalar_vector_mult(i/100, pt2), pt1) for i in range(101)], 4)



#2.14.8b

pt1 = [2,1]
pt2 = [-2,2]

plot([addVectors(scalar_vector_mult(i/100, pt2), pt1) for i in range(101)], 4)



#Backward Substitution Procedure
def triangular_solve(rowlist, label_list, b):
	D = rowlist[0].D
	x = zero_vec(D)
	for j in reversed(range(len(D))):
		c = label_list[j]
		row = rowlist[j]
		x[c] = (b[j] - x*row)/row[c]
	return x

label_list = ['a', 'b', 'c', 'd']
D = set(label_list)
rowlist = [Vec(D,{'a':1, 'b': 0.5, 'c': -2, 'd': 4}), Vec(D,{'b':3, 'c':3, 'd':2}), Vec(D,{'c': 1, 'd': 5}), Vec(D,{'d': 2})]
b = [-8, 3, -4, 6]

print(str(triangular_solve(rowlist, label_list, b)))
