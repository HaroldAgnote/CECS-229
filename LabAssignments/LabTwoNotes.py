range(10)
list(range(10))
list(reversed(range(10)))
list(range(0,10,2))
S = [1, 2, 3]
T = [4, 5, 6]
list(zip(S,T))
{3:"Bob", 4:"Bill"}
{3:"Bob", 4:"Bill"}[3]
S = {k:v for (k, v) in [(3,2),(4,0),(100,1)]}
S[3]
S[4]
S.keys()
S.values()
chars = ["A", "B", "C"]
values = ["a", "b", "c"]
print(list(zip(chars,values)))
print(set(zip(chars,values)))

print ({k:v for (k,v) in [(x,x**2) for x in range(100)]})