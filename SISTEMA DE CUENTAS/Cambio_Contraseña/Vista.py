from tkinter import Tk, ttk, Frame, Label, Button, Entry

class VALIDACION_IDENTIDAD():
    def __init__(self, master, ventana_anterior):
        self.masterVI = master
        self.masterVI.title("Cambio de Clave de Usuario")
        self.masterVI.minsize(500,320)
        
        # Guardar una referencia a la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior = ventana_anterior
        
    # FRAMEvi - VALIDACION DE IDENTIDAD
        self.frameVI = Frame(self.masterVI, bg="white")
        self.frameVI.pack(padx=(50,50), pady=(30,30), side="top" , fill="y")
        
        label_titulo = Label(self.frameVI, bg="white", text="VALIDACION DE INDENTIDAD", font=("Arial", 17, "bold"), fg="#2F80D8")
        label_titulo.grid(row=0, column=1, sticky="we", pady=(0,20))
        
        label_text = Label(self.frameVI, bg="white", text="Ingrese los datos de Identidad")
        label_text.grid(row=1, column=1, sticky="w")
        label_text1 = Label(self.frameVI, bg="white", text="asociado con el Usuario:")
        label_text1.grid(row=2, column=1, sticky="w")
        
        self.entryRK_UserName = Entry(self.frameVI, bg="#ECE8E8", width=40)
        self.entryRK_UserName.grid(row=3, column=1, sticky="w")
        
        self.label_MensajVerifi = Label(self.frameVI, bg="white", text="")
        self.label_MensajVerifi.grid(row=5, column=1, pady=(0,10), sticky="ew")
        
        self.btn_RKverificar = Button(self.frameVI, bg="#DDE11A", command=self.Restore_Contra, text="Verificar", width=10)
        self.btn_RKverificar.grid(row=6, column=1)
        
        # SUB_FRAME_1 - EMAIL, FECHA DE NACIMIENTO
        
        self.subFrameVI = Frame(self.frameVI, bg="white")
        self.subFrameVI.grid(row=4, column=1, padx=(10,10), pady=(20,10)) 
        
        label_taxt2 = Label(self.subFrameVI, bg="white", text="Correo Electronico: ")
        label_taxt2.grid(row=1, column=1, padx=(0,5), pady=(0,10), sticky="w")
        self.entryRK_Email = Entry(self.subFrameVI, bg="#ECE8E8", width=30)
        self.entryRK_Email.grid(row=1, column=2, pady=(0,5), sticky="e")
        
        label_taxt3 = Label(self.subFrameVI, bg="white", text="Fecha de Nacimiento: ")
        label_taxt3.grid(row=2, column=1, padx=(0,10), sticky="w")
        self.entryRK_FecNacimiento = Entry(self.subFrameVI, bg="#ECE8E8", width=20)
        self.entryRK_FecNacimiento.grid(row=2, column=2, sticky="e")        
        
    def Restore_Contra(self):
        self.masteVI.destroy()
        venta_Cambio_Contraseña = Tk()
        ventana = RESTORE_KEY(venta_Cambio_Contraseña)
        venta_Cambio_Contraseña.configure(bg="white")
        venta_Cambio_Contraseña.mainloop()
        
    def Salir(self):
        # Ocultar la ventana actual
        self.masterVI.withdraw()
        
        # Mostrar la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior.deiconify()
        
class RESTORE_KEY():
    def __init__(self, master):
        self.masterRK = master
        self.masterRK.title("Restuarar Contraseña")
        self.masterRK.minsize(500,320)
        
    # FRAMERK - 
        self.frameRK = Frame(self.masterRK, bg="white")
        self.frameRK.pack(pady=(30,30), padx=(50,50))
        
        label_titulo = Label(self.frameRK, bg ="white", text="CAMBIO DE CONTRASEÑA", font=("Arail", 17, "bold"), fg="#2F80D8")
        label_titulo.grid(row=1, column=1, sticky="we")
        
        label_txtRK = Label(self.frameRK, bg="white", text="Se le envio un codigo de verificacion")
        label_txtRK.grid(row=2, column=1, sticky="w", pady=(20,0))
        
        label_txtRk1 = Label(self.frameRK, bg="white", text="a su Correo Electronico: ")
        label_txtRk1.grid(row=3, column=1, sticky="w")
        
        self.entryRK_email = Entry(self.frameRK, bg="#ECE8E8", width=35)
        self.entryRK_email.grid(row=4, column=1, pady=(5,0), sticky="w")
        
        # SUB_FRAME_1
        self.subframeRK_1 = Frame(self.frameRK, bg="white")
        self.subframeRK_1.grid(row=5, column=1, pady=(5,0), padx=(65,0), sticky="w")
        
        label_txtCodigo = Label(self.subframeRK_1, bg="white", text="Codigo:")
        label_txtCodigo.grid(row=1, column=1, padx=(0,5), sticky="w")
        
        self.entryRK_codigo = Entry(self.subframeRK_1, bg="#ECE8E8", width=15)
        self.entryRK_codigo.grid(row=1, column=2, padx=(0,20), sticky="w")
        
        self.btn_RKvalidar = Button(self.subframeRK_1, bg="#DDE11A", text="Validar", width=10)
        self.btn_RKvalidar.grid(row=1, column=3)
        label_txtRKMensajeValidar = Label(self.subframeRK_1, bg="white", text="")
        label_txtRKMensajeValidar.grid(row=2, column=3,)
        
        # SUB_FRAME_2
        self.subframeRK_2 = Frame(self.frameRK, bg="white")
        self.subframeRK_2.grid(row=6, column=1, sticky="w")
        
        label_txtRK_2= Label(self.subframeRK_2, bg="white", text="Ingrese su nueva contraseña:")
        label_txtRK_2.grid(row=1, column=1, sticky="w")
        self.entryRK_nuevaContra = Entry(self.subframeRK_2, bg="#ECE8E8", width=35)
        self.entryRK_nuevaContra.grid(row=2, column=1, sticky="w")
        
        label_txtRK_3 = Label(self.subframeRK_2, bg="white", text="Ingrese de nuevo contraseña:")
        label_txtRK_3.grid(row=3, column=1, sticky="w")
        self.entryRK_rectificaContra = Entry(self.subframeRK_2, bg="#ECE8E8", width=35)
        self.entryRK_rectificaContra.grid(row=4, column=1, sticky="w")
        
        self.btn_RKguardar = Button(self.subframeRK_2, bg="#DDE11A", text="Guardar", width=10)
        self.btn_RKguardar.grid(row=3, column=2, padx=(20,0), sticky="n")
        
        label_txtRKMensajeAceptar = Label(self.subframeRK_2, bg="white", text="hola")
        label_txtRKMensajeAceptar.grid(row=4, column=2, padx=(20,0), sticky="ew")