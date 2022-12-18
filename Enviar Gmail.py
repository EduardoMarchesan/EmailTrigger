import smtplib
import email.message

def enviar_email():  
    corpo_email = "<body style=background:bisque;text-align:center;><h1 style=background:red;text-align:center;color:white;>Relatorio</h1>"
    corpo_email= corpo_email+"Adicione Informaçoes"

    corpo_email=corpo_email+"</body>"
            #### TEXTO DA MENSAGEM ACIMA,SUPORTA HTML

    msg = email.message.Message()
    msg['Subject'] = "Assunto"     ### Titulo do Email
    msg['From'] = '{subtitua pelo remetente}'   #### EMAIL QUE ENVIA
    msg['To'] = '{subtitua pelo receptor}'
    password = 'token gerado no google'  ##### Token Gerado Na Segurança do Google
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("Enviado")



enviar_email()

