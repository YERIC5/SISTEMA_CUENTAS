from tkinter import END

from mysql.connector import Error
from Usuario.Modelo import existe_user, create_user, read_user, update_user, delete_user, obtener_datos_users
from datetime import datetime

class Usuario:
    def __init__(self, vistaU, user_name):
        self.vistU = vistaU
        self.ventana_usuario = vistaU.masterU
        
        self.formatoFecha="%Y-%m-%d"
        self.admi = "ADMINISTRADOR"
        self.estand = "ESTANDAR"
        
        self.datosUser = None
        
        self.btns_Inicio, self.btns_Crear, self.btns_Read, self.btns_Update, self.btns_Cancelar_Guardar = self.Accion_Botones()
        
    def Accion_Botones(self):
        def btns_Inicio():
            self.vistU.btn_Ucancelar.config(state="disabled")
            self.vistU.btn_Uguardar.config(state="disabled")
            self.vistU.btn_Ueliminar.config(state="disabled")
            self.vistU.btn_Ueditar.config(state="disabled")
            self.vistU.btn_Ucalendario.config(state="disabled")
            self.vistU.btn_Ubuscar.config(state="normal")
            self.vistU.btn_Ucrear.config(state="normal")
            
        def btns_para_Crear():
            #Habilitamos Botones
            self.vistU.btn_Ucrear.config(state="normal")
            self.vistU.btn_Ucancelar.config(state="normal")
            self.vistU.btn_Uguardar.config(state="normal")
            self.vistU.btn_Ucalendario.config(state="normal")
            
            #Desabilitamos Botones
            self.vistU.btn_Ueliminar.config(state="disabled")
            self.vistU.btn_Ueditar.config(state="disabled")
            self.vistU.btn_Ubuscar.config(state="disabled")
            
        def btns_para_Update():
            # HABILITAMOS BOTONES
            self.vistU.btn_Ueditar.config(state="normal")
            self.vistU.btn_Ucancelar.config(state="normal")
            self.vistU.btn_Uguardar.config(state="normal")
            
            # DESHABILITAMOS BOTONES
            self.vistU.btn_Ueliminar.config(state="disabled")
            self.vistU.btn_Ucrear.config(state="disabled")
            self.vistU.btn_Ubuscar.config(state="disabled")
            
        def btns_para_Read():
            self.vistU.btn_Ueliminar.config(state="normal")
            self.vistU.btn_Ueditar.config(state="normal")
            self.vistU.btn_Ubuscar.config(state="normal")
            
        def btns_para_Cancelar_Guardar():
            # PARA CREAR Y ACTUALIZAR
            btns_Inicio()
            self.vistU.btn_Ueditar.config(state="normal")
            self.vistU.btn_Ueliminar.config(state="normal")
        
        return btns_Inicio, btns_para_Crear, btns_para_Read, btns_para_Update, btns_para_Cancelar_Guardar
        
    def validar_edad(self, edad):
        if not edad.strip():  # Verifica si la variable está vacía o contiene una cadena
            return None
        elif int(edad) < 0 or int(edad) > 100:
            self.vistU.label_Umensaje.config(text="Edad Incorrecto".upper(), fg="#FF0707")
            return False
        else:
            return edad
        
    def validar_fecha(self, fecha):
        if not fecha.strip():  # Verifica si la variable está vacía o contiene una cadena
            return None
        try:
            datetime.strptime(fecha, self.formatoFecha)
            return fecha
        except ValueError:
            self.vistU.entry_Ufech_naci.delete(0, END)
            self.vistU.label_Umensaje.config(text="El formato de la fecha no es válido ('YYYY-MM-DD').".upper(), fg="#FF0707")
            return False
        
    def obtener_dato(self):
        result_Usuarios = obtener_datos_users()
        # Limpiar TreeView antes de agregar nuevos datos
        for record in self.vistU.tbl_usuario.get_children():
            self.vistU.tbl_usuario.delete(record)
        
        # Agregar datos al TreeView desde la lista de datos
        for dato in result_Usuarios:
            self.vistU.tbl_usuario.insert("", "end", values=dato)
        
    def manejar_estado_campos(self, campos, estado):
        for campo in campos:
            campo.config(state=estado)
        
    def activar_campos(self):
        campos_a_activar = [
            self.vistU.entry_Udni,
            self.vistU.entry_Unombre,
            self.vistU.entry_Uapellido,
            self.vistU.entry_Uemail,
            self.vistU.entry_Utelefono,
            self.vistU.combox_Urol,
            self.vistU.combox_Uedad,
            self.vistU.entry_Ufech_naci,
            self.vistU.entry_Uusuario,
            self.vistU.entry_Ucontra
        ]
        self.manejar_estado_campos(campos_a_activar, "normal")
        for campo in campos_a_activar:
            campo.delete(0, END)
        
    def desactivar_campos(self):
        campos_a_desactivar = [
            self.vistU.entry_Unombre,
            self.vistU.entry_Uapellido,
            self.vistU.entry_Uemail,
            self.vistU.entry_Utelefono,
            self.vistU.combox_Urol,
            self.vistU.combox_Uedad,
            self.vistU.entry_Ufech_naci,
            self.vistU.entry_Uusuario,
            self.vistU.entry_Ucontra
        ]
        self.manejar_estado_campos(campos_a_desactivar, "disabled")
        self.vistU.entry_Udni.config(state="normal")
        
        self.btns_Inicio()
        
    def ocultar_mensaje(self):
        self.vistU.label_Umensaje.config(text="")
        
    def create(self):
        self.activar_campos()
        self.btns_Crear()
        
    def read(self):
        dni = self.vistU.entry_Udni.get()
        if len(dni) == 8:
            self.btns_Read()
            self.datosUser = read_user(dni)
            if self.datosUser:
                self.activar_campos()   
                id_user, nombre, apellidos, email, telef, rol, self.edad, self.fecha_naci, usuario, contra = self.datosUser
                self.vistU.entry_Udni.insert(0, dni)
                self.vistU.entry_Unombre.insert(0, nombre)
                self.vistU.entry_Unombre.config(state="disabled")
                self.vistU.entry_Uapellido.insert(0, apellidos)
                self.vistU.entry_Uapellido.config(state="disabled")
                self.vistU.entry_Uemail.insert(0, email)
                self.vistU.entry_Uemail.config(state="disabled")
                self.vistU.entry_Utelefono.insert(0, telef)
                self.vistU.entry_Utelefono.config(state="disabled")
                self.vistU.combox_Urol.insert(0, rol)
                self.vistU.combox_Urol.config(state="disabled")
                
                if self.edad is None:
                    self.vistU.combox_Uedad.config(state="disabled")
                else:
                    self.vistU.combox_Uedad.insert(0, self.edad)
                    self.vistU.combox_Uedad.config(state="disabled")
                
                if self.fecha_naci is None:
                    self.vistU.entry_Ufech_naci.config(state="disabled")
                else:
                    self.vistU.entry_Ufech_naci.insert(0, self.fecha_naci)
                    self.vistU.entry_Ufech_naci.config(state="disabled")
                    
                self.vistU.btn_Ucalendario.config(state="disabled")
                self.vistU.entry_Uusuario.insert(0, usuario)
                self.vistU.entry_Uusuario.config(state="disabled")
                self.vistU.entry_Ucontra.insert(0,contra )
                self.vistU.entry_Ucontra.config(state="disabled")
                self.vistU.label_Umensaje.config(text="DATOS ENCONTADOS", fg="#2F80D8")
            else:
                self.vistU.label_Umensaje.config(text="DATOS NO ENCONTRADOS", fg="#DDE11A")
                self.activar_campos()
                self.desactivar_campos()
        else:
            self.vistU.label_Umensaje.config(text="INGRESE UN DNI CORRECTO", fg="#DDE11A" )
        self.ventana_usuario.after(2000, self.ocultar_mensaje)
        
    def update (self):
        self.read()
        self.vistU.entry_Unombre.config(state="normal")
        self.vistU.entry_Uapellido.config(state="normal")
        self.vistU.entry_Uemail.config(state="normal")
        self.vistU.entry_Utelefono.config(state="normal")
        self.vistU.entry_Udni.config(state="disabled")
        
        # Edad
        if self.edad is None:
            self.vistU.combox_Uedad.config(state="normal")
        else:
            self.vistU.combox_Uedad.config(state="disabled")
            
        # Fecha de Nacimiento
        if self.fecha_naci is None:
            self.vistU.entry_Ufech_naci.config(state="normal")
            self.vistU.btn_Ucalendario.config(state="normal")
        else:
            self.vistU.entry_Ufech_naci.config(state="disabled")
            self.vistU.btn_Ucalendario.config(state="disabled")
            
        self.btns_Update()
        
    def cancelar (self):
        self.desactivar_campos()
        user = self.vistU.entry_Udni.get()
        userExiste = existe_user(user)
        if userExiste:
            self.btns_Cancelar_Guardar()
        else:
            self.btns_Cancelar_Guardar()
            self.vistU.btn_Ueditar.config(state="disabled")
            self.vistU.btn_Ueliminar.config(state="disabled")
        
    def delete(self):
        dni = self.vistU.entry_Udni.get()
        txt_resultado, color = delete_user(dni)
        self.vistU.label_Umensaje.config(text=txt_resultado, fg=color)
        self.ventana_usuario.after(2000, self.ocultar_mensaje)
        self.activar_campos()
        self.desactivar_campos()
        self.obtener_dato()
        
    def guardar(self):
        dni = self.vistU.entry_Udni.get()
        nombre = self.vistU.entry_Unombre.get()
        apellido = self.vistU.entry_Uapellido.get()
        email = self.vistU.entry_Uemail.get()
        telefo = self.vistU.entry_Utelefono.get()
        rol = self.vistU.combox_Urol.get() 
        user = self.vistU.entry_Uusuario.get()
        contra = self.vistU.entry_Ucontra.get()
        edad = self.vistU.combox_Uedad.get()
        fecha_nacimiento = self.vistU.entry_Ufech_naci.get()
        idrol = None
        
    # PARA CREAR USUARIO
        if self.vistU.btn_Ucrear['state'] == "normal":
            # Valida que los datos estan Vacios
            if not dni.strip() or not nombre.strip() or not apellido.strip() or not email.strip() or not telefo.strip() or not user.strip() or not contra.strip():
                self.vistU.label_Umensaje.config(text="INGRESE EN TODOS LOS CAMPOS", fg="#DDE11A")
            else:
                try:
                    # el numero no contiene letras
                    DnisinLetra = int(dni)  
                    if len(dni) == 8:   # Valida que el DNI sea de 8 digitos
                        # Valida que el rol sea ADMINISTRADOR y ESTANDAR
                        if rol ==  self.admi or rol ==  self.estand: 
                            
                            validar_edad = self.validar_edad(edad)
                            validar_fecha = self.validar_fecha(fecha_nacimiento)
                            
                            if validar_edad != False and validar_fecha != False:
                                if rol == self.admi:    # Si es Admin
                                    idrol = 1
                                elif rol == self.estand: # Si es Estandar
                                    idrol = 2
                                    
                                idRol = idrol
                                txt_resultado, color, existe =  create_user(dni, nombre, apellido, email, telefo, idRol, validar_edad, validar_fecha, user, contra)
                                
                                if existe: 
                                    self.vistU.label_Umensaje.config(text=txt_resultado, fg=color)
                                    self.activar_campos()
                                else:
                                    self.desactivar_campos() 
                                    self.btns_Cancelar_Guardar()
                                    self.vistU.label_Umensaje.config(text=txt_resultado, fg=color)
                                        
                            else:
                                self.desactivar_campos()
                                self.btns_Cancelar_Guardar()
                                self.vistU.label_Umensaje.config(text="INGRESE UNA EDAD CORRECTA", fg="#DDE11A")
                        else:
                            self.vistU.label_Umensaje.config(text="SELECCIONE UN ROL", fg="#DDE11A")
                    else:
                        self.vistU.label_Umensaje.config(text="ERROR DE DNI. 8 DIGITOS", fg="#FF0707")
                except ValueError:
                    self.vistU.label_Umensaje.config(text="NO SE PERMITE LETRAS EN EL DNI", fg="#FF0707")
    # PARA ACTUALIZAR
        elif self.vistU.btn_Ueditar['state'] == "normal":
            
            validar_edad = self.validar_edad(edad)
            validar_fecha = self.validar_fecha(fecha_nacimiento)
            
            if validar_edad != False and validar_fecha != False:
                try:
                    mensaj_result, color = update_user(dni, nombre, apellido, email, telefo, validar_edad, validar_fecha)
                    self.vistU.label_Umensaje.config(text=mensaj_result, fg=color)
                except Error:
                    # Validación de la edad
                    if type(edad) == str:
                        try:
                            edad = int(edad)
                        except ValueError:
                                self.vistU.combox_Uedad.delete(0, END)
                                self.vistU.label_Umensaje.config(text="Edad Incorrecto".upper(), fg="#FF0707")
                    # Validación de la fecha de nacimiento
                    try:
                        datetime.strptime(fecha_nacimiento, self.formatoFecha)
                    except ValueError:
                        self.vistU.entry_Ufech_naci.delete(0,END)
                        self.vistU.label_Umensaje.config(text="El formato de la fecha no es válido ('YYYY-MM-DD').".upper(), fg="#FF0707")   
                    
                self.desactivar_campos()#igaul
                self.btns_Cancelar_Guardar()
            
        self.ventana_usuario.after(2000, self.ocultar_mensaje)
        self.obtener_dato()