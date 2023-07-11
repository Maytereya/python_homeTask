A = int(input('Введите число А: '))
B = int(input('Введите число B: '))


def a_sum_b(a: int, b: int) -> int:
    if b == 0:
        return a
    return a_sum_b(a + 1, b - 1)


print('Итог: ', a_sum_b(A, B))
