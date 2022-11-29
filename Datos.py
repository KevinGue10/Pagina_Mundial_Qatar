from flask_mysqldb import MySQL

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
    print(parb)
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
    
def edits(db,partido):
    db.execute("SELECT e.Nombre_est FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Estadios e Where p.idEstadio_prog=e.idEstadios AND p.idProgramacion="+partido)
    dt=db.fetchone()
    db.execute("SELECT e.Nombre_Equipo FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Equipos_Futbol e Where p.id_local=e.idEquipos_Futbol AND p.idProgramacion="+partido)
    dt1=db.fetchone()
    db.execute("SELECT e.Nombre_Equipo FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Equipos_Futbol e Where p.id_local=e.idEquipos_Futbol AND p.idProgramacion="+partido)
    dt2=db.fetchone()
    db.execute("SELECT Fecha FROM Pagina_Mundial.Programacion  Where  idProgramacion="+partido)
    dt3=db.fetchone()
    db.execute("SELECT a.Nombre_arb FROM Pagina_Mundial.Programacion p, Pagina_Mundial.Arbitros a Where p.Arbitro=a.idarb AND p.idProgramacion="+partido)
    dt4=db.fetchone()

    Datos=[dt[0],dt1[0],dt2[0],dt3[0],dt4[0]]
    return Datos
