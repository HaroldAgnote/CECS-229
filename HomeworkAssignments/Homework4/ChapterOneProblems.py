#1.7.1
def my_filter(L, num):
    return list(x for x in L if x % num != 0)

L = [1,2,4,5,7]
num = 2
print(my_filter(L, num))

#1.7.2
def myLists(L):
    A = list(list(range(x)) for x in L)
   # B = list(y + 1 for y in list(list(x for x in list(A))))

    return A

L = [1,2,4]
print(myLists(L))
L = [0]
print(myLists(L))


#1.7.3
'''
def my_function_composition(f, g):


f = {0:'a', 1:'b'}
g = {'a': 'apple', 'b': 'banana'}

print(my_function_composition(f,g))
'''

#1.7.4
def mySum(L):
    current = 0
    for x in L:
        current = current + x
    return current

L = [1, 2, 3, 4, 5]
print(mySum(L))


#1.7.5
def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return current

print(myProduct(L))

#1.7.6
def myMin(L):
    current = L[0]
    for x in L:
        if x < current:
            current = x
    return current

L = [44, 234, 5435, 2234, 554, 2342, 1, 345, 13495]
print(myMin(L))

#1.7.7
def myConcat(L):
    current = ''
    for x in L:
        current += x
    return current

T = ['Hello',',','my',' name ', ' is ', ' John.']
print(myConcat(T))

#1.7.8
def myUnion(L):
    current = set()
    for x in L:
        current = current | set(x)

    return current

D = [{1}, {1, 2}, {1, 2, 3}, {4, 5, 6}, {7, 8}, {9}]

print(myUnion(D))