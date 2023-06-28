#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
num1 = float(input('Digite um número inteiro: '))
num2 = float(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))
c1 = (2*num1) * (num2/2)
c2 = (3*num1) + num3
c3 = num3**3
print(f'O produto do dobro do primeiro com metade do segundo é: {c1}')
print(f'A soma do triplo do primeiro com o terceiro é: {c2}')
print(f'O terceiro elevado ao cubo é: {c3}')