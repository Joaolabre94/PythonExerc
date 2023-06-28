# Atribuição Múltipla
a, b = 1, 2
print('Antes da troca')
print(f"O valor das variáveis: a={a}, b={b}")
# Primeira Troca
temp = a
a = b
b = temp
print('Primeira Troca')
print(f'O valor das variáveis: a={a}, b={b}')
# Segunda Troca
a, b = b, a
print('Segunda Troca')
print(f'O valor das variáveis: a={a}, b={b}')

