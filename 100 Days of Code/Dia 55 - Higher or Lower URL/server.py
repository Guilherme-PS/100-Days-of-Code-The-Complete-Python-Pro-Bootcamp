from flask import Flask
import random

# Define a variável app com uma instância do Flask.
app = Flask(__name__)
# Gera um número aleatório entre 0 e 9.
number = random.randint(0, 9)

# Define a rota para a página inicial do site.
@app.route("/")
def higher_lower_url():
    # Retorna uma página HTML que pede ao usuário para adivinhar um número entre 0e 9.
    return "<body style='text-align: center; font-family: Century Gothic, sans-serif'>"\
           "<h1>Adivinhe um número entre 0 e 9</h1>" \
           "<hr style='width: 50%;'></hr>" \
           "<img style='width: 25%' src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTE2OTAxZTVjZDVkYmNkZmYxNjYyNWNiNzU3MTNiMTdhYWYyN2MyZSZjdD1n/IsfrRWvbUdRny/giphy.gif'>" \
           "</body>"

# Define uma rota para um número fornecido pelo usuário.
@app.route("/<int:num>")
def correct_number(num):
    # Se o número fornecido for maior do que o número gerado, exibe uma mensagem informando que o número é muito alto.
    if num > number:
        return "<body style='text-align: center; font-family: Century Gothic, sans-serif'>" \
               "<h1 style='color: #9A2CA0'>Número Muito Alto.</h1>" \
               "<hr style='width: 50%;'></hr>" \
               "<img style='width: 25%' src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>" \
               "</body>"
    # Se o número fornecido for menor do que o número gerado, exibe uma mensagem informando que o número é muito baixo.
    elif num < number:
        return "<body style='text-align: center; font-family: Century Gothic, sans-serif'>" \
               "<h1 style='color: #BA0021'>Número muito Baixo</h1>" \
               "<hr style='width: 50%;'></hr>" \
               "<img style='width: 25%' src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>" \
               "</body>"
    # Se o número fornecido for igual ao número gerado, exibe uma mensagem informando que o usuário acertou o número.
    elif num == number:
        return "<body style='text-align: center; font-family: Century Gothic, sans-serif'>" \
               "<h1 style='color: #006400'>Você Acertou!!!</h1>" \
               "<hr style='width: 50%;'></hr>" \
               "<img style='width: 25%' src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>" \
               "</body>"


# Se o arquivo for executado diretamente, inicia o servidor Flask.
if __name__ == "__main__":
    app.run(debug=True)