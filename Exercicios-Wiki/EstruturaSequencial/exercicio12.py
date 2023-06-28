#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: para homem (72.7*altura) - 58
#para mulher (62.1*h) - 44.7
resultado = str(input('Digite seu sexo [F/H]: ')).lower()

if resultado == 'f':
    alturamulher = float(input('Digite sua altura: '))
    resultado_mulher = (62*(1**alturamulher)) - 44.7
    print(f'O seu peso ideal é mulher: {resultado_mulher}')

elif resultado == 'h':
    alturahomem = float(input('Digite sua altura: '))
    resultado_homem = (72*(7**alturahomem)) - 58   
    print(f'O seu peso ideal é homem: {resultado_homem}') 
else :
    print(f'Digite o seu sexo corretamente')



