# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:55:47 2021

@author: PC
"""

import numpy as np

A = np.array([[4,-1,1],[1,3,-2],[1,1,7]])
D = np.array([[0,0,0],[0,0,0],[0,0,0]])
L = np.array([[0,0,0],[0,0,0],[0,0,0]])
U = np.array([[0,0,0],[0,0,0],[0,0,0]])

X=A.shape
print(A)
print()
for i in range(0,X[0]):
    for j in range(0,X[1]):
        if i==j:
            D[i][j]=A[i][j]
    
    

print()
print(D)
aux = 0
for i in range(0,X[0]):
    for j in range(0,X[1]):
        if i>j:
            L[i][j]=-A[i][j]
print()
print(L)

for i in range(0,X[0]):
    for j in range(0,X[1]):
        if i<j:
            U[i][j]=-A[i][j]
print()
print(U)

Dinv=np.linalg.inv(D)
suma=L+U
Tj = Dinv@suma

print(Tj)

B = np.array([27.3,18.666,3.1415])
X = np.array([0,0,0])
X1 = np.array([0,0,0])

Cj = np.inner(Dinv,B)
print(Cj)
it = 0

err=0

for j in range(0,50):
    X = np.inner(Tj,X)
    X = X+Cj
    verr=X-X1
    for i in range(0,3):
        if verr[i]>err:
            err=verr[i]
    
    X1=X
    it=it+1
    print(X)
    
print("solucion:",X)
print("iteraciones:",it)
print("Error maximo:",err)