# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

imposto_de_renda = 0.11
inss = 0.08
sindicato = 0.05

def valores():
    while True:
        try:
            valor_hora = float(input('Informe quanto ganha por hora: '))
            horas_trabalhadas = float(input('Informe horas trabalhadas no mês: '))
            salario_bruto = valor_hora * horas_trabalhadas
            imposto_de_renda_final = salario_bruto - (salario_bruto * imposto_de_renda)
            inss_final = salario_bruto - (salario_bruto * inss)
            sindicato_final = salario_bruto - (salario_bruto * sindicato)
            salario_liquido = salario_bruto - (salario_bruto * imposto_de_renda) - (salario_bruto * inss) - (salario_bruto * sindicato)
            print(f'O seu salário bruto é: R${salario_bruto:.2f}')
            print(f'O seu salário -IR(11%) é: R${imposto_de_renda_final:.2f}')
            print(f'O seu salário -INSS(8%) é: R${inss_final:.2f}')
            print(f'O seu salário -Sindicato(5%) é: R${sindicato_final:.2f}')
            print(f'O seu salário liquido é: R${salario_liquido}')
            break
        except:
            print('Digite valores corretos.')

valores()