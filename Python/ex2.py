import math

x=float(input('Введите x: '))
y=float(input('Введите y: '))
z=float(input('Введите z: '))

s = math.pow(math.fabs(math.cos(x) - math.cos(y)),(1+2*math.pow(math.sin(y),2)))*(1 + z + (math.pow(z,2)/2) + (math.pow(z,3)/3) + (math.pow(z,4)/4))

print("S = ",s)
