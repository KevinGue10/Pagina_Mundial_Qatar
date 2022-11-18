from flask import Flask,render_template,redirect,request,url_for, session,flash
import os
app=Flask(__name__)
app.secret_key=os.urandom(24)


@app.route("/home")
@app.route("/index")
@app.route('/')
def index():
    return render_template('Pagina_inicial.html')


