import numpy as np
import matrix_multi
import threading 

N = 400

std_time = []
wino_time = []

def standard_time(A, B):
    C, tempo_std = matrix_multi.standard_product(A, B)
    std_time.append(tempo_std)
    return None

def winograd_time(A, B, N):
    C, tempo_wino = matrix_multi.winograd(A, B, N)
    wino_time.append(tempo_wino)
    return None

E = 100

if __name__ == '__main__':
    for _ in range(E):
        A = np.random.rand(N, N)
        B = np.random.rand(N, N)

        thread1 = threading.Thread(target=standard_time(A, B))
        thread2 = threading.Thread(target=winograd_time(A, B, N))

        thread1.start()
        thread2.start()

    avr_std = np.mean(std_time)
    erro_std = np.std(std_time)/E**(1/2)
    avr_wino = np.mean(wino_time)
    erro_wino = np.std(wino_time)/E**(1/2)

    print("avr_std =", avr_std, "error_std =", erro_std)
    print("avr_wino =", avr_wino, "error_wino =", erro_wino)
    print("\n")

    ratio = (avr_wino/avr_std)
    std_ratio = np.sqrt((erro_wino/avr_std)**2+(erro_std*avr_wino/avr_std**2)**2)
    print("tau =",ratio, "error_tau =", std_ratio)
    w = ((3-2*ratio)/(2*ratio-1))

    print("w =",w,"error_w =",np.abs(4/((2*ratio-1)**2))*std_ratio)