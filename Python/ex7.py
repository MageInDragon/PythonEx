#1. Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить 
#программу деления дроби на дробь. Ответ должен быть несократимой дробью. 
#Использовать подпрограмму алгоритма Евклида для определения НОД.
#2. Задана окружность (x-a)2 + (y-b)2 = R2 и точки Р(р1, р2), F(f1, f1), L(l1,l2). 
#Выяснить и вывести на экран, сколько точек лежит внутри окружности. 
#Проверку, лежит ли точка внутри окружности, оформить в виде процедуры.

#1.

print('Ex7.1')

A = int(input('Введите число A (A/B): ')) #4
B = int(input('Введите число B (A/B): ')) #7
C = int(input('Введите число C (C/D): ')) #8
D = int(input('Введите число D (C/D): ')) #21


def findNOD(a,b):
    if(a < b):
        NOD = int(a)
    else:
        NOD = int(b)
        b = a
    while(b%NOD != 0):
        tmp = int(NOD)
        NOD = b%NOD
        b = tmp
    return NOD

delimoe = A*D/findNOD(A*D,B*C)
delitel = B*C/findNOD(A*D,B*C)
print('(',A,'/',B,') / (',C,'/',D,') = ', delimoe, '/', delitel) 


print('')
print('Ex7.2')

a = int(input('Введите точку a: '))
b = int(input('Введите точку b: '))
R = int(input('Введите радиус окружности: '))

P = [int(input('Введите координаты точки P: ')),int(input())]
F = [int(input('Введите координаты точки F: ')),int(input())]
L = [int(input('Введите координаты точки L: ')),int(input())]

def include(x,y):
    if((x-a)**2 + (y-b)**2 <= R**2):
        return 1
    else:
        return 0
    
included = int(0)
print('Точки, лежащие внутри окружности: ')
for i in [P,F,L]:
    if(include(i[0],i[1])):
        included += 1
        print(i[0],',',i[1])

print('Точек, лежащих внутри окружности: ',included)

