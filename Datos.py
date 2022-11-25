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

def equipos(db):
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
        db.execute("SELECT Nombre_Equipo FROM Pagina_Mundial.Arbitros where idarb="+str(i+1))
        D=db.fetchone()
        Datos.append(D[0])
    return Datos