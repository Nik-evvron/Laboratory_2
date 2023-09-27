import numpy
import timeit

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = numpy.linalg.matrix_power(a,-1)
print(timeit.timeit('b', number=1000))
