#Faça um Programa que peça dois números e imprima o maior deles.
# def encontrar_maior_numero(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# # Solicitar dois números ao usuário
# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))

# # Chamar a função para encontrar o maior número
# maior_numero = encontrar_maior_numero(numero1, numero2)

# # Imprimir o resultado
# print(f"O maior número é: {maior_numero}")

def valores():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um secundo número: '))
    if num1 > num2:
        print(f'O maior número é: {num1}')
    else:
        print(f'O maior número é: {num2}')
    
valores()