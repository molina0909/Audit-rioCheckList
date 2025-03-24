from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'kaykimolina3@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'dcvr btjq dqan jfpw')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

# Lista de e-mails dos destinatários
emails_destinatarios = [
    'molinakayki@gmail.com',
    '',
    'email3@dominio.com',
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_checklist', methods=['POST'])
def enviar_checklist():
    try:
        # Coletando os dados do formulário
        checklist = {
            'Data e Horário Confirmados': 'Sim' if request.form.get('data_horario_confirmados') else 'Não',
            'Quantidade de participantes': 'Sim' if request.form.get('qtd_participantes') else 'Não',
            'Speaker Line Renkus-Heinz IC16-8-RD': 'Sim' if request.form.get('speaker_line') else 'Não',
            'Speaker Teto JBL Pro CONTROL 16CT': 'Sim' if request.form.get('speaker_teto') else 'Não',
            'Microfones Shure SM58': 'Sim' if request.form.get('microfone_shure') else 'Não',
            'Microfones Lapela Shure': 'Sim' if request.form.get('microfone_lapela') else 'Não',
            'Microfone Gooseneck (Púlpito)': 'Sim' if request.form.get('microfone_gooseneck') else 'Não',
            'Interface Câmeras Panasonic AW-RP60GJ': 'Sim' if request.form.get('interface_cameras') else 'Não',
            'Interface Blackmagic Design ATEM TV Studio Pro': 'Sim' if request.form.get('interface_blackmagic') else 'Não',
            'Mixer Yamaha QL-1': 'Sim' if request.form.get('mixer_yamaha') else 'Não',
            'Automação Via AMX': 'Sim' if request.form.get('automacoes_amx') else 'Não',
            'Rack - Verificação de temperatura e ligações': 'Sim' if request.form.get('rack_temperatura') else 'Não',
            'Monitores Edifier R1280DB': 'Sim' if request.form.get('monitor_edifier') else 'Não',
            'Codec Cisco SX80': 'Sim' if request.form.get('codec_cisco') else 'Não',
        }

        # Construindo o corpo do e-mail em HTML
        corpo_email_html = """
        <!DOCTYPE html>
        <html>
          <body style="font-family: Arial, sans-serif; color: #333; background-color: #f9f9f9; padding: 20px;">
            <div style="background-color: #ffffff; padding: 20px; border-radius: 8px;">
              <h2 style="color: #1a73e8; text-align: center;">Checklist Pré-Evento</h2>
              <ul style="list-style: none; padding: 0;">
        """
        for item, status in checklist.items():
            corpo_email_html += f'<li><strong>{item}:</strong> {status}</li>'

        corpo_email_html += """
              </ul>
              <p style="margin-top: 20px;">Atenciosamente,<br><strong>Equipe AbsolutTechnologies & GPA</strong></p>
            </div>
          </body>
        </html>
        """

        # Enviando o e-mail com HTML
        msg = Message('Checklist Pré-Evento - AbsolutTechnologies & GPA', recipients=emails_destinatarios)
        msg.html = corpo_email_html
        mail.send(msg)

        return 'Checklist enviado com sucesso!'

    except Exception as e:
        print(e)  # Log para debug
        return f'Ocorreu um erro ao enviar o e-mail: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
