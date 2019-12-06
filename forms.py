from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UploadForm(FlaskForm):
    title = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    content = StringField('Content', validators=[DataRequired(), Length(min=2, max=10000)])
    descriptors = StringField('Descriptors', validators=[DataRequired(), Length(min=2, max=150)])
    submit = SubmitField('Upload')
