#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('Primeiro bimestre: '))
nota2 = float(input('Segundo bimestre: '))
nota3 = float(input('Terceiro bimestre: '))
nota4 = float(input('Quarto bimestre: '))

media = (nota1+nota2+nota3+nota4) / 4
print(f'Sua média foi: {media}')