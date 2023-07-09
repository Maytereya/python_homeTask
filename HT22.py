import random

print(my_list1 := [random.randint(0, 30) for _ in range(int(input('Введите размер множества №1: ')))])
print(my_list2 := [random.randint(0, 10) for _ in range(int(input('Введите размер множества №2: ')))])


def sorter(some_list):
    for i in range(len(some_list) - 1):
        if some_list[i] > some_list[i + 1]:
            some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
    some_list = set(some_list)
    return some_list


print("Итоговая последовательность: ", my_list1 := sorter(my_list1).union(sorter(my_list2)))
