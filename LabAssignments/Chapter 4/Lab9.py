from vec import Vec
from mat import Mat
from math import pi
from math import sin
from math import cos

D = {'x','y','z'}

def translationMatrix(a, b):
    result = Mat((D, D), {})
    for x in result.D[0]:
        for y in result.D[1]:
           if x == y:
               result[x,y] = 1
           elif x == 'x' and y == 'z':
               result[x,y] = a
           elif x == 'y' and y == 'z':
               result[x,y] = b
    return result

def rotationMatrix(theta):
    result = Mat((D,D), {})
    result['x', 'x'] = (cos(theta))
    result['x', 'y'] = -(sin(theta))
    result['y', 'x'] = (sin(theta))
    result['y', 'y'] = (cos(theta))
    result['z', 'z'] = 1

    return result


def pointAngleMatrix(a, b, t):
    origin = Vec(D, {'x': 0, 'y': 0, 'z': 1})
    return translationMatrix(a,b)*rotationMatrix(t)*translationMatrix(-a,-b)


print(Vec(D, {'x':2, 'y':2, 'z':1}))

print(pointAngleMatrix(3,3,pi/2)*Vec(D, {'x': 2, 'y': 2, 'z': 1}))

print(pointAngleMatrix(3,3,pi/4)*Vec(D, {'x': 2, 'y': 2, 'z': 1}))