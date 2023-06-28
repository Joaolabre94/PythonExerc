# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia_semana = int(input('Digite um número: '))
if dia_semana == 1:
    print(f'Hoje é Domingo!')
elif dia_semana == 2:
    print(f'Hoje é Segunda!')
elif dia_semana == 3:
    print(f'Hoje é Terça!')
elif dia_semana == 4:
    print(f'Hoje é Quarta!')
elif dia_semana == 5:
    print(f'Hoje é Quinta!')
elif dia_semana == 6:
    print(f'Hoje é Sexta')
elif dia_semana == 7:
    print(f'Hoje é Sabado')
else:
    print('Valor inválido')