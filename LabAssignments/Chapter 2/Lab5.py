from plotting import plot

#1a
def addVectorsAndScale(a, v, w):
	x = list(((v[i] + w[i]) for i in range(len(v))))
	y = list(a*x[i] for i in range(len(v)))

	return y

v = [1,2,3]
w = [1,0,-1]
a = 2

print(addVectorsAndScale(a,v,w))

#1b
def computeDotProduct(v, w):
	sum = 0
	for x in range((len(v))):
		sum += v[x]*w[x]
	return sum

def computeDotProductLine(v,w):
	return sum(v[i]*w[i] for i in range(len(v)))

print(computeDotProductLine(v,w))


#2

pt1 = [3.5, 3]
pt2 = [.5, 1]

#Procedure multiplies the vector v by the scalar a
def scalar_vector_mult(a, v):
	return [a*v[i] for i in range(len(v))]

#Procedure computes the sum of two vectors
def addVectors(v, w):
	return [v[i] + w[i] for i in range(len(v))]


#plot([scalar_vector_mult(i/100, v) for i in range(101)], 5)

plot([addVectors(scalar_vector_mult(i/100, pt1), pt2) for i in range(101)], 4)