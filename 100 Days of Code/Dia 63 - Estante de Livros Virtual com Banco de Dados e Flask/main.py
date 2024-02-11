from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do Flask.
app = Flask(__name__)
# Configuração do banco de dados.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Cria uma instância do SQLAlchemy.
db = SQLAlchemy(app)

# Cria a classe Books para representar a tabela de livros no banco de dados.
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"<Books {self.id} - {self.title} - {self.author} - {self.rating}>"


with app.app_context():
    # Criação de todas as tabelas definidas pelos modelos do SQLAlchemy.
    db.create_all()

# Define a rota principal da aplicação.
@app.route('/')
def home():
    # Busca todos os livros na tabela Books.
    books_data = Books.query.all()

    # Renderiza o modelo "index.html" com a lista de livros.
    return render_template("index.html", books=books_data)

# Define a rota para adicionar livros ao banco de dados.
@app.route("/add", methods=["GET", "POST"])
def add():
    # Verifica se a solicitação foi um POST.
    if request.method == "POST":
        with app.app_context():
            # Adiciona um novo livro à tabela Books.
            db.session.add(Books(title=request.form["title"],
                                 author=request.form["author"],
                                 rating=request.form["rating"]))
            # Confirma a adição no banco de dados.
            db.session.commit()

            return redirect(url_for("home"))
    return render_template("add.html")

# Define a rota para editar a avaliação de um livro no banco de dados.
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        with app.app_context():
            book_id = request.form["id"]
            get_book = db.session.get(Books, book_id)
            # Atualiza a avaliação do livro.
            get_book.rating = request.form["new_rating"]

            # Confirma a atualização no banco de dados.
            db.session.commit()
            return redirect(url_for('home'))

    book_id = request.args.get("id")
    get_book = db.session.get(Books, book_id)

    return render_template("edit.html", book=get_book)

@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book = db.session.get(Books, book_id)

    # Exclui o livro na tabela Books.
    db.session.delete(book)
    # Confirma a exclusão no banco de dados.
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

