#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.
hora = float(input('Informe o ganho por hora: '))
numeros = float(input('Informe as horas trabalhadas no mês: '))
x = hora * numeros
print(f'Salário total do mês trabalhado é: {x}')