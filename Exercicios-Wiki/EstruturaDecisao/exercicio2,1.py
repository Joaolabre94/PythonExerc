#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input('Informe um valor: '))
if valor >= 0:
    print(f'Esse valor é positivo: {valor}')
else:
    print(f'Esse valor é negativo: {valor}')