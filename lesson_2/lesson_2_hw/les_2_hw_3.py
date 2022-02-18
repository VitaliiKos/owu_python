"""
3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
Пример:
expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""

current_number = input('Insert number:')


def expanded_form(number: str) -> str:
    divisor = len(number) - 1
    result = []
    for i in current_number:
        if i != '0':
            result.append(i + (divisor * '0'))
        divisor -= 1
    return ' + '.join(result)


print('---------- Task 1 -----------------')
print(expanded_form(current_number))
print('-----------------------------------')
