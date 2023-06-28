#Faça um Programa que leia três números e mostre o maior deles.
def valores():
    while True:
        try:
            num1 = float(input('Informe primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            num3 = float(input('Informe o terceiro número: '))
            if num1 >= num2 and num1 >= num3:
                print(f'Maior número: {num1:.2f}')
                break
            elif num2 >= num1 and num2 >= num3:
                print(f'Maior número: {num2:.2f}')
                break
            else:
                print(f'Maior número: {num3:.2f}')
                break
        except:
            print('Digite um valor correto.')

valores()