from flask import Flask, render_template, request
from login_form import LoginForm
from flask_bootstrap import Bootstrap

# Criando uma instância do objeto Flask.
app = Flask(__name__)
# Definindo uma chave para a aplicação.
app.secret_key = "loginform"
# Inicializa a extensão Bootstrap com a instância do Flask criada.
Bootstrap(app)

# Rota para a página inicial.
@app.route("/")
def home():
    return render_template('index.html')

# Rota para a página de login, que aceita métodos GET e POST.
@app.route("/login.html", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    # Verifica se o método da requisição é POST e se o formulário foi validado.
    if request.method == "POST" and login_form.validate_on_submit():
        # Verifica se as credenciais de login são válidas.
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    # Renderiza a página de login e passando a instância do formulário criada como argumento.
    return render_template("login.html", form=login_form)


# Verifica se o programa está sendo executado como programa principal.
if __name__ == '__main__':
    app.run(debug=True)