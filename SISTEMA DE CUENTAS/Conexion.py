import mysql.connector

def Conexion_bd():
    try: 
        conexion = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="73600753",
            database="cuentas_usuario",
        )
    except ConnectionError:
        print("No se pudo conectar con la Base de Datos")
    
    return conexion

def Cerrar_conexcion_bd(conexion):
    conexion.close()
