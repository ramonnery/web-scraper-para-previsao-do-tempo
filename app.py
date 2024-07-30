from get_weather_forecasts import get_weather_forecasts
from dotenv import load_dotenv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pathlib
import os
from smtplib import SMTP

load_dotenv()
weather_forecasts = get_weather_forecasts()

# Caminho arquivo HTML
HTML_PATH = pathlib.Path(__file__).parent / 'email.html'

# Dados do remetente e do destinatário
sender = os.getenv('FROM_EMAIL', '')
recipient = 'adriadamara2000@gmail.com'

# Configurações SMTP
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_port = int(os.getenv('SMTP_PORT', ''))
smtp_username = sender
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(HTML_PATH, 'r') as file:
    file_text = file.read()
    template = Template(file_text)
    email_text = template.substitute(
        current_temperature=weather_forecasts.get('current_weather')[0],
        current_weather_condition=weather_forecasts.get('current_weather')[1],
        temperature_first_day=weather_forecasts.get('first_day_after')[0],
        weather_condition_first_day=weather_forecasts.get('first_day_after')[1],
        temperature_second_day=weather_forecasts.get('second_day_after')[0],
        weather_condition_second_day=weather_forecasts.get('second_day_after')[1],
        temperature_third_day=weather_forecasts.get('third_day_after')[0],
        weather_condition_third_day=weather_forecasts.get('third_day_after')[1]
    )

# Transformando a mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = 'Previsão do Tempo'

email_shape = MIMEText(email_text, 'html', 'utf-8')
mime_multipart.attach(email_shape)

# Enviando email
with SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')