from random import randint

coins = int(input('Введите число монет на столе: '))
i = 0
tails = 0
eagle = 0
while i < coins:
    side = randint(0, 1)
    print(side, end=' ')
    if side:
        eagle += 1
    else:
        tails += 1
    i += 1
print(f'Минимальное число монет, которое нужно перевернуть: {tails}' if eagle > tails else f'Перевернуть: {eagle}')
