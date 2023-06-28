#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: para homem (72.7*altura) - 58
#para mulher (62.1*h) - 44.7
sexo = str(input('Digite seu sexo [F/H]: '))
altura = float(input('Digite sua altura: '))
resultado = 0

if sexo == 'F'.lower():
    resultado = (62*(1**altura)) - 44.7
    print(f'O seu peso ideal é mulher: {resultado}')

elif sexo == 'H'.lower():
    resultado = (72*(7**altura)) - 58  
    print(f'O seu peso ideal é homem: {resultado}') 



print(resultado)