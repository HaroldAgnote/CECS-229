print("1")
L = ['A', 'B', 'C', 'D', 'E']
print(list(zip((range(len(L))), L)))


print("\n2")
dlist = [{'James':'Sean','director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce','director':'Roger'}]
k = 'James'

A = list(i[k] for i in dlist)

print(A)


print("\n3")
names = ['Larry','Curly','Moe']
id2salary = {0:1000.0, 2:990, 1:1200.50}

B = {names[k]:id2salary.get(k) for k in id2salary.keys()}

print(B)