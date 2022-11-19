import mysql.connector
conexion=mysql.connector.connect(user='admin',password='Arrozycarne21',host='database-1.cjwljy7vi4kw.us-east-1.rds.amazonaws.com',database='Pagina_Mundial')

cur=conexion.cursor()