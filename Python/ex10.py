#1. Дана прямоугольная матрица. Найти строку с наибольшей и строку с 
#наименьшей суммой элементов. Вывести на печать найденные строки и 
#суммы их элементов.
#2. Дана квадратная матрица A[N, N], Записать на место отрицательных 
#элементов матрицы нули, а на место положительных — единицы. 
#Вывести на печать нижнюю треугольную матрицу в общепринятом виде.

print('ex8.1')

with open('Bezlepkin_Konstantin_Vitalyevich_Ym232_vvod81.txt','r') as infile:
    m = int(infile.readline())
    n = int(infile.readline())
    a=[]
    for line in infile:
        b = []
        for i in line.split():
            b.append(int(i))
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

with open('Bezlepkin_Konstantin_Vitalyevich_Ym232_vivod81.txt','w') as outfile:
    outfile.write('Максимальная сумма чисел в строке массива (' + str(maxid) + '): ' + str(maxS) + '\n')
    outfile.write('Минимальная сумма чисел в строке массива (' + str(minid) + '): ' + str(minS))

print()
print('ex8.2')

with open('Bezlepkin_Konstantin_Vitalyevich_Ym232_vvod82.txt','r') as infile:
    m = int(infile.readline())
    n = int(infile.readline())
    a=[]
    for line in infile:
        b = []
        for i in line.split():
            b.append(int(i))
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

with open('Bezlepkin_Konstantin_Vitalyevich_Ym232_vivod82.txt','w') as outfile:            
    outfile.write('Нижний треугольник измененого массива: \n')
    for i in range(n):
        for j in range(n):
            if(i>0 and j < i):
                outfile.write(str(a[i][j]) + ' ')
        outfile.write('\n')


            

