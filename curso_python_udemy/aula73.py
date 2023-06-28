#Me de o print de uma lista de numeros aleatorios até o 50, depois printa que a cima de 50 não podemos exibir
lista = [1,5,30,24,19,45,60,70,135]
lista = sorted(lista)
numeros_abaixo_de_50 = []

for x in lista:
    if x <= 50:
        print(x, end=', ')
    else:
        print('Não mostramos numeros acima de 50.')

print(sorted(lista))
reverso_ordenado = list(reversed(lista))
print(reverso_ordenado)