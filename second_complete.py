import numpy as np


def first(n):
    a = np.arange(1, 10).reshape(3, 3)
    print(a)
    print()
    return a.transpose()


def second(n):
    a = np.arange(1, 5).reshape(2, 2)
    b = np.arange(5, 9).reshape(2, 2)
    print(a)
    print()
    print(b)
    print()
    return np.matmul(a, b)


def third(n):
    a = np.arange(1, 10).reshape(3, 3)
    print(a)
    print()
    print(np.linalg.matrix_rank(a))


while True:
    print('Введите номер функции:')
    print('1 - Транспонирование матрицы')
    print('2 - Умножение матриц')
    print('3 - Ранг матрицы')
    print('0 - Выход')
    n = int(input())
    if n == 1:
        print(first(n))
    if n == 2:
        print(second(n))
    if n == 3:
        print(third(n))
    if n == 0:
        exit()
