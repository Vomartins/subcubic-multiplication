import numpy as np
import matrix_multi
import time
import matplotlib.pyplot as plt

N = 100
list_N = []
K = []

for _ in range(10):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    C, tempo = matrix_multi.winograd(A, B, N)

    aux = ((tempo)/(N**3))*(2*17026)*10**(3)-3
    print(aux)
    K.append(aux)
    list_N.append(N)
    N += 50

plt.figure(figsize=(8,5))
plt.title('w',size=18)
plt.plot(list_N,K)
plt.grid(True)
plt.tight_layout()

plt.show()