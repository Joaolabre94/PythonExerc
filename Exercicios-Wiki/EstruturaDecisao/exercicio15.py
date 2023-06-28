# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
def calculos(lado1, lado2, lado3, lado4=0, lado5=0):
    if lado1 == lado2 == lado3:
        return lado1 + lado2 + lado3 
    elif lado1 == lado2 != lado3:
        return lado3 + (2*lado1)
    elif lado1 == lado3 != lado2:
        return lado2 + (2*lado1)
    elif lado2 == lado3 != lado1:
        return lado1 +(2*lado2)
    else:
        return (lado4 * lado5) / 2 
    
def verificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"


def valores():
    while True:
        try:
            lado1 = float(input('Digite o primeiro lado: '))
            lado2 = float(input('Digite o segundo lado: '))
            lado3 = float(input('Digite o terceiro lado: '))
            resultado_triangulo = verificar_triangulo(lado1, lado2, lado3)

            if resultado_triangulo == 'Escaleno':
                lado4 = float(input('Digite a base: '))
                lado5 = float(input('Digite a altura: '))
                resultado = calculos(lado1, lado2, lado3, lado4, lado5)
                print(f'A Área do triângulo informado é: {resultado:.2f}. E é um triângulo: {resultado_triangulo}')

            else:
                resultado = calculos(lado1, lado2, lado3)
                print(f'A Área do triângulo informado é: {resultado:.2f}. E é um triângulo: {resultado_triangulo}')

            while True:
                sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
                if sair == 's' or sair == 'n':
                    break
                else:
                    print('Digite [s]im ou [n]ão')
            if sair == 's':
                break

        except:
            print('Você voltou para o início, digite valores corretos.')

valores()