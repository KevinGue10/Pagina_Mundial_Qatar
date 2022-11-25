from flask import Flask,render_template,redirect,request,url_for, session,flash
import os
from flask_mysqldb import MySQL
from froms import FormProg
from db import connect

app=Flask(__name__)
app.secret_key=os.urandom(24)

app.config["MYSQL_HOST"] ='database-1.cjwljy7vi4kw.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Arrozycarne21'
app.config['MYSQL_DB'] = 'Pagina_Mundial' 
mysql= MySQL(app)


@app.route("/home")
@app.route("/index")
@app.route('/')
def index():
    return render_template('Pagina_inicial.html')


@app.route('/Programacion')
def program():
    return render_template('program.html')

@app.route('/Editp')
def Edit():
    cursor = mysql.connection.cursor()
    form=FormProg()
    if (form.validate_on_submit()):
        Estadio=request.form['Estadio']
        Equipo1=request.form[' Equipo1']
        Equipo2=request.form['Equipo2']
        Arbitro=request.form['Arbitro']
        Fecha=request.form['Fecha']
        query="Insert into Pagina_Mundial.Programacion (Estadio_prog,Partido,Fecha-Hora,Arbitro) VALUES "
    return render_template('progc.html',form=form)

