from flask import Flask, render_template
import requests

# Faz uma solicitação HTTP GET na API com os posts do blog.
data = requests.get("https://api.npoint.io/a73d89d63b9a0177806e").json()

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

# Define a rota "/contact.html".
@app.route("/contact.html")
def contact():
    return render_template("contact.html")

# Define a rota "/post.html/<int:index>" que re cebe um parâmetro "index" do tipo inteiro e usa-o para buscar o post
# correspondente.
@app.route("/post.html/<int:index>")
def blog_post(index):
    for post in data:
        if post["id"] == index:
            return render_template("post.html", post=post)


# Verifica se o script está sendo executado como programa principal.
if __name__ == "__main__":
    app.run(debug=True)