# Exemplo de uma calculadora simples em Python

# Função para adicionar dois números
def add(x, y):
   return x + y

# Função para subtrair dois números
def subtract(x, y):
   return x - y

# Função para multiplicar dois números
def multiply(x, y):
   return x * y

# Função para dividir dois números
def divide(x, y):
   return x / y

# Mensagem de boas-vindas
print("Bem-vindo à calculadora Python!")

# Solicita que o usuário digite dois números e uma operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
oper = input("Digite a operação (+, -, *, /): ")

# Realiza a operação selecionada
if oper == '+':
   print(num1, "+", num2, "=", add(num1,num2))

elif oper == '-':
   print(num1, "-", num2, "=", subtract(num1,num2))

elif oper == '*':
   print(num1, "*", num2, "=", multiply(num1,num2))

elif oper == '/':
   print(num1, "/", num2, "=", divide(num1,num2))

else:
   print("Operação inválida. Tente novamente.")