#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def calcular_media4notas():
    valor = 0
    for num in range(4):
        while True:
            try:
                nota = float(input(f'Digite a {num+1}ª nota bimestral: '))
                break
            except:
                print('Valor inválido, digite novamente.')
        valor = nota + valor
    media = valor / 4
    print(f'A média das notas bimestrais é: {media}')
    
calcular_media4notas()

