from plotting import plot
from math import pi

S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

R = set((2 + 1j) + z for z in S)
plot(S, 5)
plot(R, 5)