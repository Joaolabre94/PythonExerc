# 5) Crie um programa que receba o tamanho de três lados de um triângulo e determine se 
# as entradas representam um triângulo equilátero, escaleno ou isósceles.
def verificar_tipo_triangulo(a, b, c):
    if a == b == c:
        return 'Equilátero'
    if a !=b !=c != a:
        return 'Escaleno'
    else:
        return 'Isósceles'


def valores():
    while True:
        try:
            a = int(input('Digite um valor inteiro de um dos lados: '))
            b = int(input('Digite outro valor inteiro de outro lado: '))
            c = int(input('Digite mais um valor inteiro para o ultimo lado: '))
            verificar_tipo_triangulo(a, b, c)
            resultado = verificar_tipo_triangulo(a, b, c)
            print(f'Seu triangulo é: {resultado}')
            break
        except:
            print('Digite o valor corretamente')


valores()