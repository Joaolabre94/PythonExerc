# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
# (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas 
# trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
valor_hora = int(input('Digite o valor da sua hora de trabalho: '))
quantidade_horas = int(input('Digite a quantidade de horas trabalhas no mês: '))
salario = valor_hora * quantidade_horas
ir = 0
inss = 0
fgts = 0
total_descontos = 0
salario_liquido = 0
if salario <= 900:
    ir = 0
    inss = (salario * 0.10) 
    fgts = (salario * 0.11)
    total_descontos = ir + inss 
    salario_liquido = salario - total_descontos
elif salario in range(900, 1500):
    ir = (salario * 0.05)
    inss = (salario * 0.10)
    fgts = (salario * 0.11)
    total_descontos = ir + inss
    salario_liquido = salario - total_descontos
elif salario in range(1500, 2500):
    ir = (salario * 0.10)
    inss = (salario * 0.10)
    fgts = (salario * 0.11)
    total_descontos = ir + inss
    salario_liquido = salario - total_descontos
else:
    ir = (salario * 0.20)
    inss = (salario * 0.10)
    fgts = (salario * 0.11)
    total_descontos = ir + inss
    salario_liquido = salario - total_descontos

print(f'         Salário Bruto: ({valor_hora} * {quantidade_horas})        : R$ {salario}')
print(f'         (-) IR (5%)                     : R$  {ir} ')
print(f'         (-) INSS ( 10%)                 : R$  {inss}')
print(f'         FGTS (11%)                      : R$  {fgts}')
print(f'         Total de descontos              : R$  {total_descontos}')
print(f'         Salário Liquido                 : R$  {salario_liquido}')


