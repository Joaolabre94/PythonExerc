#implementar uma solução em python que retorne a soma de todos os elementos pares de uma lista.
lista = [2,5,6,7,10,11,31,46]
def pares(numeros):
    resultado = numeros%2 == 0
    return resultado
def somarpares(listar):
    soma = 0
    for cadauma in listar:
        if pares(cadauma):
            soma = soma + cadauma
    return soma
soma = somarpares(lista)
print(soma)
