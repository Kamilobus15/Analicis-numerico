# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:49:45 2021

@author: JUAN RINCON
"""

import sympy as sp
import math

def muller(x,f,x0,x1,x2,tol):
  
    print()
    i = 0
    while True:
        i=i+1
        h0 = x1-x0
        h1 = x2 -x1
        fx0 = sp.sympify(f).subs(x,x0)
        fx1 = sp.sympify(f).subs(x,x1)
        fx2 = sp.sympify(f).subs(x,x2)
        if h0 != 0:
            del0 = (fx1-fx0)/h0
        else:
            break
        if h1 != 0:
            del1 = (fx2-fx1)/h1
        else:
            break
        d = (del1-del0)/(h0+h1)
        b = (d*h1)+del1
        #print("a: ",d)
        #print("b: ",b)
        #print("fx2: ",fx2)
        #if (pow(b,2)-(4*fx2*d))>0:
        D = math.sqrt(pow(b,2)-(4*fx2*d))
        #else:
         #   break
        if math.isnan(b) != True and math.isnan(D) != True:
            if abs(b-D) < abs(b+D):
                E = b + D
            else:
                E = b - D
        else:
            break
        h = (-2*fx2)/E
        x3 = x2 + h
        err = sp.sympify(f).subs(x,x3)
       # errp =sp.sympify(f).subs(x,err)
        #print("error: ",errp)
        #print("it ", i)
        #print(err)
        x0 = x1
        x1 = x2
        x2 = x3
        if abs(err) < tol:
            break
    print("raiz aproximada: ",x3)
    print(i," iteraciones")
def mulleracelerado(x,f,x0,x1,x2,tol):
    print()
    i = 0
    n0 = 0.0
    n1 = 0.0
    n2 = 0.0
    while True:
        h0 = x1-x0
        h1 = x2 -x1
        fx0 = sp.sympify(f).subs(x,x0)
        fx1 = sp.sympify(f).subs(x,x1)
        fx2 = sp.sympify(f).subs(x,x2)
        if h0 != 0:
            del0 = (fx1-fx0)/h0
        else:
            break
        if h1 != 0:
            del1 = (fx2-fx1)/h1
        else:
            break
        d = (del1-del0)/(h0+h1)
        b = (d*h1)+del1
        if (pow(b,2)-(4*fx2*d))>0:
            D = math.sqrt(pow(b,2)-(4*fx2*d))
        else:
            break
        if math.isnan(b) != True and math.isnan(D) != True:
            if abs(b-D) < abs(b+D):
                E = b + D
            else:
                E = b - D
        else:
            break
        h = (-2*fx2)/E
        x3 = x2 + h
        err = sp.sympify(f).subs(x,x3)
        x0 = x1
        x1 = x2
        x2 = x3
        if i == 0:
           n0 = x3
        if i == 1:
           n1 = x3
        if i == 2:
           n2 = x3
           break
        i=i+1
        if abs(err) < tol:
            break
    while True:
        i=i+1
        acc = n0-(pow(n1-n0,2)/(n2-(2*n1)+n0))
        if math.isnan(acc):
            break
        print(acc)
        err2 = sp.sympify(f).subs(x,acc)
        n0=n1
        n1=n2
        n2=acc
        if err2 < tol:
            break
    print(i," iteraciones")
    
x = sp.Symbol('x')
f = input("Ingrese la expresion en terminos de x: ")
#r = sp.sympify(f).subs(x,0)
#print(r)
x0 = float(input("ingrese el valor de x0: "))
x2 = float(input("ingrese el valor de x2: "))
x1 = (x0+x2)/2
e0 = x0
e1 = x1
e2 = x2
print("**Metodo de muller**")
print("1.muller")
print("2.muller acelerado")
op2 = int(input())
if op2 == 1:
    print("tolerancia: ")
    print("1.personalizada")
    print("2.10^-8,10^-16,10^-32 y 10^-56")
    op = int(input())
    if op == 1:
        tol = float(input("ingrese la tolerancia: "))
        muller(x,f,x0,x1,x2,tol)
    else:
        print("Tolerancia 10^-8:")
        muller(x,f,x0,x1,x2,1E-8)
        x0=e0
        x1=e1
        x2=e2
        print("Tolerancia 10^-16:")
        muller(x,f,x0,x1,x2,1E-16)
        x0=e0
        x1=e1
        x2=e2
        print("Tolerancia 10^-32:")
        muller(x,f,x0,x1,x2,1E-32)
        x0=e0
        x1=e1
        x2=e2
        print("Tolerancia 10^-56:")
        muller(x,f,x0,x1,x2,1E-56)
else:
    print("tolerancia: ")
    print("1.personalizada")
    print("2.10^-8,10^-16,10^-32 y 10^-56")
    op = int(input())
    if op == 1:
        tol = float(input("ingrese la tolerancia: "))
        mulleracelerado(x,f,x0,x1,x2,tol)
    else:
        print("Tolerancia 10^-8:")
        mulleracelerado(x,f,x0,x1,x2,1E-8)
        print("Tolerancia 10^-16:")
        mulleracelerado(x,f,x0,x1,x2,1E-16)
        print("Tolerancia 10^-32:")
        mulleracelerado(x,f,x0,x1,x2,1E-32)
        print("Tolerancia 10^-56:")
        mulleracelerado(x,f,x0,x1,x2,1E-56)
    