import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor de e-mail
smtp_server = 'smtp.gmail.com'
porta = 587
remetente = 'grumelo098@gmail.com'
senha = 'bancodedados_'

# Cria a mensagem
msg = MIMEMultipart()
msg['From'] = remetente
msg['To'] = 'bruno9405@fito.br'
msg['Subject'] = 'Teste de funcionamento de script'

corpo = 'Olá, este é um e-mail de teste.'
msg.attach(MIMEText(corpo, 'plain'))

# Conecta-se ao servidor SMTP e envia o e-mail
try:
    servidor_smtp = smtplib.SMTP(smtp_server, porta)
    servidor_smtp.starttls()
    servidor_smtp.login(remetente, senha)
    servidor_smtp.send_message(msg)
    servidor_smtp.quit()
    print('E-mail enviado com sucesso.')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
