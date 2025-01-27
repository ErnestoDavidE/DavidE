# Para descargar el conector con la BD es necesario
# pip install mysql-connector-python

import mysql.connector
class Conexion:

   def ConexionBaseDeDatos():
    try:
        conexion = mysql.connector.connect(user='root',password='hola123*',
                                               host='127.0.0.1',
                                               database='clientesbd',
                                               port='3306')
        print("Conexión Correcta")

        return conexion
        
    except mysql.connector.Error as error:
        print("Error al conectarte a la BD {}".format(error))

        return conexion
        
   ConexionBaseDeDatos()