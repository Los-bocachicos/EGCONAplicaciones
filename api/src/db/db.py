import mysql.connector as mysql

cnx = mysql.MySQLConnection(
    host="127.0.0.1",
    port=3306,
    user="EGC0NAlicaciones",
    password="EGC0NAlicaciones",
    database="evergreen",
    auth_plugin="mysql_native_password"
)
