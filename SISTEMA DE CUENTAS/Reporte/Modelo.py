from Conexion import Conexion_bd, Cerrar_conexcion_bd

def Conexion_Insert():
    conexion = Conexion_bd()
    cursor = conexion.cursor()
    
    return conexion, cursor
    
def reporte_cuenta(dni, fecha_inicio, fecha_fin, rol, id_user):
    conexion, cursor = Conexion_Insert()
    
    # Definir los parámetros
    parametros = {
        'tu_dni': dni,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    }
    
    if rol == "ADMINISTRADOR":
        consulta = """
            SELECT C.id_Cuenta, C.Usuario, C.Contraseña, C.Tipo_Cuenta, U.Nombre AS Dueño, C.Descripcion, C.Link, C.Fecha_creacion
            FROM tbl_cuenta C
            LEFT JOIN tbl_usuario U ON C.id_Usuario = U.id_Usuario
            WHERE (U.DNI = COALESCE(%(tu_dni)s, U.DNI) OR %(tu_dni)s IS NULL OR %(tu_dni)s = '')
            AND ((C.Fecha_creacion BETWEEN COALESCE(%(fecha_inicio)s, '1970-01-01') AND COALESCE(%(fecha_fin)s, CURRENT_DATE()))
                OR (%(fecha_inicio)s IS NULL AND %(fecha_fin)s IS NULL OR (%(fecha_inicio)s = '' AND %(fecha_fin)s = '')))
        """
        cursor.execute(consulta, parametros)
            
    elif rol == "ESTANDAR":
        consulta = """
            SELECT C.id_Cuenta, C.Usuario, C.Contraseña, C.Tipo_Cuenta, U.Nombre AS Dueño, C.Descripcion, C.Link, C.Fecha_creacion
            FROM tbl_cuenta C
            LEFT JOIN tbl_usuario U ON C.id_Usuario = U.id_Usuario
            WHERE (U.DNI = COALESCE(%(tu_dni)s, U.DNI) OR %(tu_dni)s IS NULL OR %(tu_dni)s = '')
            AND ((C.Fecha_creacion BETWEEN COALESCE(%(fecha_inicio)s, '1970-01-01') AND COALESCE(%(fecha_fin)s, CURRENT_DATE()))
                OR (%(fecha_inicio)s IS NULL AND %(fecha_fin)s IS NULL OR (%(fecha_inicio)s = '' AND %(fecha_fin)s = '')))
            AND (U.id_Usuario = COALESCE(%(id_user)s, U.id_Usuario))
        """
        parametros['id_user'] = id_user
        cursor.execute(consulta, parametros)
    
    resultado = cursor.fetchall()
    conexion.commit()
    
    Cerrar_conexcion_bd(conexion)
    
    return resultado

def reporte_usuario(dni, fecha_inicio, fecha_fin):
    conexion, cursor = Conexion_Insert()
    
    # Definir los parámetros
    parametros = {
        'tu_dni': dni,  # Reemplaza con el valor deseado
        'fecha_inicio': fecha_inicio,  # Reemplaza con el valor deseado
        'fecha_fin': fecha_fin  # Reemplaza con el valor deseado
    }
    
    consulta = """
                SELECT U.id_Usuario, U.DNI, CONCAT( U.Nombre,' ',U.Apellido) AS NOMBRE_COMPLETO, 
                U.Correo, U.Telefono, R.nombre, U.Edad, U.Fecha_Nacimiento,
                L.Usuario, L.Contraseña
                FROM tbl_usuario U
                LEFT JOIN tbl_rol R ON U.id_Rol = R.id_Rol
                LEFT JOIN tbl_login L ON U.id_Usuario = L.id_Usuario
                WHERE (U.DNI = COALESCE(%(tu_dni)s, U.DNI) OR %(tu_dni)s IS NULL OR %(tu_dni)s = '')
                AND ((U.Fecha_creacion BETWEEN COALESCE(%(fecha_inicio)s, '1970-01-01') AND COALESCE(%(fecha_fin)s, CURRENT_DATE()))
                    OR (%(fecha_inicio)s IS NULL AND %(fecha_fin)s IS NULL OR (%(fecha_inicio)s = '' AND %(fecha_fin)s = '')))
                """
    cursor.execute(consulta, (parametros))
    resultado = cursor.fetchall()
    conexion.commit()
    
    Cerrar_conexcion_bd(conexion)
    return  resultado

def insert_reporte(tipo_reporte, nombre_document, id_user, documento):
    
    conexion, cursor = Conexion_Insert()
    
    consulta = """INSERT INTO tbl_reportes (Tipo_Reporte, Nombre_Documento, id_Usuario, Documento) 
                VALUES (%s, %s, %s, %s)"""
                
    cursor.execute(consulta, (tipo_reporte, nombre_document, id_user, documento))
    conexion.commit()
    Cerrar_conexcion_bd(conexion)