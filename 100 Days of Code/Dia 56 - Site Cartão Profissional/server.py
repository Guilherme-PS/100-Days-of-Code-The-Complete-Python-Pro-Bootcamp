from flask import Flask, render_template

# Cria uma instância do Flask, que representa a aplicação.
app = Flask(__name__)

# Definição da rota padrão da aplicação.
@app.route("/")
def home():
    return render_template("index.html")


# Verifica se o script está sendo executado diretamente e não sendo importado como um módulo.
if __name__ == "__main__":
    app.run(debug=True)