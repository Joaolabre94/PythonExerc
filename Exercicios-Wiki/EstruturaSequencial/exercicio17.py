# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
# isto é, considere latas cheias.

# Dados do problema
metros_quadrados_por_litro = 6
litros_por_lata = 18
preco_lata = 80.00
litros_por_galao = 3.6
preco_galao = 25.00
folga = 1.1


# Entrada do usuário
area_a_pintar = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

# Cálculos para comprar apenas latas de 18 litros
litros_necessarios = (area_a_pintar / metros_quadrados_por_litro) * folga
quantidade_latas = int(litros_necessarios / litros_por_lata)
if litros_necessarios % litros_por_lata != 0:
    quantidade_latas += 1
preco_total_latas = quantidade_latas * preco_lata

# Cálculos para comprar apenas galões de 3,6 litros
quantidade_galoes = int(litros_necessarios / litros_por_galao)
if litros_necessarios % litros_por_galao != 0:
    quantidade_galoes += 1
preco_total_galoes = quantidade_galoes * preco_galao

# Cálculos para misturar latas e galões
quantidade_latas_mistura = int(litros_necessarios / litros_por_lata)
litros_restantes = litros_necessarios % litros_por_lata
quantidade_galoes_mistura = int(litros_restantes / litros_por_galao)
if litros_restantes % litros_por_galao != 0:
    quantidade_galoes_mistura += 1
preco_total_mistura = (quantidade_latas_mistura * preco_lata) + (quantidade_galoes_mistura * preco_galao)

# Resultado
print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas de tinta:", quantidade_latas)
print("Preço total: R$", "{:.2f}".format(preco_total_latas))
print()

print("Situação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões de tinta:", quantidade_galoes)
print("Preço total: R$", "{:.2f}".format(preco_total_galoes))
print()

print("Situação 3: Misturar latas e galões")
print("Quantidade de latas de tinta:", quantidade_latas_mistura)
print("Quantidade de galões de tinta:", quantidade_galoes_mistura)
print("Preço total: R$", "{:.2f}".format(preco_total_mistura))