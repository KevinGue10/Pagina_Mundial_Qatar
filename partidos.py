from flask_mysqldb import MySQL
import datetime

current_time=datetime.datetime.now().replace(microsecond=0)

def get_Fecha(db):    
    fecha=""
    db.execute("SELECT Fecha_Hora FROM Pagina_Mundial.Programacion ORDER BY Fecha_Hora")
    fecha = db.fetchone()
    return fecha

def get_Local(db):    
    fecha=""
    db.execute("SELECT Fecha_Hora FROM Pagina_Mundial.Programacion ORDER BY Fecha_Hora")
    fecha = db.fetchone()
    return fecha