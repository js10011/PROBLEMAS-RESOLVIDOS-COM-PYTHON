'''Escreva um programa que se conecta ao servidor POP3, autentica,
obtém uma lista de e-mails e exibe o conteúdo do último e-mai'''
import poplib
from email.parser import BytesParser
from email.policy import default

# Servidor POP3 e credenciais
POP3_SERVER = 'pop.example.com'
POP3_PORT = 110
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Conexão ao servidor POP3 e autenticação
mailbox = poplib.POP3(POP3_SERVER, POP3_PORT)
mailbox.user(USERNAME)
mailbox.pass_(PASSWORD)

# Obtenção da lista de e-mails
num_messages = len(mailbox.list()[1])

# Se houver e-mails, obtém o conteúdo do último
if num_messages > 0:
    response, lines, octets = mailbox.retr(num_messages)
    message_content = b'\r\n'.join(lines)

    # Parsing do e-mail
    message = BytesParser(policy=default).parsebytes(message_content)
    
    # Exibição do conteúdo do último e-mail
    print(f"Subject: {message['subject']}")
    print(f"From: {message['from']}")
    print(f"To: {message['to']}")
    print(f"Date: {message['date']}")
    print("\nBody:\n")
    if message.is_multipart():
        for part in message.iter_parts():
            if part.get_content_type() == "text/plain":
                print(part.get_payload(decode=True).decode(part.get_content_charset()))
    else:
        print(message.get_payload(decode=True).decode(message.get_content_charset()))

# Fechamento da conexão
mailbox.quit()

'''Escreva um programa que se conecte a um servidor SMTP, autentique e envie um email.'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your_email@example.com'
password = 'your_password'
from_email = 'your_email@example.com'
to_email = 'recipient@example.com'
subject = 'Assunto do email'
body = 'Este é o corpo do email'

# Criação da mensagem
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Conexão com o servidor SMTP e envio do email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Estabelece uma conexão TLS
    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())
    print("Email enviado com sucesso")
except Exception as e:
    print(f"Erro ao enviar o email: {e}")
finally:
    server.quit()