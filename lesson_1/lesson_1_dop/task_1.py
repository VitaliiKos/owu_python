#########################################
# 1. Cоздать функцию которая принимает число и возвращает  текст как в примере:
#   3275  —>  "3000 + 200 + 70 +5"
#########################################

def return_text():
    current_number = (input('Insert number:'))
    divisor = len(current_number) - 1
    result = []

    for i in current_number:
        result.append(i + (divisor * '0'))
        divisor -= 1

    return ' + '.join(result)


print(return_text())
