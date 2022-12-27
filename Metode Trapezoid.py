print('+======== UAS PRAKTIKUM FISIKA KOMPUTASI =======+')
print('+============ FARIS HAIDAR MUBASYIR ============+')

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 6*x**2 - 3
a = float(input('Batas bawah(a) = '))   #a = 1.0
b = float(input('Batas atas (b) = '))   #b = 10.0
n = int (input('Jumlah grid (n) = '))   #n = divariasikan dimulai dari 10, 100, 1000

#Trapezoid
dx = (b-a)/(n-1)
x = np.linspace(a,b,n)
sigma = 0
for i in range (1, n-1):
    sigma += func(x[i])
hasil = 0.5*dx*(func(x[0])+2*sigma+func(x[-1]))
print(a, b, hasil)

xp = np.linspace(a,b)


