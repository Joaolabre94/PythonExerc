#Implementar uma solução em python que retorne a soma de todos elementos pares de uma lista
lista = [1,3,2,5,7,10,6,8,22,31]
def par(num):
    resultado = num%2 == 0
    return resultado
def soma(x):
    total = 0
    for cadaum in x:
        if par(cadaum):
            total = cadaum + total
    return total

print(soma(lista))