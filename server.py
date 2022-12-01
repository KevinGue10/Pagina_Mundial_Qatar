from flask import Flask,render_template,redirect,request,url_for, session,flash
import os
from flask_mysqldb import MySQL
from froms import FormProg
from Datos import estd,equiposk,arb,ids,validate
from datetime import datetime
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
    flash("FUNCIONA")
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
    print(form.validate_on_submit())
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

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

@app.route('/jugadores')
def jugadores():
    return render_template('jugadores.html')

@app.route('/modweb')
def modweb():
    dat = datetime.now()
    date = str(dat)
    x = date.split()
    horac = x[1].split(':')
    numhoract = int(horac[0])
    numminact = int(horac[1])
    horact = horac[0]+":"+horac[1]
    cur = mysql.connection.cursor()
    sql = "SELECT Nombre_Equipo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_local=idEquipos_Futbol"
    cur.execute(sql)
    local =cur.fetchall()
    sql = "SELECT idProgramacion FROM Programacion WHERE DATE(Fecha)='"+x[0]+"'"
    cur.execute(sql)
    ids = cur.fetchall()
    sql = "SELECT Nombre_Equipo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_visitante=idEquipos_Futbol"
    cur.execute(sql)
    visitante = cur.fetchall()
    sql = "SELECT Logo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_local=idEquipos_Futbol"
    cur.execute(sql)
    logolocal = cur.fetchall()
    sql = "SELECT Logo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_visitante=idEquipos_Futbol"
    cur.execute(sql)
    logovisitante = cur.fetchall()
    sql = "SELECT TIME(Fecha) FROM Pagina_Mundial.Programacion WHERE DATE(Fecha)='"+x[0]+"'"
    cur.execute(sql)
    hora = cur.fetchall()

    data = {
        "locales": local,
        "ids": ids,
        "visitantes":  visitante,
        "logolocales": logolocal,
        "logovisitantes": logovisitante,
        "hora": hora
    }

    lok = []
    vis = []
    logl = []
    logv = []
    hor = []
    numhor = []
    nummin = []
    idst = []
    for i in data.get('locales'):
        lok.append(i[0])
    for i in data.get('ids'):
        idst.append(i[0])
    for i in data.get('visitantes'):
        vis.append(i[0])
    for i in data.get('logolocales'):
        logl.append(i[0])
    for i in data.get('logovisitantes'):
        logv.append(i[0])
    for i in data.get('hora'):
        a = str(i[0])
        b = a.split(':')
        numhor.append(int(b[0]))
        nummin.append(int(b[1]))
        hor.append(b[0]+":"+b[1])
    numpart = len(lok) 
    golesL = []
    golesV = []
    finpar = []
    print(numhor)
    print(idst)
    for i in range(numpart):
        sql = "SELECT sum(GolL)  FROM Pagina_Mundial.Minuto where id_partido='"+str(idst[i])+"' order by id_partido desc limit 1"
        cur.execute(sql)
        golL = cur.fetchone()
        golesL.append(golL[0])
        sql = "SELECT sum(GolV)  FROM Pagina_Mundial.Minuto where id_partido='"+str(idst[i])+"' order by id_partido desc limit 1"
        cur.execute(sql)
        golV = cur.fetchone()
        golesV.append(golV[0])
        sql = "SELECT sum(FindJu)  FROM Pagina_Mundial.Minuto where id_partido='"+str(idst[i])+"' order by id_partido desc limit 1"
        cur.execute(sql)
        fin = cur.fetchone()
        finpar.append(fin[0])
        print(finpar)
        
    return render_template('modweb.html',x=x[0],local=local,data=data,lok=lok,vis=vis,numminact=numminact,
                            logl=logl,logv=logv,numpart=numpart,hor=hor,horact=horact,numhoract=numhoract,
                            numhor=numhor,golesL=golesL,golesV=golesV,finpar=finpar,nummin=nummin)












@app.route('/estadisticas/<int:partido>')
def estad(partido):
    dat = datetime.now()
    date = str(dat)
    x = date.split()
    horac = x[1].split(':')
    numhoract = int(horac[0])
    numminact = int(horac[1])
    horact = horac[0]+":"+horac[1]
    cur = mysql.connection.cursor()
    sql = "SELECT Nombre_Equipo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_local=idEquipos_Futbol"
    cur.execute(sql)
    local =cur.fetchall()
    sql = "SELECT idProgramacion FROM Programacion WHERE DATE(Fecha)='"+x[0]+"'"
    cur.execute(sql)
    ids = cur.fetchall()
    sql = "SELECT Nombre_Equipo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_visitante=idEquipos_Futbol"
    cur.execute(sql)
    visitante = cur.fetchall()
    sql = "SELECT Logo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_local=idEquipos_Futbol"
    cur.execute(sql)
    logolocal = cur.fetchall()
    sql = "SELECT Logo FROM Equipos_Futbol, Programacion WHERE DATE(Fecha)='"+x[0]+"' AND id_visitante=idEquipos_Futbol"
    cur.execute(sql)
    logovisitante = cur.fetchall()
    sql = "SELECT TIME(Fecha) FROM Pagina_Mundial.Programacion WHERE DATE(Fecha)='"+x[0]+"'"
    cur.execute(sql)
    hora = cur.fetchall()


    data = {
        "locales": local,
        "ids": ids,
        "visitantes":  visitante,
        "logolocales": logolocal,
        "logovisitantes": logovisitante,
        "hora": hora
    }
    

    lok = []
    vis = []
    logl = []
    logv = []
    hor = []
    numhor = []
    nummin = []
    idst = []
    for i in data.get('locales'):
        lok.append(i[0])
    for i in data.get('ids'):
        idst.append(i[0])
    for i in data.get('visitantes'):
        vis.append(i[0])
    for i in data.get('logolocales'):
        logl.append(i[0])
    for i in data.get('logovisitantes'):
        logv.append(i[0])
    for i in data.get('hora'):
        a = str(i[0])
        b = a.split(':')
        numhor.append(int(b[0]))
        nummin.append(int(b[1]))
        hor.append(b[0]+":"+b[1])
    
    numpart = len(lok) 
    golesL = []
    golesV = []
    finpar = []
    remls = []
    remvs = []
    taamt = []
    taamVt = []
    tarot = []
    taroVt = []
    tirodet = []
    tirodeVt = []
    grupos = []
    ird = idst[0]
    print(ird)


    for i in range(numpart):
        print(i)
        sql = "SELECT sum(GolL), sum(GolV), sum(FindJu), sum(Remate), sum(RemateV), sum(TaAm), sum(TaAmV), sum(TaRo), sum(TaRoV), sum(TirodE), sum(TirodEV) FROM Pagina_Mundial.Minuto where id_partido='"+str(idst[i])+"' order by id_partido desc limit 1"
        cur.execute(sql)
        golL = cur.fetchone()
        sql = "SELECT Grupo FROM Equipos_Futbol, Programacion WHERE id_local='"+str(idst[i])+"' AND id_local=idEquipos_Futbol"
        cur.execute(sql)
        grupo = cur.fechone()
        grupos.append(grupo[0])
        golesL.append(golL[0])
        golesV.append(golL[1])
        finpar.append(golL[2])
        remls.append(golL[3])
        remvs.append(golL[4])
        taamt.append(golL[5])
        taamVt.append(golL[6])
        tarot.append(golL[7])
        taroVt.append(golL[8])
        tirodet.append(golL[9])
        tirodeVt.append(golL[10])
        
        

    for i in range(numpart):
        
        if finpar[i]==1:
            sql = "SELECT enday FROM Equipos_Futbol WHERE Nombre_Equipo='"+lok[i]+"'"
            cur.execute(sql)
            enday = cur.fetchone()
            if enday[0] == 0:
                if golesL[i] == None:
                    golesL[i] = 0
                if golesV[i] == None:
                    golesV[i] = 0
                if golesL[i] > golesV[i]:
                    sql = "UPDATE Equipos_Futbol SET Puntos=Puntos+3, enday=enday+1 WHERE Nombre_Equipo='"+lok[i]+"'"
                    cur.execute(sql)
                    mysql.connection.commit()
                    sql = "UPDATE Equipos_Futbol SET enday=enday+1 WHERE Nombre_Equipo='"+vis[i]+"'"
                    cur.execute(sql)
                    mysql.connection.commit()

                elif golesL[i] < golesV[i]:
                    sql = "UPDATE Equipos_Futbol SET Puntos=Puntos+3, enday=enday+1 WHERE Nombre_Equipo='"+vis[i]+"'"
                    cur.execute(sql)
                    mysql.connection.commit()
                    sql = "UPDATE Equipos_Futbol SET enday=enday+1 WHERE Nombre_Equipo='"+lok[i]+"'"
                    cur.execute(sql)
                    mysql.connection.commit()

    sql = "SELECT Minuto, Descrip FROM Minuto where id_partido='"+str(partido+1)+"' order by idMinuto DESC"
    cur.execute(sql)
    desc = cur.fetchone()   
    minuto = desc[0]
    descrip = desc[1]
    
    return render_template('estadisticas.html',x=x[0],local=local,data=data,lok=lok,vis=vis,numminact=numminact,
                            logl=logl,logv=logv,numpart=numpart,hor=hor,horact=horact,numhoract=numhoract,
                            numhor=numhor,golesL=golesL,golesV=golesV,finpar=finpar,nummin=nummin,partido=partido,
                            remls=remls,remvs=remvs,taamt=taamt,taamVt=taamVt,tarot=tarot,taroVt=taroVt,
                            tirodet=tirodet,tirodeVt=tirodeVt,minuto=minuto,descrip=descrip)

@app.route('/tablas/<grupo>')    
def tablas(grupo):
    sql = "SELECT Nombre_Equipo, Puntos FROM Equipos_Futbol WHERE Grupo='"+grupo+"' order by Puntos desc"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    ta = cur.fetchall()
    print(ta)

    return render_template('tablas.html',grupo=grupo)
