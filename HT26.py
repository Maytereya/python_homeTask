A = int(input('Введите число А: '))
B = int(input('Введите число B: '))


def a_pow_b(a: int, b: int) -> int:
    if b == 1:
        return a
    return a_pow_b(a, b - 1) * a


print('Итог: ', a_pow_b(A, B))
