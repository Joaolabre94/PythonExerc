#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: para homem (72.7*altura) - 58
#para mulher (62.1*h) - 44.7
sexo = input('Digite seu sexo [F/H]: ').lower()
resultado = 0
if sexo == 'f':
    altura_mulher = float(input('Digite sua altura:'))
    resultado = (62*(1**altura_mulher)) - 44.7

elif sexo == 'h':
    altura_homem = float(input('Digite sua altura: '))
    resultado = (72*(7**altura_homem)) - 58


print(f'O seu peso ideal é: {resultado}')