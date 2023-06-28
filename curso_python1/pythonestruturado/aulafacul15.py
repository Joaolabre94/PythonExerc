#implementar uma solução que retorne o menor elemento de uma lista.
lista = [2,10,3,1,4,5]
def dado(valores):
    minimo = lista [0]
    for elemento in valores:
        if elemento < minimo:
            minimo = elemento
    return minimo

#menor = dado(lista)
print(dado(lista))   
