# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
S = int(input('Введите общее количество журавликов: '))
p = None
k = None
if S >= 6 and S % 6 == 0:
    p = int(S / 6)
    k = 4 * p
else:
    print("Введите количество журавликов больше 6 и кратно 6")
if p:
    print("Петя сделал: ", p, "журавликов,", "Сережа сделал:", p, "журавликов,", "Катя сделала", k, "журавликов.")
else:
    print("Задача не может быть решена.")