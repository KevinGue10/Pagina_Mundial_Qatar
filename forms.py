from flask_wtf import FlaskForm
from flask import Flask
from wtforms import Form,StringField,SubmitField,SelectField,DateTimeField,IntegerField
from wtforms.validators import DataRequired
class FormProg(FlaskForm):
    
    Estadio=SelectField('Estadio',choices=[])
    Equipo1=SelectField('Equipo_1',choices=[])
    Equipo2=SelectField('Equipo_2',choices=[])
    Arbitro=SelectField('Arbitro',choices=[])
    Fecha=DateTimeField('Fecha_Hora',validators=[DataRequired(message='llene este campo')])
    ingb=SubmitField('Ingresar')

class modprog(FlaskForm):
    Estadio=SelectField('Estadio',choices=[])
    Equipo1=SelectField('Equipo_1',choices=[])
    Equipo2=SelectField('Equipo_2',choices=[])
    Arbitro=SelectField('Arbitro',choices=[])
    Fecha=DateTimeField('Fecha_Hora',validators=[DataRequired(message='llene este campo')])
    ingb=SubmitField('Editar')

class chspar(FlaskForm):
    Partido=SelectField('Partido',choices=[])
    ingb=SubmitField('Editar')

