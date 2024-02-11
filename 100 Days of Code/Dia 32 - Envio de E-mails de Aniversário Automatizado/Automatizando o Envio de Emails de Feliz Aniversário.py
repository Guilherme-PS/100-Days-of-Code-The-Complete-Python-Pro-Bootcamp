import datetime as dt
import pandas as pd
import smtplib
import random

# Adicione suas credenciais de email e senha de app.
MY_EMAIL = "SEU EMAIL"
PASSWORD = "SENHA DO APP"

# Obtém a data e hora atuais.
now = dt.datetime.now()

# Lê o arquivo .CSV de aniversários.
df = pd.read_csv("birthdays.csv")

# Itera sobre o arquivo .CSV.
for index, row in df.iterrows():
    # Verifica se a data atual corresponde à data de aniversário de alguém da lista.
    if now.month == row["month"] and now.day == row["day"]:
        # Abre uma carta de aniversário aleatória.
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", mode="r", encoding="utf8") as letter:
            letter = letter.read()

            # Preenche o nome do d estinatário na carta.
            message = f"Subject:Feliz Aniversário!\n\n{letter.replace('[NAME]', row['name'])}"

            # Envia o email.
            with smtplib.SMTP("SERVER DO SEU EMAIL", 587) as server:
                server.starttls()
                server.login(user=MY_EMAIL, password=PASSWORD)
                server.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row["email"],
                                msg=message.encode("utf8"))
