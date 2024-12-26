import numpy as np
import matrix_multi
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

M = 1

level = 8
dimensions = [2**(j+1) for j in range(4, level)]

E = 100

#strassen_time = {key: [] for key in dimensions}
standard_time = {key: [] for key in dimensions}

#strassen_avr = {key: 0 for key in dimensions}
#strassen_error = {key: 0 for key in dimensions}
standard_avr = {key: 0 for key in dimensions}
standard_error = {key: 0 for key in dimensions}

for N in dimensions:
    
    for _ in range(E):
        A = np.random.rand(N, N)
        B = np.random.rand(N, N)

        #start_strassen = time.process_time()
        #C = matrix_multi.strassen_winograd(A, B)
        #end_strassen = time.process_time()

        #t_strassen = (end_strassen - start_strassen)
        #strassen_time[N].append(t_strassen)

        start_standard = time.process_time()
        C = matrix_multi.standard_recursive(A, B)
        end_standard = time.process_time()

        t_standard = (end_standard - start_standard)
        standard_time[N].append(t_standard)

    print(N)

    #strassen_avr[N] = np.mean(strassen_time[N])
    #strassen_error[N] = np.std(strassen_time[N])/E**(1/2)
    #strassen_time[N] = None

    standard_avr[N] = np.mean(standard_time[N])
    standard_error[N] = np.mean(standard_time[N])/E**(1/2)
    standard_time[N] = None

print('\n')
#print("avr_strassen =",strassen_avr)
#print("error_strassen =",strassen_error)
print('\n')
print("avr_standard =",standard_avr)
print("error_standard =",standard_error)
print('\n')
'''
avr_std = np.mean(standard_time)
erro_std = np.std(standard_time)/E**(1/2)
avr_strassen = np.mean(strassen_time)
erro_strassen = np.std(strassen_time)/E**(1/2)

print("avr_std=", avr_std, "erro_std=", erro_std)
print("avr_wino=", avr_strassen, "erro_wino=", erro_strassen)
print("\n")
'''