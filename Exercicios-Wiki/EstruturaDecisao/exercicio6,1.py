#Faça um Programa que leia três números e mostre o maior deles.
def calc(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c

def valores():
    while True:
        try:
            num1 = float(input('Informe primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            num3 = float(input('Informe o terceiro número: '))
            resultado = calc(num1, num2, num3)
            print(f'O maior valor deles é: {resultado:.2f}')
            break

        except:
            print('Digite um valor correto.')

valores()

