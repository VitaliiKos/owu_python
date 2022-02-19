"""
порахувати кількість парних і непарних цифр числа,
  наприклад:
        х = 225688 -> п = 5, н = 1;
        х = 33294 -> п = 2, н = 3
"""
x = 225688
even_numbers = 0
odd_numbers = 0
print(f'x = {x}')

while x:
    if x % 10 % 2:
        even_numbers += 1
    else:
        odd_numbers += 1
    x //= 10
print(f'п = {odd_numbers}, н = {even_numbers}')
