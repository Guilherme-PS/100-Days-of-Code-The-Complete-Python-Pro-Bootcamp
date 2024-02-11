from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class RateMovieForm(FlaskForm):
    rating = FloatField("New Rating", validators=[DataRequired()])
    review = StringField("New Review", validators=[DataRequired()])
    edit_button = SubmitField()

class AddMovie(FlaskForm):
    name = StringField("Movie Title", validators=[DataRequired()])
    add_button = SubmitField()