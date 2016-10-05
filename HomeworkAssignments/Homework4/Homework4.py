from plotting import plot

#2.14.8a
pt1 = [-1.5, 2]
pt2 = [3, 0]

#Procedure multiplies the vector v by the scalar a
def scalar_vector_mult(a, v):
	return [a*v[i] for i in range(len(v))]

#Procedure computes the sum of two vectors
def addVectors(v, w):
	return [v[i] + w[i] for i in range(len(v))]



#2.14.8b

pt1 = [2,1]
pt2 = [-2,2]

plot([addVectors(scalar_vector_mult(i/100, pt2), pt1) for i in range(101)], 4)