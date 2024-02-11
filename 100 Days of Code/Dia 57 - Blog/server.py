from flask import Flask, render_template
import requests
# Importa a classe Post do módulo post.
from post import Post

# Faz uma requisição HTTP para a API.
response = requests.get("https://api.npoint.io/06cbf48d0526ec05b292")
# Cria uma lista de objetos Post a partir do JSON retornado.
data = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in response.json()]

# Cria uma instância da classe Flask.
app = Flask(__name__)

# Define a rota principal da aplicação e renderiza o tempalte "index.html" passando a lista de posts como parâmetro.
@app.route("/")
def blog():
    return render_template("index.html", data=data)

# Define uma rota para exibir um post específico com base em seu ID.
@app.route("/post/<int:post_id>")
def post(post_id):
    # Busca o post na lista de posts e renderiza o template "post.html" passando o objeto Post como parâmetro.
    for post in data:
        if post.id == post_id:
            return render_template("post.html", post=post)


# Verifica se o script está sendo executado diretamente e não sendo importado como um módulo.
if __name__ == "__main__":
    app.run(debug=True)