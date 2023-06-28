#função def 
#Implementar uma solução que retorne a soma de todos os elementos pares de uma lista.
lista = [10, 2, 5, 7, 6, 3]
soma_pares = 0
for elemento in lista:
    if elemento % 2 == 0:
        soma_pares += elemento
print("A soma dos elementos pares da lista é:", soma_pares)