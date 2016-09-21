from math import e
from math import pi

from plotting import plot

S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

plot(S)

R = {z*e**((pi/4)*1j) for z in S}

plot(R)


def transform(a,b,L):
    return list(a*z+b for z in L)
    


n = 20
w = e**(2*1j*pi/n)



C = set(w**i for i in range(n))
B = set(1/2*z for z in C)
A = set(2*z for z in C)

plot(C|B|A)


