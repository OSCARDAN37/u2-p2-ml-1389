import numpy as np
# Oscar Flores NC = 1389 fecha = 22 oct 2026
# Ejemplos numpy numerenial python
print("-- Espaciado Linealmente en array -- 1389 --")
arre = np.linspace(start=0, stop=5, num=5)
print(arre)
print("-- Matriz identidad en 2D array -- 1389 --")
matrix = np.eye(3)
print(matrix)
print("-- genera numeros al azar(alatorios) en 2D array -- 1389 --")
numale = np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("-- genera 9 numeros al azar(alatorios) entre 0 y 1 -- 1389 --")
numale = np.random.random((3,3)) # genera 12 numeros aleatorios
print(numale)
# como generar numeros aleatorios 9 numeros comprendidos entre 1 y 20 
# con numpy en un arreglo de 3  por 3
print("-- genera 9 numeros al azar(alatorios) entre 1 y 20 -- 1389 --")
numale = np.random.randint(1, 21, size=9).reshape(3, 3)
print(numale)
print("Programa realizado por Oscar Flores NC = 1389")