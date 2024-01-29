from Conexion import Conexion_bd, Cerrar_conexcion_bd

def conexion_insert():
    conexion = Conexion_bd()
    cursor = conexion.cursor()
    
    return conexion, cursor

def inicio_sesion(usuario, contraseña):
    
    conexion, cursor = conexion_insert()
    
    consulta = "SELECT COUNT(*) FROM tbl_Login WHERE Usuario = %s AND Contraseña = %s"
    cursor.execute(consulta, (usuario, contraseña)) # Ejecutar la consulta
    resultado = cursor.fetchone()       # Obtener solo una fila de resultados
    cursor.close()
    
    Cerrar_conexcion_bd(conexion)
    
    return resultado

def autenticacion(usuario, contraseña):
    conexion, cursor = conexion_insert()
    
    consulta = """
                SELECT U.id_Usuario, U.DNI, CONCAT(U.Nombre, ' ', U.Apellido) AS Nombre_Completo, U.Correo, U.Telefono, R.nombre AS Rol, U.edad, U.Fecha_Nacimiento
                FROM tbl_Login L
                JOIN tbl_Usuario U ON L.id_Usuario = U.id_Usuario
                JOIN tbl_Rol R ON U.id_rol = R.id_Rol
                WHERE L.Usuario = %s AND L.Contraseña = %s;
            """
    cursor.execute(consulta, (usuario, contraseña))
    resultado = cursor.fetchall()   # Vamos a obtener todas las filas de la cunsulta
    
    Cerrar_conexcion_bd(conexion)
    return resultado
    
def Usuario (user_name):
    conexion, cursor = conexion_insert()
    
    consulta = """SELECT U.id_Usuario, R.nombre
                FROM tbl_usuario U
                JOIN tbl_rol R ON U.id_Rol = R.id_Rol
                WHERE CONCAT(U.Nombre, ' ', U.Apellido) = %s"""
                
    cursor.execute(consulta, (user_name,))
    resultado = cursor.fetchone()
    conexion.commit()
    Cerrar_conexcion_bd(conexion)
    
    return resultado