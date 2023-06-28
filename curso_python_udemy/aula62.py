"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue
    if contador >= 50 and contador <=64:
        print(f'Não vou mostrar o numero')
        continue

    print(contador)

    if contador == 80:
        break


print('Acabou')