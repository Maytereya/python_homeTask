# print_operation_table(operation, num_rows=6, num_columns=6)
# print_operation_table(lambda x, y: x * y)
# n, m = 6, 6
# a = [[i*j for j in range(1, m + 1)] for i in range(1, n + 1)] # Так короче и проще, но не по условию задачи (.

print(*(lambda z: ("\t".join(f"{i * j}" for j in range(1, z)) for i in range(1, z)))(
    int(input('Введите размер столбца и строки: ')) + 1), sep="\n")


'''def print_matrix(mtx):
    for row in mtx:
        for x in row:
            print('{:4d}'.format(x), end=" ")
        print()'''


# print_matrix(a)
