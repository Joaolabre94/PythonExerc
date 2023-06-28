#Faça um Programa que converta metros para centímetros.
def valores():
    while True:
        try:
            metros = float(input('Informe o valor em metros: '))
            calculo = metros * 100
            print(f'O valor em centímetros ficou: {calculo}')
            break
        except:
            print(f'Por favor, digite um número.')

valores()