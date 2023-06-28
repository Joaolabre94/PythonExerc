def validar_informacoes():
    while True:
        nome = input("Digite o nome (maior que 3 caracteres): ")
        if len(nome) > 3:
            break
        else:
            print("Nome inválido. Digite novamente.")

    while True:
        idade = int(input("Digite a idade (entre 0 e 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida. Digite novamente.")

    while True:
        salario = float(input("Digite o salário (maior que zero): "))
        if salario > 0:
            break
        else:
            print("Salário inválido. Digite novamente.")

    while True:
        sexo = input("Digite o sexo ('f' ou 'm'): ")
        if sexo.lower() == 'f' or sexo.lower() == 'm':
            break
        else:
            print("Sexo inválido. Digite novamente.")

    while True:
        estado_civil = input("Digite o estado civil ('s', 'c', 'v' ou 'd'): ")
        if estado_civil.lower() in ['s', 'c', 'v', 'd']:
            break
        else:
            print("Estado civil inválido. Digite novamente.")

    print("Informações válidas:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Salário:", salario)
    print("Sexo:", sexo)
    print("Estado Civil:", estado_civil)

# Chamada da função
validar_informacoes()