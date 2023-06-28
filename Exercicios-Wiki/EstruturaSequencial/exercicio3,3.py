#Faça um Programa que peça dois números e imprima a soma.
def valores():
    while True:
        try:
            num1 = float(input('Informe o primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            x = num1 + num2
            print(f'A soma dos dois números é: {x}')
            break
        except:
            print(f'Digite um número!')

valores()