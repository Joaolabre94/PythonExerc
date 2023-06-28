# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
def valores():
    while True:
        try:
            numero1 = int(input('Digite o primeiro número inteiro: '))
            numero2 = int(input('Digite o segundo número inteiro: '))

            if numero1 > numero2:
                numero1, numero2 = numero2, numero1

            for num in range(numero1, numero2 + 1):
                print(num, end=" ")

            break  

        except ValueError:
            print('Digite valores inteiros corretamente.')

valores()