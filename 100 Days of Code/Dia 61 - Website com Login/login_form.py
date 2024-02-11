from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

# Criando uma classe de formulario de login que herda da classe FlaskForm.
class LoginForm(FlaskForm):
    # Cria um campo de entra de texto para o email.
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    # Cria um campo de entrada de texto para a senha.
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    # Cria um botão de envio.
    send_button = SubmitField("Submit")