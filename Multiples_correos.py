import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Colocamos la direccion de correo nuestra o de donde salga
sender_address = '@gmail'
sender_pass = '1234'

#Iniciamos la conexion al servidor de correo electronico(direccion, puerto)
session = smtplib.SMTP("smtp.server.com", 587)
session.starttls()
session.login(sender_address, sender_pass)

#Ofrecemos una dirreccion de correo electronico dde una lista de dirrecciones
for correo in ['@gmail', '@gmail.com', '@gmail.com']:
    message = MIMEMultipart()
    message['Form'] = sender_address
    message['Subject'] = 'Cumpleanos'
    mail_content = "Estas invitado a mi cumple"
    message.attach(MIMEText(mail_content, 'plain'))
    text = message.as_string()
    #Finalmente enviamos el ensaje
    session.sendmail(sender_address, correos, text)
session.quit()
