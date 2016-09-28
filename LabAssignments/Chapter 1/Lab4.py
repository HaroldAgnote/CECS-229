from plotting import plot
from math import e
from math import pi
from image import file2image as f2i

#1
S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
T = {(e**(2*pi*1j/20))**x for x in range(20)}

def transform(a,b,L):
    return list(a*z+b for z in L)

O = transform(1, -2.5 - 1.5j, S)

U = transform(1.25, 0, T)

plot (set(O) | set(U))


#2
data = f2i("./img01.png")
pts = [(x+y*1j) for x in range (len(data)) for y in range(len(data[0])) if data[x][y][0] < 120]

I = {z*e**((3*pi/2)*1j) + 5 + 190j for z in pts}
plot(I,200)