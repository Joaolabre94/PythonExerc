#Faça um Programa que leia três números e mostre o maior e o menor deles.
def valores():
    while True:
        try:
            num1 = float(input('Informe o primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            num3 = float(input('Informe o terceiro número: '))
            max1 = max(num1, num2, num3)
            min2 = min(num1, num2, num3)
            print(f'O maior número é: {max1}')
            print(f'O menor número é: {min2}')

        except:
            print('Digite o valor correto.')

valores()