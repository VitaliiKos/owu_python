"""
 4. Точная степень двойки
  Дано натуральное число N.
      Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
      Операцией возведения в степень пользоваться нельзя!
"""

check_number = int(input('Insert number: '))
two = 2

while True:
    if two == check_number:
        print('Yes')
        break
    elif two > check_number:
        print('No')
        break
    two *= 2
