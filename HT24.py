from random import randint

print(bushes := [randint(100, 200) for _ in range(int(input('Введите количество кустов на грядке: ')))])
max_berries = 0

for i in range(len(bushes)):
    if i == 0:
        current = bushes[i] + bushes[i + 1] + bushes[len(bushes) - 1]
    elif 0 < i < len(bushes) - 1:
        current = bushes[i] + bushes[i + 1] + bushes[i - 1]
    else:
        current = bushes[i] + bushes[0] + bushes[i - 1]
    if current > max_berries:
        max_berries = current

print('Наибольшее количество ягод, которые можно собрать за один заход: ', max_berries)
