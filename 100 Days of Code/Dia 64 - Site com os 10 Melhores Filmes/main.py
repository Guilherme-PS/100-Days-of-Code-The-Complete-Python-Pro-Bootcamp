from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import RateMovieForm, AddMovie
import requests

# Chave da API do TheMovieDB.
API_KEY = "3650a821a3de93cfff6100bf8908f649"

# Configurações do Flask e do SQLAlchemy.
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6bJ'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
Bootstrap(app)

# Cria o banco de dados.
db = SQLAlchemy(app)

# Define as colunas do banco de dados.
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(50))
    img_url = db.Column(db.Text, nullable=False)


# Cria a tabela do banco de dados.
with app.app_context():
    db.create_all()

# Rota principal.
@app.route("/")
def home():
    # Busca os filmes no banco de dados, ordenados pelas avaliações.
    data = Movie.query.order_by(Movie.rating).all()

    # Define o ranking de cada filme com base na posição na lista.
    for index in range(len(data), 0, -1):
        data[index - len(data) - 1].ranking = index

    # Exibe a página principal.
    return render_template("index.html", movies=data)

# Rota para adicionar filmes.
@app.route("/add", methods=["GET", "POST"])
def add():
    # Cria o formulário para adicionar os filmes.
    addform = AddMovie()
    # Obtém o ID do filme a partir dos argumentos da URL, se existir.
    movie_id = request.args.get("movie_id")

    # Se o formulário for enviado e validado.
    if addform.validate_on_submit():
        # Faz uma solicitação à API do TheMovieDB para buscar os filmes pelo título.
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}"
                                f"&language=en-US&query={addform.name.data}&page=1&include_adult=false")

        # Exibe a lista de filmes.
        return render_template("select.html", movie_list=response.json()["results"])

    # Se um filme for selecionado na lista.
    if movie_id:
        # Busca informações do filme selecionado na API do TheMovieDB.
        movie = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US").json()

        # Adiciona os registros de filme no banco de dados.
        with app.app_context():
            db.session.add(Movie(title=movie["original_title"],
                                 year=movie["release_date"][:4],
                                 description=movie["overview"],
                                 img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"))

            # Confirma a adição de registros no banco de dados.
            db.session.commit()

        # Envia o ID do filme para a rota de edição.
        for movie in Movie.query.filter_by(title=movie["original_title"]):
            return redirect(url_for("edit", id=movie.id))

    # Exibe a página para adicionar filmes.
    return render_template("add.html", form=addform)

# Rota para adicionar a descrição e a avaliação para o filme.
@app.route("/edit", methods=["GET", "POST"])
def edit():
    # Cria o formulário para editar a avaliação e a descrição.
    editform = RateMovieForm()
    # Obtém o registro do filme com o ID especificado na requisição.
    movie = db.session.get(Movie, request.args.get("id"))

    # Se o formulário for validado.
    if editform.validate_on_submit():
        # Atualiza a nota e a avaliação do filme no registro correspondente.
        movie.rating = float(editform.rating.data)
        movie.review = editform.review.data

        # Confirma as atualizações no banco de dados.
        db.session.commit()
        # Redireciona o usuário para a página inicial.
        return redirect(url_for("home"))

    # Exibe a página para adicionar a descrição e a avaliação do filme.
    return render_template("edit.html", movie=movie, form=editform)

# Define a rota para remover os filmes.
@app.route("/delete", methods={"GET", "POST"})
def delete():
    # Obtém o registro do filme com o ID especificado na requisição.
    db.session.delete(db.session.get(Movie, request.args.get("id")))
    # Confirma a remoção no banco de dados.
    db.session.commit()

    # Redireciona o usuário para a página principal.
    return redirect(url_for("home"))


# Verifica se o programa está sendo executado como programa principal.
if __name__ == '__main__':
    app.run(debug=True)
