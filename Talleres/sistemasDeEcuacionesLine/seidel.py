# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:03:22 2021

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

inv = np.linalg.inv(D-L)
Tg = inv@U


err=0

B = np.array([27.3,18.666,3.1415])
X = np.array([0,0,0])
X1 = np.array([0,0,0])
it=0
Cg =  np.inner(inv,B)
for j in range(0,50):
    X = np.inner(Tg,X)
    X = X+Cg
    
    verr=X-X1
    for i in range(0,3):
        if verr[i]>err:
            err=verr[i]
    X1=X
    it=it+1
    print(X)
    
print("solucion:",X)
print("iteraciones:",it)
print(err)



