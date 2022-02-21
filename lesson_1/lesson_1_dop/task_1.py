"""
 1. Cоздать функцию которая принимает число и возвращает  текст как в примере:
   3275  —>  "3000 + 200 + 70 +5"
"""


def return_text():
    current_number = (input('Insert number:'))
    len_current_number = len(current_number) - 1
    result = []

    for index, val in enumerate(current_number):
        if int(val):
            result.append(val + '0' * (len_current_number - index))
    return ' + '.join(result)


print(return_text())
