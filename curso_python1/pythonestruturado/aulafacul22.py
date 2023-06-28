#Implementar uma solução em python que retorne o menor elemento de uma lista
lista = [5,2,8,5,6,9,12,1,6]
def menor(num):
    minimo = lista[0]
    for cadaum in num:
        if cadaum < minimo:
            minimo = cadaum
    return minimo

print(menor(lista))