# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa 
#que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = int(input('Qual o seu salário meu querido colaborador: '))
percentual_aplicado = 0
salario_aumentado = 0
valordo_aumento = 0
if salario < 280:
    percentual_aplicado = 0.20
    valordo_aumento = (salario * 0.20)
    salario_aumentado = (salario * 0.20) + salario
    #print (f'Seu novo salário é: {salario_aumentado}')
elif salario in range(280, 700):
    percentual_aplicado = 0.15
    valordo_aumento = (salario * 0.15)
    salario_aumentado = (salario * 0.15) + salario
    #print(f'Seu novo salário é: {salario_aumentado}')
elif salario in range(700, 1500):
    percentual_aplicado = 0.10
    valordo_aumento = (salario * 0.10)
    salario_aumentado = (salario * 0.10) + salario
    #print(f'Seu novo salário é: {salario_aumentado}')
else:
    percentual_aplicado = 0.05
    valordo_aumento = (salario * 0.05)
    salario_aumentado = (salario * 0.05) + salario
   # print(f'Seu novo salário é: {salario_aumentado}')

print(f'Seu antigo salário era: {salario}')
print(f'O percentual aplicado foi de: {percentual_aplicado}')
print(f'O valor do aumento foi: {valordo_aumento} ')
print(f'O seu novo salario após o aumento é: {salario_aumentado}')

