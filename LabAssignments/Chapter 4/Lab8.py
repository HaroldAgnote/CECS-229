from vec import Vec
from mat import Mat
from math import sin
from math import cos
from math import pi

def identityMatrix(labels):
    assert isinstance(labels, set)

    identity = Mat((labels, labels), { })
    for x in identity.D[0]:
        for y in identity.D[1]:
            if x == y:
                identity[x, y] = 1
            else:
                identity[x, y] = 0
    return identity

print("\nIdentity Matrices")
C = {'1', '2'}
D = {'a','b','c'}
E = {'1','2','c','d'}

one = identityMatrix(C)
two = identityMatrix(D)
three = identityMatrix(E)

print(one)
print(two)
print(three)

def translationMatrix(a, b):
    R = {'A', 'B', 'C'}
    result = Mat((R, R), {})
    for x in result.D[0]:
        for y in result.D[1]:
           if x == y:
               result[x,y] = 1
           elif x == 'A' and y == 'C':
               result[x,y] = a
           elif x == 'B' and y == 'C':
               result[x,y] = b
    return result

print("Translate a Matrix")

v = Vec({'A','B','C'}, {'A': 3, 'B':2, 'C':1})
print("Vector v")
print(v)
print("\nTranslate by (a,b) where a = 2, and b = 3")
print(translationMatrix('a','b'))
print(translationMatrix(2,3))
print("\nResult:")
print(translationMatrix(2,3)*v)

def scaleMatrix(a, b):
    R = { 'A', 'B', 'C' }
    result = Mat((R, R), {})
    for x in result.D[0]:
        for y in result.D[1]:
            if x == y and x == 'A':
                result[x,y] = a
            elif x==y and x == 'B':
                result[x,y] = b
            elif x==y and x == 'C':
                result[x,y] = 1
    return result

print("\nScale a Matrix")
print("Vector v")
print(v)
print("\nScale by (a, b) where a = 2, and b = 4")
print(scaleMatrix('a','b'))
print(scaleMatrix(2,4))
print("\nResult:")
print(scaleMatrix(2,4)*v)

def rotationMatrix(theta):
    R = {'A','B','C'}
    result = Mat((R,R), {})
    result['A', 'A'] = int(cos(theta))
    result['A', 'B'] = -int(sin(theta))
    result['B', 'A'] = int(sin(theta))
    result['B', 'B'] = int(cos(theta))
    result['C', 'C'] = 1

    return result

print("\nRotation Matrix")
print("Vector v")
v = Vec({'A', 'B', 'C'}, {'A': 2, 'B':4, 'C':1})
print(v)
print("\nRotate by 90 degrees (pi/2)")
print(rotationMatrix(pi/2))
print("\nResult:")
print(rotationMatrix(pi/2)*v)

def y_reflectMatrix():
    R = {'A', 'B', 'C'}
    result = Mat((R,R), {})
    result['A', 'A'] = -1
    result['B', 'B'] = 1
    result['C', 'C'] = 1
    return result

print("\nReflection")
print("Vector y")
y = Vec({'A','B', 'C'},{'A': 1, 'B': 1, 'C':1})
print(y)
print("\nReflection about the y-axis")
print(y_reflectMatrix())
print("\nResult")
print(y_reflectMatrix()*y)

def x_reflectMatrix():
    R = { 'A', 'B', 'C' }
    result = Mat((R, R), {})
    result['A', 'A'] = 1
    result['B', 'B'] = -1
    result['C', 'C'] = 1
    return result

print("\nReflection")
print("Vector x")
x = Vec({'A','B', 'C'},{'A': 1, 'B': 1, 'C':1})
print(x)
print("\nReflection about the x-axis")
print(x_reflectMatrix())
print("\nResult")
print(x_reflectMatrix()*x)
