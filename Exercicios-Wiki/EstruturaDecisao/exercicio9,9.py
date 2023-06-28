#Faça um Programa que leia três números e mostre-os em ordem decrescente.
numeros = []
for each in range(3):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

numeros.sort(reverse=True)

print('Os numeros em ordem decrescente são: ')
for numero in numeros:
    print(numero)