from tkinter import END

from mysqlx import Error
from Inicio_Sesion.Modelo import Usuario

from Cuenta.Modelo import existe_cuenta, obtener_datos_cuenta, read_cuenta, delete_cuenta, update_cuenta, create_cuenta

class Cuenta:
    def __init__(self, vistaC, user_name ):
        self.vistaC = vistaC
        self.controlador_Cuenta = vistaC.masterC
        self.btns_Inicio, self.btns_Crear, self.btns_Read, self.btns_Update, self.btns_Cancelar_Guardar = self.Accion_Botones()
        
        self.nombre_suario = user_name
        
    def Accion_Botones(self):
        def btns_Inicio():
            self.vistaC.btn_Ccancelar.config(state="disabled")
            self.vistaC.btn_Cguardar.config(state="disabled")
            self.vistaC.btn_Celiminar.config(state="disabled")
            self.vistaC.btn_Ceditar.config(state="disabled")
            self.vistaC.btn_Cbuscar.config(state="normal")
            self.vistaC.btn_Ccrear.config(state="normal")
        
        def btns_para_Crear():
            #Habilitamos Botones
            self.vistaC.btn_Ccrear.config(state="normal")
            self.vistaC.btn_Ccancelar.config(state="normal")
            self.vistaC.btn_Cguardar.config(state="normal")
            
            #Desabilitamos Botones
            self.vistaC.btn_Celiminar.config(state="disabled")
            self.vistaC.btn_Ceditar.config(state="disabled")
            self.vistaC.btn_Cbuscar.config(state="disabled")
            
        def btns_para_Update():
            # HABILITAMOS BOTONES
            self.vistaC.btn_Ceditar.config(state="normal")
            self.vistaC.btn_Ccancelar.config(state="normal")
            self.vistaC.btn_Cguardar.config(state="normal")
            
            # DESHABILITAMOS BOTONES
            self.vistaC.btn_Celiminar.config(state="disabled")
            self.vistaC.btn_Ccrear.config(state="disabled")
            self.vistaC.btn_Cbuscar.config(state="disabled")
            
        def btns_para_Read():
            self.vistaC.btn_Celiminar.config(state="normal")
            self.vistaC.btn_Ceditar.config(state="normal")
            self.vistaC.btn_Cbuscar.config(state="normal")
            
        def btns_para_Cancelar_Guardar():
            # PARA CREAR Y ACTUALIZAR
            btns_Inicio()
            self.vistaC.btn_Ceditar.config(state="normal")
            self.vistaC.btn_Celiminar.config(state="normal")
        
        return btns_Inicio, btns_para_Crear, btns_para_Read, btns_para_Update, btns_para_Cancelar_Guardar
    
    def obtener_dato(self):
        
        resultado = Usuario(self.nombre_suario)
        id_user, tipo_user = resultado 
        
        result_Cuentas = obtener_datos_cuenta(id_user, tipo_user)
        
        # Limpiar TreeView antes de agregar nuevos datos
        for record in self.vistaC.tbl_cuenta.get_children():
            self.vistaC.tbl_cuenta.delete(record)
        
        # Agregar datos al TreeView desde la lista de datos
        for dato in result_Cuentas:
            self.vistaC.tbl_cuenta.insert("", "end", values=dato)
        
    def manejar_estado_campos(self, campos, estado):
        for campo in campos:
            campo.config(state=estado)
        
    def activar_campos(self):
        campos_a_activar = [
            self.vistaC.entry_Cn,
            self.vistaC.entry_Cusuario,
            self.vistaC.entry_Ccontra,
            self.vistaC.comob_Ctipo,
            self.vistaC.entry_Calias,
            self.vistaC.entry_Cdescripcion,
            self.vistaC.entry_Ctelefono,
            self.vistaC.entry_Clink
        ]
        self.manejar_estado_campos(campos_a_activar, "normal")
        for campo in campos_a_activar:
            campo.delete(0, END)
        
    def desactivar_campos(self):
        campos_a_desactivar = [
            self.vistaC.entry_Cn,
            self.vistaC.entry_Cusuario,
            self.vistaC.entry_Ccontra,
            self.vistaC.comob_Ctipo,
            self.vistaC.entry_Calias,
            self.vistaC.entry_Cdescripcion,
            self.vistaC.entry_Ctelefono,
            self.vistaC.entry_Clink
        ]
        self.manejar_estado_campos(campos_a_desactivar, "disabled")
        self.vistaC.entry_Cn.config(state="normal")
        
        self.btns_Inicio()
        
    def ocultar_mensaje(self):
        self.vistaC.label_Cmensaje.config(text="")
    
    def create(self):
        self.activar_campos()
        self.vistaC.entry_Cn.config(state="disabled")
        self.btns_Crear()
        
    def read(self):
        id = self.vistaC.entry_Cn.get()
        if (not isinstance(id, str)) or int(id) > 0:
            try:
                self.btns_Read()
                self.datosCuenta = read_cuenta(id)
                if self.datosCuenta:
                    self.activar_campos()   
                    id_cuenta, alias, user, contra, tipo_cuenta, telef, descrip, id_user, link = self.datosCuenta
                    
                    self.vistaC.entry_Cn.insert(0, id_cuenta)
                    
                    if alias:
                        self.vistaC.entry_Calias.insert(0, alias)
                        self.vistaC.entry_Calias.config(state="disabled")
                    else:
                        self.vistaC.entry_Calias.insert(0, "")
                        self.vistaC.entry_Calias.config(state="disabled")
                        
                    self.vistaC.entry_Calias.config(state="disabled")
                    self.vistaC.entry_Cusuario.insert(0, user)
                    self.vistaC.entry_Cusuario.config(state="disabled")
                    self.vistaC.entry_Ccontra.insert(0, contra)
                    self.vistaC.entry_Ccontra.config(state="disabled")
                    self.vistaC.comob_Ctipo.insert(0, tipo_cuenta)
                    self.vistaC.comob_Ctipo.config(state="disabled")
                    
                    if telef:
                        self.vistaC.entry_Ctelefono.insert(0, telef)
                        self.vistaC.entry_Ctelefono.config(state="disabled")
                    else:
                        self.vistaC.entry_Ctelefono.insert(0, "")
                        self.vistaC.entry_Ctelefono.config(state="disabled")
                        
                    if descrip:
                        self.vistaC.entry_Cdescripcion.insert(0, descrip)
                        self.vistaC.entry_Cdescripcion.config(state="disabled")
                    else:
                        self.vistaC.entry_Cdescripcion.insert(0, "")
                        self.vistaC.entry_Cdescripcion.config(state="disabled")
                        
                    if link:
                        self.vistaC.entry_Clink.insert(0, link)
                        self.vistaC.entry_Clink.config(state="disabled")
                    else:
                        self.vistaC.entry_Clink.insert(0, "")
                        self.vistaC.entry_Clink.config(state="disabled")
                    
                    self.vistaC.label_Cmensaje.config(text="DATOS ENCONTADOS", fg="#2F80D8")
                else:
                    self.vistaC.label_Cmensaje.config(text="DATOS NO ENCONTRADOS", fg="#DDE11A")
                    self.activar_campos()
                    self.desactivar_campos()
                    
            except TypeError:
                self.vistaC.label_Cmensaje.config(text="INGRESE UN NUMERO", fg="#DDE11A")
                
        else:
            self.vistaC.label_Cmensaje.config(text="INGRESE UN ID CORRECTO", fg="#DDE11A" )
        self.controlador_Cuenta.after(2000, self.ocultar_mensaje)
        
    def update (self):
        self.vistaC.entry_Calias.config(state="normal")
        self.vistaC.entry_Ctelefono.config(state="normal")
        self.vistaC.entry_Cdescripcion.config(state="normal")
        self.vistaC.entry_Ccontra.config(state="normal")
        self.vistaC.entry_Clink.config(state="normal")
        self.vistaC.entry_Cn.config(state="disabled")
            
        self.btns_Update()
        
    def cancelar (self):
        self.desactivar_campos()
        id = self.vistaC.entry_Cn.get()
        cuentaExiste = existe_cuenta(id)
        if cuentaExiste:
            self.btns_Cancelar_Guardar()
        else:
            self.btns_Cancelar_Guardar()
            self.vistaC.btn_Ceditar.config(state="disabled")
            self.vistaC.btn_Celiminar.config(state="disabled")
        
    def delete(self):
        id = self.vistaC.entry_Cn.get()
        txt_resultado, color = delete_cuenta(id)
        self.vistaC.label_Cmensaje.config(text=txt_resultado, fg=color)
        self.controlador_Cuenta.after(2000, self.ocultar_mensaje)
        self.activar_campos()
        self.desactivar_campos()
        self.obtener_dato()
        
    def guardar(self):
        id = self.vistaC.entry_Cn.get()
        alias = self.vistaC.entry_Calias.get()
        user = self.vistaC.entry_Cusuario.get()
        contra = self.vistaC.entry_Ccontra.get()
        tipo_cuenta = self.vistaC.comob_Ctipo.get()
        telefo = self.vistaC.entry_Ctelefono.get()
        descrip = self.vistaC.entry_Cdescripcion.get()
        link = self.vistaC.entry_Clink.get()
        
        resultado = Usuario(self.nombre_suario)
        id_user = int(resultado[0])
        
    # PARA CREAR CUENTA
        if self.vistaC.btn_Ccrear['state'] == "normal":
            # Valida que los datos estan Vacios
            if not user.strip() or not contra.strip() or not tipo_cuenta.strip() or not telefo.strip():
                self.vistaC.label_Cmensaje.config(text="INGRESE EN TODOS LOS CAMPOS", fg="#DDE11A")
            else:
                
                if  not alias.strip():
                    alias = None
                elif not telefo.strip():
                    telefo=None
                elif not descrip.strip():
                    descrip =None
                elif not link.strip():
                    link = None
                
                txt_resultado, color, id_cuenta =  create_cuenta(alias, user, contra, tipo_cuenta, telefo, descrip, id_user, link)
                
                self.vistaC.entry_Cn.config(state="normal")
                self.vistaC.entry_Cn.insert(0,id_cuenta)
                self.desactivar_campos() 
                self.btns_Cancelar_Guardar()
                self.vistaC.label_Cmensaje.config(text=txt_resultado, fg=color)
                    
    # PARA ACTUALIZAR
        elif self.vistaC.btn_Ceditar['state'] == "normal":
            
                mensaj_result, color = update_cuenta(id, alias, contra, telefo, descrip, link)
                self.vistaC.label_Cmensaje.config(text=mensaj_result, fg=color)
                
                self.desactivar_campos()#igaul
                self.btns_Cancelar_Guardar()
            
        self.controlador_Cuenta.after(2000, self.ocultar_mensaje)
        self.obtener_dato()