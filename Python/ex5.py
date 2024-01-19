s = str(input('Ввевдите строку: '))
count = int(0)
news = str('')
for i in range(len(s)):
    if s[i] == 'а':
        news += 'о'
        count += 1
    else:
        news += s[i]
print('Оригинальная строка: ', s)
print('Измененная строка: ', news)
print('Количество замен: ',count)
