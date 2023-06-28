#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = """
    Mano, vou tentar mandar a mensagem por aqui um codigo gigante, vamo ve se vai, é uma função de baskara
    def valores():
    resultado = int(input('Digite o numero da equação: '))
    return resultado
    a = valores()
    b = valores()
    c = valores()

    def calc_delta(a, b, c):
        delta = (b*b) - (4 * a * c)
        return delta

    import math
    def calc_raizes(a, b, c, delta):
        if delta < 0 :
            resultado = 'A equação não possui raízes dos números reais'
        elif delta == 0:
            x = -b / (2*a)
            resultado = f'A equação possui apenas uma raiz: {x}'
        else:
            x1 = (-b -math.sqrt(delta)) / (2*a)
            x2 = (-b +math.sqrt(delta)) / (2*a)
            resultado = f'A equação possui duas raízes: {x1}, {x2}'
        return resultado


    delta = calc_delta(a, b, c)
    resultado = calc_raizes(a, b, c, delta)
    print(resultado)
    """

#parâmetros
senha = "fptzyamhqguuizmz"
msg['From'] = "jlucaslabre2@gmail.com"
msg['To'] = " contato@skillsit.com.br"
msg['Subject'] = "Função de baskara"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')