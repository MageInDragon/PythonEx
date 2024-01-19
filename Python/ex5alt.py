s = str(input('Ввевдите строку: '))
count = int(0)
for i in range(len(s)):
    if s[i] == 'а':
        count += 1
print('Оригинальная строка: ',s) 
print('Измененная строка: ',s.replace('а','о'))
print('Количество замен: ', count)
