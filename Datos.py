from flask_mysqldb import MySQL
from datetime import datetime, timedelta

def estd(db):
    Datos=['']
    db.execute("SELECT Nombre_est FROM Pagina_Mundial.Estadios")
    x=len(db.fetchall())
    for i in range (x):
        db.execute("SELECT Nombre_est FROM Pagina_Mundial.Estadios where idEstadios="+str(i+1))
        D=db.fetchone()
        Datos.append(D[0])
    return Datos

def equiposk(db):
    Datos=['']
    db.execute("SELECT Nombre_Equipo FROM Pagina_Mundial.Equipos_Futbol")
    Datos=['']
    x=len(db.fetchall())
    for i in range (x):
        db.execute("SELECT Nombre_Equipo FROM Pagina_Mundial.Equipos_Futbol where idEquipos_Futbol="+str(i+1))
        D=db.fetchone()
        Datos.append(D[0])
    return Datos
    
def arb(db):
    Datos=['']
    db.execute("SELECT Nombre_arb FROM Pagina_Mundial.Arbitros")
    x=len(db.fetchall())
    for i in range (x):
        db.execute("SELECT Nombre_arb FROM Pagina_Mundial.Arbitros where idarb="+str(i+1))
        D=db.fetchone()
        Datos.append(D[0])
    return Datos


def ids(db,Estadio,E1,E2,Ar):
    db.execute("SELECT idEstadios FROM Pagina_Mundial.Estadios where Nombre_est= '"+Estadio+"'")
    Est=db.fetchone()
    db.execute("SELECT idEquipos_Futbol FROM Pagina_Mundial.Equipos_Futbol where Nombre_Equipo= '"+E1+"'")
    Eq1=db.fetchone()
    db.execute("SELECT idEquipos_Futbol FROM Pagina_Mundial.Equipos_Futbol where Nombre_Equipo= '"+E2+"'")
    Eq2=db.fetchone()
    db.execute("SELECT idarb FROM Pagina_Mundial.Arbitros where Nombre_arb= '"+Ar+"'")
    arb=db.fetchone()
    db.execute("SELECT max(idProgramacion) FROM Pagina_Mundial.Programacion")
    idp=db.fetchone()
    info=[Est[0],Eq1[0],Eq2[0],arb[0],idp[0]]
    return info
   

def validate(db,ida,E1,E2):
    db.execute("Select Procedencia FROM Pagina_Mundial.Arbitros where idarb= "+str(ida))
    parb=db.fetchone()
    if(parb[0]==E1 or parb[0]==E2):
        return 1
    else:
        return 0

def maxid(db):
    db.execute("SELECT max(idProgramacion) FROM Pagina_Mundial.Programacion")
    mid=db.fetchone()
    return mid[0]

def maxequ(db):
    db.execute("SELECT max(idEquipos_Futbol) FROM Pagina_Mundial.Equipos_Futbol")
    mid=db.fetchone()
    return mid[0]
def maxida(db):
    db.execute("SELECT max(idarb) FROM Pagina_Mundial.Arbitros")
    mid=db.fetchone()
    return mid[0]
def maxest(db):
    db.execute("SELECT max(idEstadios) FROM Pagina_Mundial.Estadios")
    mid=db.fetchone()
    return mid[0]
def maxj(db):
    db.execute("SELECT max(id_jugador) FROM Pagina_Mundial.Jugadores_Eq")
    mid=db.fetchone()
    return mid[0]
    
def edits(db,partido,est,equ,arbi):
    print(partido)
    db.execute("SELECT e.Nombre_est FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Estadios e Where p.Estadio_prog=e.idEstadios AND p.idProgramacion="+partido)
    dt=db.fetchone()
    db.execute("SELECT e.Nombre_Equipo FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Equipos_Futbol e Where p.id_local=e.idEquipos_Futbol AND p.idProgramacion="+partido)
    dt1=db.fetchone()
    db.execute("SELECT e.Nombre_Equipo FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Equipos_Futbol e Where p.id_visitante=e.idEquipos_Futbol AND p.idProgramacion="+partido)
    dt2=db.fetchone()
    db.execute("SELECT Fecha FROM Pagina_Mundial.Programacion  Where  idProgramacion="+partido)
    dt3=db.fetchone()
    db.execute("SELECT a.Nombre_arb FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Arbitros a Where p.Arbitro=a.idarb AND p.idProgramacion="+partido)
    dt4=db.fetchone()
    print("Equip1= "+str(dt1[0])+ " Equip2= "+str(dt2[0]))
    for i in range (len(est)): 
            if est[i]==dt[0]:
                d1=i
    for i in range (len(equ)):
        if equ[i]==dt1[0]:
            d2=i
        if equ[i]==dt2[0]:
            d3=i
    for i in range (len(arbi)):
        if arbi[i]==dt4[0]:
            d4=i

    Datos=[d1,d2,d3,d4,dt3[0]]
    return Datos

def ctime():
    now = datetime.now().replace(microsecond=0).replace(second=0)
    nowm2= now - timedelta(hours=2)
    now2 = now + timedelta(hours=2)
    horas=[nowm2,now2]
    return horas

def getlocal(db):
    # db.execute("SELECT e.Logo, e.Nombre_Equipo FROM Equipos_Futbol e, Programacion p WHERE e.idEquipos_Futbol=p.id_local AND p.Fecha BETWEEN '"+horas[0]+"' AND '"+horas[1]+"'")
    db.execute("SELECT e.Logo, e.Nombre_Equipo, p.Fecha,p.idProgramacion FROM Equipos_Futbol e, Programacion p WHERE e.idEquipos_Futbol=p.id_local AND p.Fecha BETWEEN '2020-11-30 08:50:00' AND '2020-11-30 11:00:00'")
    data=db.fetchall()
    if len(data)==0:
        datos=[0,0,0,0]
    else:
        datos=[data[0][0],data[0][1],data[0][2],data[0][3]]
    return datos

def getvisitante(db):
    # db.execute("SELECT e.Logo, e.Nombre_Equipo FROM Equipos_Futbol e, Programacion p WHERE e.idEquipos_Futbol=p.id_local AND p.Fecha BETWEEN '"+horas[0]+"' AND '"+horas[1]+"'")
    db.execute("SELECT e.Logo, e.Nombre_Equipo FROM Equipos_Futbol e, Programacion p WHERE e.idEquipos_Futbol=p.id_visitante AND p.Fecha BETWEEN '2022-11-30 08:50:00' AND '2022-11-30 11:00:00'")
    data=db.fetchall()
    if len(data)==0:
        datos=[0,0,0,0]
    else:
        datos=[data[0][0],data[0][1]]
    return datos

def maxidparti(db):
    db.execute("SELECT max(idMinuto) FROM Pagina_Mundial.Minuto")
    mid=db.fetchone()
    return mid[0]

def stats(db):
    db.execute("SELECT GolL,GolV,Remate,RemateV,TaAm,TaAmV,TaRo,TaRoV,TirodE,TirodEV,FindJu FROM Minuto ORDER BY idMinuto DESC LIMIT 1")
    data=db.fetchall()
    datos=[data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10]]
    return datos
    
def noPaLocal(db):
    db.execute("SELECT e.Logo, e.Nombre_Equipo, p.Fecha FROM Minuto m, Programacion p, Equipos_Futbol e WHERE m.id_partido=p.idProgramacion AND e.idEquipos_Futbol=p.id_local ORDER BY idMinuto DESC LIMIT 1")
    data=db.fetchall()
    datos=[data[0][0],data[0][1],data[0][2]]
    return datos

def noPaVis(db):
    db.execute("SELECT e.Logo, e.Nombre_Equipo, p.Fecha FROM Minuto m, Programacion p, Equipos_Futbol e WHERE m.id_partido=p.idProgramacion AND e.idEquipos_Futbol=p.id_visitante ORDER BY idMinuto DESC LIMIT 1")
    data=db.fetchall()
    datos=[data[0][0],data[0][1],data[0][2]]
    return datos