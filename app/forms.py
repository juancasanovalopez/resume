from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class JobPostForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    period = StringField('Period', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('+')