import numpy as np
import time

def dot_product(v,w,n):
    S = 0
    for j in range(n):
        S += v[j]*w[j]
    return S 

def standard_product(A,B):
    m, p = np.shape(A)
    q, n = np.shape(B)
    #p=q=m=n

    C = np.zeros((m,n))

    start = time.process_time()
    for j in range(m):
        for k in range(n):
            for l in range(n):
                C[j,k] += A[j,l]*B[l,k]#dot_product(A[j,:],B[:,k],m)
    end = time.process_time()

    return C, end-start

def even_odd(v,n):
    even = []
    odd = []
    for j in range(int(n/2)):
        even.append(v[2*j])
        odd.append(v[2*j+1])
    return np.array(even), np.array(odd)


def winograd1(A, B, N):
    #p=q=m=n

    A_vec = np.zeros(N)
    B_vec = np.zeros(N)                
    C = np.zeros((N,N))
    start = time.time()
    for j in range(N):
        even, odd = even_odd(A[j,:])
        A_vec[j] = dot_product(even, odd, N/2)
        even, odd = even_odd(B[:,j])
        B_vec[j] = dot_product(even, odd, N/2)

        for k in range(N):
            if N%2 == 0:
                A_even, A_odd = even_odd(A[j,:])
                B_even, B_odd = even_odd(B[:,k])

                v = A_odd + B_even
                w = A_even + B_odd

                C[j,k] = dot_product(v,w, N/2) - A_vec[j] - B_vec[k]
            else:
                A_even, A_odd = even_odd(A[j,:N-1])
                B_even, B_odd = even_odd(B[:N-1,k])

                v = A_odd + B_even
                w = A_even + B_odd

                C[j,k] = A[j,-1]*B[-1,k] + dot_product(v,w, N/2) - A_vec[j] - B_vec[k]
    end = time.time()
    return C, end-start

def winograd(A, B, N):
    #p=q=m=n

    A_vec = np.zeros(N)
    B_vec = np.zeros(N)                
    C = np.zeros((N,N))
    n= int(N/2)

    start = time.process_time()
    for j in range(N):
        for l in range(n):
            A_vec[j] += A[j,2*l]*A[j,2*l+1]
        for k in range(N):
            if B_vec[k] == 0:
                for l in range(n):
                    B_vec[k] += B[2*l,k]*B[2*l+1,k]
            for l in range(n):
                C[j,k] += (A[j,2*l+1]+B[2*l,k])*(A[j,2*l]+B[2*l+1,k])
            C[j,k] = C[j,k] - A_vec[j] - B_vec[k]
    end = time.process_time()

    return C, end-start

def split_block(A):
    m,n = np.shape(A)
    row, col = m//2, n//2
    return A[:row,:col], A[:row,col:], A[row:,:col], A[row:,col:]

def strassen_winograd(A,B):

    if np.size(A) == 1:
        return A*B
    
    a1, a2, a3, a4 = split_block(A)
    b1, b2, b3, b4 = split_block(B)

    p1 = strassen_winograd(a1, b2-b4)
    p2 = strassen_winograd(a1+a2, b4)
    p3 = strassen_winograd(a3+a4, b1)
    p4 = strassen_winograd(a4, b3-b1)
    p5 = strassen_winograd(a1+a4, b1+b4)
    p6 = strassen_winograd(a2-a4, b3+b4)
    p7 = strassen_winograd(a1-a3, b1+b2)

    c11 = p5+p4-p2+p6
    c12 = p1+p2
    c21 = p3+p4
    c22 = p1+p5-p3-p7
       
    return np.vstack((np.hstack((c11,c12)), np.hstack((c21,c22))))

def standard_recursive(A, B):
    if A.size == 1:
        return A*B

    a1, a2, a3, a4 = split_block(A)
    b1, b2, b3, b4 = split_block(B)
    
    
    c11 = standard_recursive(a1,b1) + standard_recursive(a2,b3)
    c12 = standard_recursive(a1,b2) + standard_recursive(a2,b4)
    c21 = standard_recursive(a3,b1) + standard_recursive(a4,b3)
    c22 = standard_recursive(a3,b2) + standard_recursive(a4,b4)
    
    return np.vstack((np.hstack((c11,c12)), np.hstack((c21,c22))))