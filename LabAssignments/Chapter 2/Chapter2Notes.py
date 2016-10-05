
'''
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
'''

from vec import Vec

v = Vec({'A','B','C'}, {'A':1})
w = Vec({'A','B','C'}, {'A':2, 'B':4})
for d in v.D:
	if d in v.f:
		print(v.f[d])


print(Vec.__getitem__(v, 'A'))

Vec.__setitem__(v, 'B', 2)

print(Vec.__getitem__(v, 'B'))

print("V\n")
print(v)
print("W\n")
print(w)
print("\n\nDotProduct of v and w\n")
print(Vec.__mul__(v,w))

print("Add v and w to create x\n")
x = Vec.__add__(v,w)

print(x)
print("Scale x by 2\n")
x = Vec.__rmul__(x,2)
print(x)
print("Add x and w\n")
print(Vec.__add__(x,w))

print("Negate x\n")
print(Vec.__neg__(x))

