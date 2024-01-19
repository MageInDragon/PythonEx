
print('Ex9.1')

a = int(input('Введите число: '))

def findSum(a):
    if(a==0):
        return 1
    return findSum(a//10) + a%10

print(findSum(a))

print()
print('Ex9.2')
    
a = int(input('Введите число: ')) 

def prost(a,b):
    if(a<2):
        return 0
    elif (a == 2):
        return 1
    elif (a % b == 0):
        return 0
    elif (b < a /2):
        return prost(a,b+1)
    else:
        return 1

if(prost(a,2)):
    print('YES')
else:
    print('NO')
