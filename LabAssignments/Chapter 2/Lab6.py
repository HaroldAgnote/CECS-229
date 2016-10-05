from vec import Vec

D = {'x','y','z'}
u = Vec(D, {'x':1,'y':1})
v = Vec(D, {'x':1,'y':2,'z':3})
w = Vec(D, {'x':0,'y':0})

print(u)
print(v)
print(w)

def vec_select(L,s):
	result = list()
	for y in L:
		if y.__getitem__(s) == 0:
			result.append(y)

	return result



print(vec_select([u,v,w],'x'))
print("\n\n")
print(vec_select([u,v,w],'y'))
print("\n\n")
print(vec_select([u,v,w],'z'))
print("\n\n")



def vec_sum(L, D):
	result = Vec(D,{})
	for x in D:
		sum = 0
		for y in L:
			sum += Vec.__getitem__(y, x)
			Vec.__setitem__(result, x, sum)

	return result


v = vec_sum([u,v,w],D)

print(v)