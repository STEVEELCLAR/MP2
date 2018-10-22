from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addForm(FlaskForm):
    id = StringField('ID Number', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    year = StringField('Year Level', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    submit = SubmitField('Enter')


class updForm(FlaskForm):
    id = StringField('Current ID Number', validators=[DataRequired()])
    newid = StringField('New ID Number', validators=[DataRequired()])
    lname = StringField('Current Last Name', validators=[DataRequired()])
    newlname = StringField('New Last Name', validators=[DataRequired()])
    fname = StringField('Current First Name', validators=[DataRequired()])
    newfname = StringField('New First Name', validators=[DataRequired()])
    course = StringField('Current Course', validators=[DataRequired()])
    newcourse = StringField('New Course', validators=[DataRequired()])
    year = StringField('Current Year Level', validators=[DataRequired()])
    newyear = StringField('New Year Level', validators=[DataRequired()])
    gender = StringField('Current Gender', validators=[DataRequired()])
    newgender = StringField('New Gender', validators=[DataRequired()])
    submit = SubmitField('Enter')


