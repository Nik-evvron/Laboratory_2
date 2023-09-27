def first(n):
    # Транспонирование матрицы

    n, m = int(input('Введите кол-во строк:')), int(input('Введите кол-во столбцов:'))  # Размерность матрицы
    a = [[0] * m for _ in range(n)]
    count = 1

    for i in range(n):
        for j in range(m):
            print('Введите', count, 'элемент матрицы: ')
            a[i][j] = input()
            count += 1
    print()
    print('Вывод:')

    for i in range(n):  # Вывод матрицы
        for j in range(m):
            print(a[i][j], end=' ')
        print()
    print()
    for i in range(m):  # Вывод транспонированной матрицы
        for j in range(n):
            print(a[j][i], end=' ')
        print()
    return ''


def second(n):
    # Умножение матриц

    n1, m1 = int(input('Введите кол-во строк:')), int(input('Введите кол-во столбцов:'))
    f_m = [[0] * m1 for _ in range(n1)]
    count = 1
    for i in range(n1):
        for j in range(m1):
            print('Введите', count, 'элемент матрицы:')
            f_m[i][j] = input()
            count += 1
    print()
    n2, m2 = int(input('Введите кол-во строк:')), int(input('Введите кол-во столбцов:'))
    s_m = [[0] * m2 for _ in range(n2)]
    count = 1
    for i in range(n2):
        for j in range(m2):
            print('Введите', count, 'элемент матрицы:')
            s_m[i][j] = input()
            count += 1

    print()
    print('Матрица 1:')
    for i in range(n1):
        for j in range(m1):
            print(f_m[i][j], end=' ')
        print()
    print('Матрица 2:')
    for i in range(n2):
        for j in range(m2):
            print(s_m[i][j], end=' ')
        print()
    print()
    if n2 == m1:
        m = len(f_m)
        n = len(s_m)
        k = len(s_m[0])
        res_m = [[0] * k for __ in range(m)]
        for i in range(m):
            for j in range(k):
                res_m[i][j] = sum(int(f_m[i][kk]) * int(s_m[kk][j])
                                  for kk in range(n))
        print('Результат умножения матриц:')
        for i in range(len(res_m)):
            for j in range(len(res_m)):
                print(res_m[i][j], end=' ')
            print()
    else:
        print('Длина строки М1 и столбца М2 не равны')
    return ''


def third(n):
    # Ранг матрицы

    n, m = int(input('Введите кол-во строк:')), int(input('Введите кол-во столбцов:'))
    count = 1
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            print('Введите', count, 'элемент матрицы')
            matrix[i][j] = int(input())
            count += 1
    if n < m:
        minn = n
    else:
        minn = m
    for k in range(1, minn):
        for l in range(1, n):
            if l != k:
                if matrix[k][k] != 0:
                    sz = matrix[l][k] / matrix[k][k]
                    for j in range(1, m):
                        matrix[l][j] = matrix[l][j] - sz * matrix[k][j]
    rang = 0
    for l in range(minn):
        if matrix[l][l] != 0:
            rang += 1
    print('rang=', rang)
    return ''


while True:
    print('Введите номер функции:')
    print('1 - Транспонирование матрицы')
    print('2 - Умножение матриц')
    print('3 - Ранг матрицы')
    print('0 - Выход')
    a = int(input())
    if a == 1:
        print(first(a))
    if a == 2:
        print(second(a))
    if a == 3:
        print(third(a))
    if a == 0:
        exit()
