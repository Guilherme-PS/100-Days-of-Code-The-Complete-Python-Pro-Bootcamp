from flask import Flask, render_template, request
import requests
import smtplib

# Faz uma solicitação HTTP GET na API com os posts do blog.
data = requests.get("https://api.npoint.io/a73d89d63b9a0177806e").json()

# Dados de Email do Usuário.
MY_EMAIL = "jacquellynstvesant@gmail.com"
PASSWORD = "kbbgjdvemjlsgasx"

# Cria uma instãncia do objeto Flask.
app = Flask(__name__)

# Define a rota principal.
@app.route("/")
def home():
    return render_template("index.html", posts=data)

# Define a rota "/about.html".
@app.route("/about.html")
def about():
    return render_template("about.html")

# Define a rota "/contact.html" com suporte aos métodos GET e POST.
@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        send_email(request.form["username"], request.form["email"], request.form["phone"], request.form["message"])
        return render_template("contact.html", msg=True)
    return render_template("contact.html", msg=False)

# Define a rota "/post.html/<int:index>" que re cebe um parâmetro "index" do tipo inteiro e usa-o para buscar o post
# correspondente.
@app.route("/post.html/<int:index>")
def blog_post(index):
    for post in data:
        if post["id"] == index:
            return render_template("post.html", post=post)

# Envia os dados para o email do usuário.
def send_email(name, email, phone, message):
    new_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user=MY_EMAIL, password=PASSWORD)
        server.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=new_message.encode("utf8"))


# Verifica se o script está sendo executado como programa principal.
if __name__ == "__main__":
    app.run(debug=True)