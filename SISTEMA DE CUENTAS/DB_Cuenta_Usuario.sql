CREATE DATABASE Cuentas_Usuario;
USE Cuentas_Usuario;

CREATE TABLE tbl_Rol (
    id_Rol INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre ENUM('ADMINISTRADOR', 'ESTANDAR') NOT NULL
);

CREATE TABLE tbl_Usuario (
    id_Usuario INT NOT NULL AUTO_INCREMENT,
    DNI VARCHAR(8) NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) NOT NULL,
    Telefono VARCHAR(9) NOT NULL,
    id_Rol INT NOT NULL,
    Edad INT,
    Fecha_Nacimiento DATE,
    PRIMARY KEY (id_Usuario),
    FOREIGN KEY (id_Rol) REFERENCES tbl_Rol(id_Rol)
);

CREATE TABLE  tbl_Cuenta (
    id_Cuenta INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Alias_Cuenta varchar(50) not null,
    Usuario varchar(50) not null,
    Contraseña varchar(30) not null,
    Tipo_Cuenta varchar(50) not null,
    Telefono varchar (9),
    Descripcion varchar(100),
    id_Usuario INT NOT NULL,
    Link varchar(200),
    FOREIGN KEY (id_Usuario) REFERENCES tbl_Usuario(id_Usuario) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE tbl_Login (
    id_Login INT NOT NULL AUTO_INCREMENT,
    id_Usuario INT NOT NULL,
    Usuario  VARCHAR(50) NOT NULL,
    Contraseña VARCHAR(60) NOT NULL, -- Se almacenará la contraseña de manera encriptada
	PRIMARY KEY (id_Login),
    FOREIGN KEY (id_Usuario) REFERENCES tbl_Usuario(id_Usuario) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE tbl_InicioSesion (
    id_Inicio_Sesion INT NOT NULL AUTO_INCREMENT,
    id_Usuario INT NOT NULL,
    Hora_Inicio DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    Hora_Cierre DATETIME,
    Exitoso BOOLEAN NOT NULL,
    Duracion TIME,    
    PRIMARY KEY (id_Inicio_Sesion),
    FOREIGN KEY (id_Usuario) REFERENCES tbl_Usuario(id_Usuario)
);

CREATE TABLE tbl_Reportes (
    id_Reporte INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    Tipo_Reporte ENUM('CUENTA', 'USUARIO') NOT NULL,
    Fecha_Creacion DATETIME,
    Documento TEXT,
    Nombre_Documento VARCHAR(100), -- Columna para almacenar el nombre del documento
    id_Usuario INT NOT NULL,
    PRIMARY KEY (id_Reporte),
    FOREIGN KEY (id_Usuario) REFERENCES tbl_Usuario(id_Usuario)
);

CREATE TABLE tbl_Auditoria (
    id_Auditoria INT NOT NULL AUTO_INCREMENT,
    Fecha_Hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Tabla_Afectada VARCHAR(50) NOT NULL,
    Accion_Realizada ENUM('EDITAR', 'ACTUALIZAR', 'ELIMINAR', 'CREAR') NOT NULL,
    id_Usuario INT,
    PRIMARY KEY (id_Auditoria),
    FOREIGN KEY (id_Usuario) REFERENCES tbl_Usuario(id_Usuario) ON DELETE SET NULL
);

CREATE TABLE tbl_Historial_Contrasenas (
    id_Historial INT NOT NULL AUTO_INCREMENT,
    id_Login INT,
    Contraseña_Anterior VARCHAR(60) NOT NULL,
    Fecha_Cambio DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (id_Historial),
    FOREIGN KEY (id_Login) REFERENCES tbl_Login(id_Login) ON DELETE CASCADE
);
