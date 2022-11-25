from flask_wtf import FlaskForm
from flask import Flask
from wtforms import Form,StringField,SubmitField,SelectField,DateTimeField
from wtforms.validators import DataRequired
class FormProg(FlaskForm):
    
    #Estadio=SelectField('Estadio',choices=[Datos[0],Datos[1],Datos[2]])
    #Equipo1=SelectField('Equipo1',choices=['Qatar','Ecuador'])
    Estadio=StringField('Estadio',validators=[DataRequired(message='llene este campo')])
    Equipo1=StringField('Equipo_1',validators=[DataRequired(message='llene este campo')])
    Equipo2=StringField('Equipo_2',validators=[DataRequired(message='llene este campo')])
    Arbitro=StringField('Arbitro',validators=[DataRequired(message='llene este campo')])
    Fecha=DateTimeField('Fecha_Hora',validators=[DataRequired(message='llene este campo')])
    ingb=SubmitField('Ingresar')
    
 