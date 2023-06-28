# Faça um Programa que peça dois números e imprima o maior deles.

def calculo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
def valores():
    while True:
        try:
            valor1 = int(input('Escreva um número inteiro: '))
            valor2 = int(input('Escreva outro número inteiro: '))
            resultado = calculo(valor1,valor2)
            print(f'O maior número desses dois valores é: {resultado}')
            break
        except:
            print('Digite um valor correto.')

valores()