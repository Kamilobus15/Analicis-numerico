# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 09:58:50 2021

@author: PC
"""

from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**3-2*x**2+(4/3)*x-(8/27)

#x = np.linspace(start=-10,stop=10,num=100)
#plt.plot(x,f(x))
#plt.grid()
#plt.axhline(y=0,linewidth=2,c='k')
#plt.axvline(x=0,linewidth=2,c='k')
#plt.show()

sol=root_scalar(f,method='brentq',bracket=[0.5,0.7],xtol=2e-60)

print()
print("prueba 1 metodo de brent con interpolacion cuadratica inversa:")
print("raiz aproximada: ","{:.30f}".format(sol.root))
print("Iteraciones: ",sol.iterations)


      
      