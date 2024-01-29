from Conexion import Conexion_bd, Cerrar_conexcion_bd

def Conexion_insert():
    conexion = Conexion_bd()
    cursor = conexion.cursor()
    
    return conexion, cursor

def existe_cuenta(id):
    conexion, cursor = Conexion_insert()
    cuentaExiste = False
    
    consulta = "SELECT id_Cuenta FROM tbl_cuenta WHERE id_Cuenta = %s"
    conexion.commit()    # Realizar el commit de la transacción            
    cursor.execute(consulta, (id,))
    resultado = cursor.fetchone()
    
    Cerrar_conexcion_bd(conexion)
    
    if resultado:
        cuentaExiste = True
        return cuentaExiste # Si existe
    
    else:
        return cuentaExiste # No existe
    
def obtener_datos_cuenta(id_user, tipo_user):
    conexion, cursor = Conexion_insert()
    
    if tipo_user == "ESTANDAR":
        consulta = """SELECT C.id_Cuenta, C.Usuario, C.tipo_cuenta, C.descripcion
                    FROM tbl_cuenta C
                    JOIN tbl_usuario U ON C.id_Usuario = U.id_Usuario
                    WHERE U.id_Usuario = %s
                    """
        cursor.execute(consulta, (id_user,))
    elif tipo_user == "ADMINISTRADOR":
        consulta = """SELECT C.id_Cuenta, C.Usuario, C.tipo_cuenta, C.descripcion FROM tbl_cuenta C"""
        cursor.execute(consulta)
    
    resultado = cursor.fetchall()
    conexion.commit()    
    Cerrar_conexcion_bd(conexion)
    return resultado
    
def create_cuenta(alias, user, contra, tipo_cuenta, telef, descrip, id_user, url):
    conexion, cursor = Conexion_insert()
    
    consulta = """INSERT INTO tbl_Cuenta (Alias_Cuenta, Usuario, Contraseña, Tipo_Cuenta, Telefono, Descripcion, id_Usuario, Link) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    # Insertar en tbl_Usuario y tbl_Login
    cursor.execute(consulta, (alias, user, contra, tipo_cuenta, telef, descrip, id_user, url))
    
    # Obtener el ID del último registro insertado
    id_cuenta = cursor.lastrowid
    
    conexion.commit()    # Realizar el commit de la transacción
    Cerrar_conexcion_bd(conexion)
    return f"Cuenta: {tipo_cuenta} registrado satisfactoriamente".upper(), "#2F80DF", id_cuenta
    
def read_cuenta(id): # Leer datos
    
    conexion, cursor = Conexion_insert()
    
    Existe = existe_cuenta(id)
    
    if Existe:
        consulta = """SELECT * FROM tbl_Cuenta WHERE id_Cuenta = %s"""
                    
        cursor.execute(consulta, (id,))
        resultado = cursor.fetchone()
        conexion.commit()    # Realizar el commit de la transacción
        
        Cerrar_conexcion_bd(conexion)
        return resultado

def update_cuenta(id, alias, contra, telef, descrip, url):
    conexion, cursor = Conexion_insert()
    
    Existe = existe_cuenta(id)
    
    if Existe:
        consulta = """UPDATE tbl_Cuenta
                    SET Alias_Cuenta = %s, Contraseña = %s, Telefono = %s, Descripcion = %s, Link = %s
                    WHERE id_Cuenta = %s"""
                    
        cursor.execute(consulta, (alias, contra, telef, descrip, url, id))
        conexion.commit()    # Realizar el commit de la transacción
        Cerrar_conexcion_bd(conexion)
        
        return f"Datos de la Cuenta: {id} actualizado".upper(), "#2F80DF"
    else:
        return f"Cuenta {id} no Existe".upper(), "#FF0707"
    
def delete_cuenta(id):
    conexion, cursor = Conexion_insert()
    
    Existe = existe_cuenta(id)
    
    if Existe:
        consulta = """DELETE FROM tbl_Cuenta
                    WHERE id_Cuenta = %s"""
                    
        cursor.execute(consulta, (id,))
        conexion.commit()    # Realizar el commit de la transacción
        Cerrar_conexcion_bd(conexion)
        
        return f"Cuenta: {id} Eliminado".upper(), "#2F80DF"
    else:
        return f"Cuenta: {id} no Existe".upper(), "#FF0707"    