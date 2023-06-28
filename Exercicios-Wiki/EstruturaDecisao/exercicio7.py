#Faça um Programa que leia três números e mostre o maior e o menor deles.
numero1 = float(input('Digite seu número: '))
numero2 = float(input('Digite seu número: '))
numero3 = float(input('Digite seu número: '))
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')