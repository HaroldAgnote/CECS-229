#1
# Input List L of Integers
# Output List of Integers where ith element is 1 more than the i element of L

def number1(L): return [i+1 for i in L]

print(number1([1, 5, 7]))

#ex. input [1,5,6]
#   output [2,6,8]

#2 input: dct = {'a': 'A', 'b': 'B', 'c': 'C'}
#         keylist = ['b', 'c', 'a']
# output: ['B','C', 'A']

dct = {'a': 'A', 'b': 'B', 'c': 'C'}
keylist = ['b', 'c', 'a']

def number2(dct, key): return [dct[k] for k in key]

print(number2(dct,keylist))

#3

# input: L = ['A', 'B', 'C'] & keylist = ['a','b','c']
# output: {'a':'A', 'b':'B', 'c', 'C'}

L = ['A', 'B', 'C']
keylist = ['a','b','c']


def number3 (L, key): return {k:v for (k, v) in zip(key, L)}

print(number3(L, keylist))

s = "There is no spoon."

for i in range(len(s)):
        if s[i] == 'n':
            break
