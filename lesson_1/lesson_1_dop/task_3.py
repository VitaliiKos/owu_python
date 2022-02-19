"""
 3. Знайти анаграму.
    Перевірити чи слово має в собі такі самі літери як і поеперднє слово.
    ANAGRAM | MGANRAA -> true
    EXIT | AXET -> false
    GOOD | DOGO -> true
"""

first_word = sorted(i for i in input('Insert fist word: '))
second_word = sorted(i for i in input('Insert second word: '))

if len(first_word) == len(second_word):

    for i in range(len(first_word) - 1):
        if first_word[i] != second_word[i]:
            print('False')
            break
    else:
        print('True')

else:
    print('False')
