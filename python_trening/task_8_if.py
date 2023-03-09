num = 3
if num >= 0:
    print('число больше либо равно нулю')
else:
    print('число отрицательное')


str1 = 'test'
str2 = 'test1'
if str1 in str2:
    print('Да')
else:
    print('Нет')


num_float = 3.4
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True


if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


a = 5
if a in range(1, 5):
    print('бакалавр')
elif a in range(5,7):
    print('магистр')
elif a in range(7,10):
    print('аспирант')
else:
    print('Введите корректный год обучения')
