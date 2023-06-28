# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
def valores():
    while True:
        try:
            metros_quadrados_por_lata = 18 * 3
            preço_lata = 80.00
            tamanho_metros_quadrados_area = int(input('Digite o tamanho em metros quadrados da área: '))

            quantidade_latas = tamanho_metros_quadrados_area / metros_quadrados_por_lata
            if quantidade_latas % 1 != 0:
                quantidade_latas = int(quantidade_latas) + 1
            else:
                quantidade_latas = int(quantidade_latas)
            
            preço_total = quantidade_latas * preço_lata
            print("Quantidade de latas de tinta:", quantidade_latas)
            print("Preço total: R$", "{:.2f}".format(preço_total))
            break



        except:
            print('Digite valores corretos.')

valores()