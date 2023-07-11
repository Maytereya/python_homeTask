'''Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint as rd


def create_list(objs: int) -> list[int]:
    return [rd(0, 10) for _ in range(objs)]


my_l = create_list(int(input('Введите длину списка: ')))
l_min = int(input('Введите минимальное значение диапазона: '))
l_max = int(input('Введите максимальное значение диапазона: '))

print(my_l)

result = []
for i in range(len(my_l)):
    if l_min <= my_l[i] <= l_max:
        result.append(i)

print(f'Индексы элементов списка, вошедшие в диапазон от {l_min} до {l_max}: ', result)
