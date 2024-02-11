from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])

    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# Rota para a página inicial.
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()

    return render_template("index.html", all_posts=posts)

# Rota para um post específico.
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)

    return render_template("post.html", post=requested_post)

# Rota para adicionar um post.
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    now = dt.datetime.now()
    add_form = CreatePostForm()

    if add_form.validate_on_submit():
        with app.app_context():
            db.session.add(BlogPost(title=add_form.title.data,
                                    subtitle=add_form.subtitle.data,
                                    date=f"{now:%B %d, %Y}",
                                    body=add_form.body.data,
                                    author=add_form.author.data,
                                    img_url=add_form.img_url.data))

            db.session.commit()

            return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=add_form)

# Rota para editar um post.
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    now = dt.datetime.now()
    post = BlogPost.query.get(post_id)

    edit_form = CreatePostForm(title=post.title,
                               subtitle=post.subtitle,
                               img_url=post.img_url,
                               author=post.author,
                               body=post.body)

    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.date = f"{now:%B %d, %Y}"
        post.body = edit_form.body.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data

        db.session.commit()

        return redirect(url_for("show_post", index=post_id))

    return render_template("make-post.html", form=edit_form, is_edit=True)

# Rota para remover um post existente
@app.route("/del-post/<int:index>")
def del_post(index):
    post = BlogPost.query.get(index)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)