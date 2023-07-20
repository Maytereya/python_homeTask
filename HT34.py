frase = input('Введите фразу для оценки ритма: ')
# frase = 'парарам пам-пам-па падам-пам'
frase = frase.split()


def find_a(str1: str) -> int:
    sum1 = 0
    for i in str1:
        if i == 'а':
            sum1 += 1
    return sum1


def rithm(lst):
    if len(set(map(lambda al: find_a(al), lst))) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


rithm(frase)
