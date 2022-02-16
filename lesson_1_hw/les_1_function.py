#####################################################
# function
#####################################################
"""
    f1. створити функцію яка виводить ліст
    f2. створити функцію яка приймає три числа та виводить та повертає найменьше.
    f3. створити функцію яка приймає три числа та виводить та повертає найбільше.
    f4. створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
    f5. створити функцію яка виводить ліст
    f6. створити функцію яка повертає найбільше число з ліста
    f7. створити функцію яка повертає найменьше число з ліста
    f8. створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
    f9. створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
"""


def f1_return_list():
    print('Task f1:', [1, 2, 3, 4, 5, 6])
    print('-------------------------------')


def f2_func_min(a, b, c):
    result_f2 = []
    result_f2 += str(a) + str(b) + str(c)
    return min(result_f2)


def f3_func_max(a, b, c):
    result_f2 = []
    result_f2 += str(a) + str(b) + str(c)
    return max(result_f2)


def f4_func_min_max(*args):
    print('Task f4 max:', max(args))
    return min(args)


def f5_return_list():
    print('Task f5:', [1, 2, 3, 4, 5, 6])
    print('-------------------------------')


def f6_func_max_list():
    return max([9, 5, 7, 8, 2, 7, 8, 9, 6])


def f7_func_min_list():
    return min([9, 5, 7, 8, 2, 7, 8, 9, 6])


def f8_func_sum_list(sum_list):
    return sum(sum_list)


def f9_func_mean_list(sum_list):
    return sum(sum_list) / len(sum_list)


f1_return_list()
print('Task f2:', f2_func_min(9, 5, 7))
print('-------------------------------')
print('Task f3:', f3_func_max(9, 5, 7))
print('-------------------------------')
print('Task f4 min:', f4_func_min_max(9, 5, 7, 8, 2, 7, 8, 9, 6))
print('-------------------------------')
f5_return_list()
print('Task f6:', f6_func_max_list())
print('-------------------------------')
print('Task f7:', f7_func_min_list())
print('-------------------------------')
print('Task f8:', f8_func_sum_list([9, 5, 7, 8, 2, 7, 8, 9, 6]))
print('-------------------------------')
print('Task f9:', f9_func_mean_list([9, 5, 7, 8, 2, 7, 8, 9, 6]))
