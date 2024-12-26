import numpy as np
import matrix_multi

m, p = 8, 8
n, q = 8, 8

A = 10 * np.random.rand(m, p)
B = 10 * np.random.rand(n, q)

print(matrix_multi.standard_product(A, B))
print('\n')
print(matrix_multi.winograd(A, B, m))
print('\n')
print(matrix_multi.strassen_winograd(A,B))
print('\n')
print(matrix_multi.standard_recursive(A, B))