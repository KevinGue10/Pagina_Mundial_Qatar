from flask import Flask,render_template,redirect,request,url_for, session,flash
import os
from froms import FormProg
app=Flask(__name__)
app.secret_key=os.urandom(24)


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
    form=FormProg()
    if (form.validate_on_submit()):
        Estadio=request.form['Estadio']
        Equipo1=request.form[' Equipo1']
        Equipo2=request.form['Equipo2']
        Arbitro=request.form['Arbitro']
        Fecha=request.form['Fecha']

    return render_template('progc.html',form=form)

