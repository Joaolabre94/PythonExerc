# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, 
# a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def conversor(horas, minutos):
    if horas == 0:
        horas = 12
        periodo = "A.M."
    elif horas < 12:
        periodo = "A.M."
    elif horas == 12:
        periodo = "P.M."
    else:
        horas =  horas - 12
        periodo = "P.M."
    
    return horas, periodo


def saida():
    while True:
        try:
            hora_24h = input("Digite a hora no formato HH:MM (24 horas): ")
            partes = hora_24h.split(":")
            horas = int(partes[0])
            minutos = int(partes[1])
            resultado_horas, resultado_periodo = conversor(horas, minutos)
            resultado = f"{resultado_horas}:{minutos:02d} {resultado_periodo}"
            print(f"A hora convertida é: {resultado}")
            break
        except:
            print('Digite um valor correto.')


saida()