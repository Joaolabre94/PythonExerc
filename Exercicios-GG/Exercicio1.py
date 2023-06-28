#Implemente um programa para uma revendedora de carros que calcule o salário de cada vendedor.
#Considere que todos os carros tem o mesmo valor, e que a revendedora paga:
#a) um salario fixo de dois salarios minimos a seus vendedores
#b) uma comissao fixa de R$50,00 por carro que for vendido
#c) caso o vendedor tenha vendido mais de 10 carros, uma comissao variavel de 5% do valor total 
#das vendas
def valores():
    while True:
        try:
            salario_minimo = 1300  # valor do salário mínimo atual
            salario_fixo = 2 * salario_minimo  # salario fixo dos vendedores
            carros_vendidos = int(input('Informe a quantidade de carros vendidos: '))  
            comissao_fixa = 50 * carros_vendidos
            if carros_vendidos > 10:
                comissao_variavel = (comissao_fixa * 0.05) 
            else:
                comissao_variavel = 0
            salario_final = salario_fixo + comissao_fixa + comissao_variavel
            print(f'Seu salário final é: {salario_final}')
            break

        except:
            print('Digite um valor correto.')

valores()