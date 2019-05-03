from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AccessForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('ENTER THE LOUNGE')