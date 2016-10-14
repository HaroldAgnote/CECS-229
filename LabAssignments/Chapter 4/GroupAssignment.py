from vec import Vec
from mat import Mat

M = Mat(({'a', 'b'}, {'@', '#', '?'}), {('a', '@'): 1, ('a', '#'):2, ('a','?'): 3, ('b', '@'): 10, ('b', '#'): 20, ('b', '?'):30 })

print(M)