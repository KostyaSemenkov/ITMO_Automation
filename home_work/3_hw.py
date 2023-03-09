def two_numbers(first_num, second_num):
    return print(max(first_num, second_num))
two_numbers(3, 5)


def number135(num1, num2):
    if max(num1, num2) - min(num1,num2) == 135:
        return print('yes')
    else:
        return print('No')
number135(135, 0)


def seasons(season):
    if season in [1, 2, 12]:
        return print('зима')
    elif season in range(3,6):
        return print('весна')
    elif season in range(6,9):
        return print('лето')
    elif season in [9, 10, 11]:
        return print('осень')
    else:
        return print('')
seasons(11)


def numbers(first_num, second_num, third_num):
    if first_num > 10 and second_num > 10 and third_num >10:
        return print('yes')
    else:
        return print('no')
numbers(1, 2, 10)


def list_positive(list_p):
    count = 0
    for i in range(5):
        if list_p[i] > 0:
            count += 1
    print(count)
list_positive([1, -1, 2 ,-2, 3])


def days(a: int, b: int):
    return print(a*12*29 + b*29)
days(1, 2)