# Faça um programa que leia 5 números e informe o maior número.
numeros = [ ]

for x in range(5):
    numero = int(input("Digite um número: "))
    numero.append(numero)

maior_numero = max(numeros)

print(f"O maior número é: {maior_numero}")  