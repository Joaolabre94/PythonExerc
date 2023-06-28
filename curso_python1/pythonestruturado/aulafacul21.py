#implementar uma solução em Python que retorne o menor elemento de uma lista.
minhalista=[2,4,8,14,28,37,1, 42,60]
def minimo(lista):
    minimo = lista [0]
    for num in lista:
        if num < minimo :
            minimo = num
    return minimo

menor = minimo(minhalista)
print([menor])