import mysql.connector as mysql
import os

cnx = mysql.MySQLConnection(
    host="127.0.0.1",
    port=3306,
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'],
    database="evergreen",
    auth_plugin="mysql_native_password"
)
