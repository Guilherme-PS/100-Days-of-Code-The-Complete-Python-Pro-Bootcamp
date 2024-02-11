from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

# Constantes com email e senha de app
MY_EMAIL = "SEU EMAIL"
PASSWORD = "SEU CÓDIGO"

# Cria uma instancia do flask
app = Flask(__name__)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def home():
    # Envia um email
    if request.method == "POST":
        # Cria uma instância do EmailMessage
        msg = EmailMessage()

        # Define o corpo do email, assunto, remetente e destinatário
        msg.set_content(request.form.get('message'))
        msg['Subject'] = request.form.get('subject')
        msg['From'] = request.form.get("email")
        msg['To'] = MY_EMAIL

        # Configura o servidor SMTP (GMAIL)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user=MY_EMAIL, password=PASSWORD)

            server.send_message(msg)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)