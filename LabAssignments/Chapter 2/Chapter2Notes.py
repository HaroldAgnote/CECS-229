from plotting import plot

#Procedure computes the sum of two vectors
def addVectors(v, w):
	return [v[i] + w[i] for i in range(len(v))]

#Procedure multiplies the vector v by the scalar a
def scalar_vector_mult(a, v):
	return [a*v[i] for i in range(len(v))]


L = [[2, 2], [3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1]]

plot(L,4)

v = [3, 2]


plot([scalar_vector_mult(i/10, v) for i in range(11)], 5)
plot([scalar_vector_mult(i/100, v) for i in range(101)], 5)