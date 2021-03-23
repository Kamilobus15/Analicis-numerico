# este es un pequeño código que hicimos para organizar una matriz diagonal mente dominante  -
"""
Created on Fri Mar 12 07:13:32 2021

@author: PC
"""

import numpy as np

def digdom():
    A = ([[1,3,-2],[4,-1,1],[1,1,7]])
    B = ([[18.666],[27.3],[3.1416]])
    es=True
    
    aux=0
    sum0=0
    sum1=0
    sum2=0
    for i in range(0,3):
        for j in range(0,3):
            if(i==j):
             aux = abs(A[i][j])  
            if(i==0 and i!=j):
                sum0=sum0+A[i][j]
            if(i==1 and i!=j):
                sum1=sum1+A[i][j]
            if(i==2 and i!=j):
                sum2=sum2+A[i][j]
        if(i==0):
            if(aux<abs(sum0)):
                es=False
        if(i==1):
            if(aux<abs(sum1)):
                es=False
        if(i==2):
            if(aux<abs(sum2)):
                es=False  
                
    if(es==True):
        print("es")
    else:
        print("no es")
def digdom2():
    A = ([[4,-1,1],[1,3,-2],[1,1,7]])
    B = ([[18.666],[27.3],[3.1416]])
    es=True
    
    aux=0
    sum0=0
    sum1=0
    sum2=0
    for i in range(0,3):
        for j in range(0,3):
            if(i==j):
             aux = abs(A[i][j])  
            if(i==0 and i!=j):
                sum0=sum0+A[i][j]
            if(i==1 and i!=j):
                sum1=sum1+A[i][j]
            if(i==2 and i!=j):
                sum2=sum2+A[i][j]
        if(i==0):
            if(aux<abs(sum0)):
                es=False
        if(i==1):
            if(aux<abs(sum1)):
                es=False
        if(i==2):
            if(aux<abs(sum2)):
                es=False  
                
    if(es==True):
        print("es")
    else:
        print("no es")
        
print("prueba 1 matriz original:")        
digdom()
print("prueba 2 matriz intercambiando filas:")
digdom2()

