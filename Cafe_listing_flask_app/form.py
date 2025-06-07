from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, URL


coffee_rating_choices = [
    ("✘", "✘"),
    ("☕", "☕"),
    ("☕☕", "☕☕"),
    ("☕☕☕", "☕☕☕"),
    ("☕☕☕☕", "☕☕☕☕"),
    ("☕☕☕☕☕", "☕☕☕☕☕")
]
wifi_rating_choices = [
        ("✘", "✘"),
        ("💪", "💪"),
        ("💪💪", "💪💪"),
        ("💪💪💪", "💪💪💪"),
        ("💪💪💪💪", "💪💪💪💪"),
        ("💪💪💪💪💪", "💪💪💪💪💪")
]

power_rating_choices =[
        ("✘", "✘"),
        ("🔌", "🔌"),
        ("🔌🔌", "🔌🔌"),
        ("🔌🔌🔌", "🔌🔌🔌"),
        ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
        ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")
]
class CafeForm(FlaskForm):
    cafe_name =StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location(Google Maps)', validators=[DataRequired(), URL()])
    open = StringField('Open(Eg: 8:00 AM)', validators=[DataRequired()])
    close = StringField('Close(Eg: 3:00 PM)', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices= coffee_rating_choices,validators=[DataRequired()])
    wifi = SelectField('Wifi',choices= wifi_rating_choices ,validators=[DataRequired()])
    power = SelectField('Power', choices= power_rating_choices,validators=[DataRequired()])
    submit = SubmitField(label='Submit')
