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
    form2=FormProg()
    mid=maxid(cur)  
    for i in range (mid):
        form.Partido.choices.append('Partido '+str((i+1)))
    print(form.validate_on_submit())
    if (form.validate_on_submit()):
        Partido=request.form['Partido']
        est=estd(cur)
        arbi=arb(cur)
        equ=equiposk(cur)
        Partido=Partido.split('Partido')
        comp=edits(cur,Partido[1],est,equ,arbi)
        for i in range (len(est)):
            if i==0:
                form2.Estadio.choices.append(est[comp[0]])
            elif i!=comp[0]:  
                form2.Estadio.choices.append(est[i])
        print("Eq1= "+str(comp[1])+" Eq2= "+str(comp[2]))
        for i in range (len(equ)):
            if i==0:
                form2.Equipo1.choices.append(equ[comp[1]])
                form2.Equipo2.choices.append(equ[comp[2]])
            else:
                if i!=comp[1]:
                    form2.Equipo1.choices.append(equ[i]) 
                if i!=comp[2]:
                    form2.Equipo2.choices.append(equ[i])
        for i in range (len(arbi)):
            if i==0:
                form2.Arbitro.choices.append(arbi[comp[3]])
            elif i!=comp[3]:
                form2.Arbitro.choices.append(arbi[i])
        form2.Fecha.data=comp[4]
        if (form2.validate_on_submit()):
            Estadio=request.form2['Estadio']
            Equipo1=request.form2['Equipo1']
            Equipo2=request.form2['Equipo2']
            Arbitro=request.form2['Arbitro']
            Fecha=request.form2['Fecha']
            ID=ids(cur,Estadio,Equipo1,Equipo2,Arbitro)
            vd=validate(cur,ID[3],Equipo1,Equipo2)
            if (vd==1):
                msg='ERROR: ARBITRO INVALIDO PARA ESTE PARTIDO'
            else: 
                
                cur.execute("UPDATE Pagina_Mundial.Programacion Set Estadio_prog = '"+str(ID[0])+"', id_local= '"+str(ID[1])+"' ,id_visitante= '"+
                +str(ID[2])+"', Fecha= '"+Fecha+"', Arbitro= '"++str(ID[3])+"' Where idProgramacion= "+str(Partido[1]))
                mysql.connection.commit()
        return render_template('progc.html',form=form2,P=1,pr=Partido[1])
        
    else:
        return render_template('exmodprog.html',form=form)


@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/equipos', methods=['GET','POST'])
def equipos():
    if request.method=='POST':
        select = request.form.get('group-select')
        print(select)
        cur= mysql.connection.cursor()
        cur.execute("SELECT Nombre_Equipo, Entrenador, Logo FROM Pagina_Mundial.Equipos_Futbol WHERE Grupo='"+select+"'")
        data=cur.fetchall()
        team1=[data[0][0],data[0][1],data[0][2]]
        team2=[data[1][0],data[1][1],data[1][2]]
        team3=[data[2][0],data[2][1],data[2][2]]
        team4=[data[3][0],data[3][1],data[3][2]]
        print(team1)
        print(team2)
        print(team3)
        print(team4)
        mysql.connection.commit()
    # return redirect(url_for('equipos'))
        return render_template('equipos_flask.html', t1=team1, t2=team2, t3=team3, t4=team4)
    else:
        return render_template('equipos.html')

@app.route('/jugadores')
def jugadores():
    return render_template('jugadores.html')

@app.route('/editequipos')
def edit_equipos():
    return render_template('edit_equipos.html')


@app.route('/add_equipo', methods=['GET','POST'])
def add_equipos():
    if request.method=='POST':
        print('entro post')
        nombre_equipo=request.form['nombre_equipo']
        entrenador=request.form['entrenador']
        logo=request.form['logo']
        grupo=request.form['grupo']
        cur= mysql.connection.cursor()
        idq=maxequ(cur)
        cur.execute("Insert INTO Pagina_Mundial.Equipos_Futbol (idEquipos_Futbol,Nombre_Equipo, Entrenador, Logo, Grupo) VALUES ('"
            +str(idq+1)+"','"+nombre_equipo+"','"+entrenador+"','"+logo+"','"+grupo+"')")
        # cur.execute=('INSERT INTO Pagina_Mundial.Equipos_Futbol (Nombre_Equipo, Entrenador, Logo, Grupo) VALUES (%s, %s, %s, %s)',
        # (nombre_equipo, entrenador, logo, grupo))
        mysql.connection.commit()
    return redirect(url_for('edit_equipos'))


@app.route('/select_group_edit', methods=['GET','POST'])
def select_group_edit():
    team1=0
    team2=0
    team3=0
    team4=0
    if request.method=='POST':
        select = request.form.get('group-select')
        print(select)
        cur= mysql.connection.cursor()
        cur.execute("SELECT Nombre_Equipo, Entrenador, Logo FROM Pagina_Mundial.Equipos_Futbol WHERE Grupo='"+str(select)+"'")
        data=cur.fetchall()
        team1=[data[0][0],data[0][1],data[0][2]]
        team2=[data[1][0],data[1][1],data[1][2]]
        team3=[data[2][0],data[2][1],data[2][2]]
        team4=[data[3][0],data[3][1],data[3][2]]
        print(team1)
        print(team2)
        print(team3)
        print(team4)
        mysql.connection.commit()
    # return redirect(url_for('equipos'))
    return render_template('edit_equipos_flask.html', t1=team1, t2=team2, t3=team3, t4=team4)

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