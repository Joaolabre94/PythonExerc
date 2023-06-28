# Faça um programa que leia 5 números e informe a soma e a média dos números.
numeros = [ ]
for x in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    soma = sum(numeros)
    media = soma / 5
print(f'A soma dos números é: {soma} \nE a media é: {media:.2f}')