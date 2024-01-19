#1. Дана прямоугольная матрица. Найти строку с наибольшей и строку с 
#наименьшей суммой элементов. Вывести на печать найденные строки и 
#суммы их элементов.
#2. Дана квадратная матрица A[N, N], Записать на место отрицательных 
#элементов матрицы нули, а на место положительных — единицы. 
#Вывести на печать нижнюю треугольную матрицу в общепринятом виде.

print('ex8.1')

m=int(input('Введите количество строк: '))
n=int(input('Введите количество столбцов: '))
a=[]
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент: ')
        b.append(int(input()))
    a.append(b)

print('Исходный массив')
for i in range(m):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()

minS = int(0)
maxS = int(0)
for j in range(n):
        minS += a[0][j]
        maxS += a[0][j]
minid = int(0)
maxid = int(0)

for i in range(m):
    S = int(0)
    for j in range(n):
        S += a[i][j]
    if(S > maxS):
        maxS = S
        maxid = i
    if(S < minS):
        minS = S
        minid = i

print('Максимальная сумма чисел в строке массива (',maxid,'): ',maxS)
print('Минимальная сумма чисел в строке массива (',minid,'): ',minS)

print()
print('ex8.1')

n=int(input('Введите размер матрицы: '))
a=[]
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент: ')
        b.append(int(input()))
    a.append(b)

print('Исходный массив')
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
    
for i in range(n):
    for j in range(n):
        if(a[i][j] <= 0):
            a[i][j] = 0
        else:
            a[i][j] = 1

print('Нижний треугольник измененого массива')
for i in range(n):
    for j in range(n):
        if(i>0 and j < i):
            print(a[i][j], end = ' ')
    print()

            
