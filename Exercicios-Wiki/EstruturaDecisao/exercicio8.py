#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input('Valor do primeiro produto: '))
produto2 = float(input('Valor do segundo produto: '))
produto3 = float(input('Valor do terceiro produto: '))
if produto1 < produto2 and produto1 < produto3:
    print(f'O menor preço é o primeiro produto: {produto1}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'O menor preço é o segundo produto: {produto2}')
else:
    print(f'O menor preço é o terceiro produto: {produto3}')
