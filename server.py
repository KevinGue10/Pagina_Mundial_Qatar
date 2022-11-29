from flask import Flask,render_template,redirect,request,url_for, session,flash
import os
from flask_mysqldb import MySQL
from forms import FormProg,modprog,chspar
from Datos import estd,equiposk,arb,ids,validate,maxid,edits,maxequ
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

@app.route('/Editp', methods=['GET','POST'])
def Edit():
    cur= mysql.connection.cursor()
    form=FormProg()
    est=estd(cur)
    equ=equiposk(cur)
    arbi=arb(cur)
    for i in range (len(est)):
        form.Estadio.choices.append(est[i])
    for i in range (len(equ)):
        form.Equipo1.choices.append(equ[i])
        form.Equipo2.choices.append(equ[i])
    for i in range (len(arbi)):
        form.Arbitro.choices.append(arbi[i])
    msg=''
    if (form.validate_on_submit()):
        Estadio=request.form['Estadio']
        Equipo1=request.form['Equipo1']
        Equipo2=request.form['Equipo2']
        Arbitro=request.form['Arbitro']
        Fecha=request.form['Fecha']
        ID=ids(cur,Estadio,Equipo1,Equipo2,Arbitro)
        vd=validate(cur,ID[3],Equipo1,Equipo2)
        print(vd)
        if (vd==1):
            msg='ERROR: ARBITRO INVALIDO PARA ESTE PARTIDO'
        else: 
            
            cur.execute("Insert INTO Pagina_Mundial.Programacion (idProgramacion,Estadio_prog,id_local,id_visitante,Fecha,Arbitro) VALUES ('"
            +str(ID[4]+1)+"','"+str(ID[0])+"','"+str(ID[1])+"','"+str(ID[2])+"','"+Fecha+"','"+str(ID[3])+"' )")
            mysql.connection.commit()
    return render_template('progc.html',form=form,msg=msg)

@app.route('/modpar', methods=['GET','POST'])
def modpar():
    cur= mysql.connection.cursor()
    form=chspar()
    form2=modprog()
    mid=maxid(cur)
    for i in range (mid):
        form.Partido.choices.append('Partido '+str((i+1)))
    print(form.validate_on_submit())
    if (form.validate_on_submit()):
        Partido=request.form['Partido']
        est=estd(cur)
        equ=equiposk(cur)
        arbi=arb(cur)
        comp=edits(cur,Partido)
        for i in range (len(est)):
            if i==0:
                form2.Estadio.choices.append(est[i])
            else:    
                form2.Estadio.choices.append(est[i])
        for i in range (len(equ)):
            form2.Equipo1.choices.append(equ[i])
            form2.Equipo2.choices.append(equ[i])
        for i in range (len(arbi)):
            form2.Arbitro.choices.append(arbi[i])
        return render_template('progc.html',form=form2,P=1,pr=Partido)
        
    else:
        return render_template('exmodprog.html',form=form)


@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

@app.route('/jugadores')
def jugadores():
    return render_template('jugadores.html')


@app.route('/editequipos')
def edit_equipos():
    return render_template('edit_equipos.html')

@app.route('/editjugadores')
def edit_jugadores():
    return render_template('edit_jugadores.html')

@app.route('/arbitros')
def arbitros():
    return render_template('arbitros.html')

@app.route('/editarbitros')
def edit_arbitros():
    return render_template('edit_arbitros.html')

@app.route('/estadios')
def estadios():
    return render_template('estadios.html')

@app.route('/editestadios')
def edit_estadios():
    return render_template('edit_estadios.html')