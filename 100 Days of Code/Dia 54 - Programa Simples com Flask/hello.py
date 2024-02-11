from flask import Flask

# Cria uma instância do objeto Flask chamada app.
app = Flask(__name__)

# Define a rota do aplicativo.
@app.route("/")
# Define a função que será executada quando a rota for acessada.
def hello_world():
    # Retorna a mensagem "Hello, World!" em HTML.
    return "<h1>Hello, World!</h1>"


# Verifica se o scipt está sendo executado como o programa principal.
if __name__ == "__main__":
    # Inicia o servidor Flask.
    app.run()
