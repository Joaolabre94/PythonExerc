# Altere o programa anterior para mostrar no final a soma dos números.
def valores():
    while True:
        try:
            numero1 = int(input('Digite o primeiro número inteiro: '))
            numero2 = int(input('Digite o segundo número inteiro: '))

            if numero1 > numero2:
                numero1, numero2 = numero2, numero1

            for num in range(numero1, numero2 + 1):
                print(num, end=" ")

            soma = numero1 + numero2
            print(f'\nA soma dos números é: {soma}')
            break  

        except ValueError:
            print('Digite valores inteiros corretamente.')

valores()