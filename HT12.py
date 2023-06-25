S = int(input('Сумма: '))
P = int(input('Произведение: '))

for i in range(S):
    for j in range(P):
        if P == i * j and S == i + j:
            print(i, j)