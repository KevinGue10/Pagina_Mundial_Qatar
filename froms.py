from flask_wtf import FlaskForm
from flask import Flask
from wtforms import Form,StringField,SubmitField,SelectField,DateTimeField
from wtforms.validators import DataRequired
class FormProg(FlaskForm):
    
    Estadio=SelectField('Estadio',choices=[])
    Equipo1=SelectField('Equipo_1',choices=[])
    Equipo2=SelectField('Equipo_2',choices=[])
    Arbitro=StringField('Arbitro',validators=[DataRequired(message='llene este campo')])
    Fecha=DateTimeField('Fecha_Hora',validators=[DataRequired(message='llene este campo')])
    ingb=SubmitField('Ingresar')
    
 