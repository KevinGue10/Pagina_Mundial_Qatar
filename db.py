from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app=Flask(__name__)
app.config["MYSQL_HOST"] ='database-1.cjwljy7vi4kw.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Arrozycarne21'
app.config['MYSQL_DB'] = 'Pagina_Mundial' 
mysql = MySQL(app)
def connect():

  
    cursor = mysql.connection.cursor()
    return cursor
