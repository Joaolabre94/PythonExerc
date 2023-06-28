#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def valores():
    while True:
        try: 
            nota1 = float(input('Digite a nota do 1ª bimestre: '))
            nota2 = float(input('Digite a nota do 2ª bimestre: '))
            nota3 = float(input('Digite a nota do 3ª bimestre: '))
            nota4 = float(input('Digite a nota do 4ª bimestre: '))
            media = (nota1+ nota2 + nota3 + nota4) / 4
            print(f'A media das suas notas é: {media}')   
            break
        except:
            print('Valor inserido incorreto, digite novamente')

valores()