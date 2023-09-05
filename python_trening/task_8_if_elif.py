num = 3

if num >= 0:
    print ('Число больше либо равно 0')
else:
    print ('Число меньше 0')

num = -3

if num >= 0:
    print ('Число больше либо равно 0')
else:
    print ('Число меньше 0')

num = 0

if num >= 0:
    print ('Число больше либо равно 0')
else:
    print ('Число меньше 0')

str1 = 'cat'
str2 = 'catt'

if str1 in str2:
    print ('YES')
else:
    print ('NO')

num_float = 3.14

if num_float > 0:
    print ('Число положительное')
elif num_float == 0:
    print ('Число равно 0')
else:
    print ('Число отрицательное')

num = 4
permit_print = True

if num > 0 and permit_print:
    print ('num - положительное число')
elif not permit_print:
    print ('Печать запрещена')

year = 5

if year > 0 and year < 5:
    print ('Бакалавр')
elif year >= 5 and year < 7:
    print ('Магистр')
elif year >= 7 and year < 10:
    print ('Аспирант')
else:
    print ('Введите корректный год обучения')

number = 55
if number not in range (-100, 101):
    print('-')
else:
    print('+')

