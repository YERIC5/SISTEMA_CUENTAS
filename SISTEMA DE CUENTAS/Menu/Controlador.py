
class Menu_Opciones:
    def __init__(self, vistMO, usuario, tipoUsurio):
        self.vistM = vistMO
        self.ventana_Authenticacion = vistMO.masterM  # Accede a la ventana principal
        
        self.user = usuario
        self.tipo_Usuario = tipoUsurio
        
    def Usuario(self):
        self.vistM.label_usuario.config(text=f"USUARIO: {self.user}")
        self.vistM.label_tipo_usuario.config(text=self.tipo_Usuario)
        
        self.restricciones(self.tipo_Usuario)
        
    def restricciones(self, tipo_Usuario):        
        if tipo_Usuario == "ESTANDAR":
            self.vistM.btn_usuario.config(state="disabled")
            self.vistM.btn_auditoria.config(state="disabled")
    