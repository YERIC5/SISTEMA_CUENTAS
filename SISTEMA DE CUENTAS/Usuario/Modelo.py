from Conexion import Conexion_bd, Cerrar_conexcion_bd

def Conexion_insert():
    conexion = Conexion_bd()
    cursor = conexion.cursor()
    
    return conexion, cursor

def existe_user(dni):
    conexion, cursor = Conexion_insert()
    userExiste = False
    
    consulta = "SELECT * FROM tbl_Usuario WHERE `DNI` = %s;"
    conexion.commit()    # Realizar el commit de la transacción            
    cursor.execute(consulta, (dni,))
    resultado = cursor.fetchone()
    
    Cerrar_conexcion_bd(conexion)
    
    if resultado:
        userExiste = True
        return userExiste # Si existe
    
    else:
        return userExiste # No existe

def obtener_datos_users():
    conexion, cursor = Conexion_insert()
    
    consulta = """SELECT U.id_Usuario, U.DNI, CONCAT(U.Nombre, ' ', U.Apellido) AS Nombre_Completo, U.Correo
                    FROM tbl_Usuario U"""
    
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    conexion.commit()    
    Cerrar_conexcion_bd(conexion)
    return resultado
    
def create_user(dni, nombre, apellido, email, telef, idRol, edad, fechaNaci, user, contraseña):
    conexion, cursor = Conexion_insert()
    
    Existe = existe_user(dni)
    
    if Existe:
        return f"Usuario: {dni} ya Existe".upper(), "#FF0707", True
    
    else:
        consulta_usuario = """INSERT INTO tbl_Usuario (DNI, Nombre, Apellido, Correo, Telefono, id_rol, edad, Fecha_Nacimiento) 
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                        
        consulta_login = """INSERT INTO tbl_Login (id_Usuario, Usuario, Contraseña) 
                            VALUES (%s, %s, %s)"""
                            
        # Insertar en tbl_Usuario y tbl_Login
        cursor.execute(consulta_usuario, (dni, nombre, apellido, email, telef, idRol, edad, fechaNaci))
        id_usuario_insertado = cursor.lastrowid     # Obtener el ID del usuario insertado
        cursor.execute(consulta_login, (id_usuario_insertado, user, contraseña))
        
        conexion.commit()    # Realizar el commit de la transacción
        Cerrar_conexcion_bd(conexion)
        return f"Usuario: {nombre} registrado satisfactoriamente".upper(), "#2F80DF", False
        
def read_user(dni): # Leer datos
    
    conexion, cursor = Conexion_insert()
    
    Existe = existe_user(dni)
    
    if Existe:
        consulta = """SELECT U.id_Usuario, U.Nombre, U.Apellido, U.Correo, U.Telefono, R.nombre AS Rol, U.Edad, U.Fecha_Nacimiento, L.Usuario, L.Contraseña
                    FROM tbl_login L
                    JOIN tbl_usuario U ON L.id_Usuario = U.id_Usuario
                    JOIN tbl_Rol R ON U.id_rol = R.id_Rol
                    WHERE U.DNI = %s"""
                    
        cursor.execute(consulta, (dni,))
        resultado = cursor.fetchone()
        conexion.commit()    # Realizar el commit de la transacción
        
        Cerrar_conexcion_bd(conexion)
        return resultado

def update_user(dni, nombre, apellido, email, telef, edad, fechaNaci):
    conexion, cursor = Conexion_insert()
    
    Existe = existe_user(dni)
    
    if Existe:
        consulta = """UPDATE tbl_Usuario 
                    SET Nombre = %s, Apellido = %s, Correo = %s, Telefono = %s, Edad = %s, Fecha_Nacimiento = %s
                    WHERE DNI = %s"""
                    
        cursor.execute(consulta, (nombre, apellido, email, telef, edad, fechaNaci, dni))
        conexion.commit()    # Realizar el commit de la transacción
        Cerrar_conexcion_bd(conexion)
        
        return f"Datos del Usuario: {nombre} actualizado".upper(), "#2F80DF"
    else:
        return f"Usuario {dni} no Existe".upper(), "#FF0707"
    
def delete_user(dni):
    conexion, cursor = Conexion_insert()
    
    Existe = existe_user(dni)
    
    if Existe:
        consulta = """DELETE FROM tbl_Usuario 
                    WHERE DNI = %s"""
                    
        cursor.execute(consulta, (dni,))
        conexion.commit()    # Realizar el commit de la transacción
        Cerrar_conexcion_bd(conexion)
        
        return f"Usuario: {dni} Eliminado".upper(), "#2F80DF"
    else:
        return f"Usuario: {dni} no Existe".upper(), "#FF0707"