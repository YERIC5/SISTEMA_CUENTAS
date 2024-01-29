from tkinter import Tk, ttk, Button, Label, Entry, Frame
from tkinter.ttk import Combobox

class BUSQUEDA:
    
    def __init__(self, master, ventana_anterior):
        self.masterB = master
        self.masterB.title("Gestion de Busqueda")
        self.masterB.minsize(950,600)
        
        # Guardar una referencia a la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior = ventana_anterior
        
    # FRAMEB - TIPO DE USUARIO
        self.frameB = Frame(self.masterB, bg="white")
        self.frameB.pack(padx=(70,70), pady=(20,30), side="top", fill="both")
        
        tipo_usuario = "ADMINISTRADOR"
        self.label_BtipoUser = Label(self.frameB, bg="white", text=f"USUARIO: {tipo_usuario}", fg="#2F80D8")
        self.label_BtipoUser.pack(side="right")
        
    # BUSQUEDA DE CUENTAS
        # FRAMEBC_1 - TITULO, DNI, TIPO DE CUENTA
        self.frameBC_1 = Frame(self.masterB, bg="white")
        self.frameBC_1.pack(padx=(70,70), pady=(0,20), fill="both")
        
        label_TitCuenta = Label(self.frameBC_1, bg="white", fg="#2F80D8", text="BUSCAR CUENTA", font=("Arial", 15, "bold"))
        label_TitCuenta.grid(row=1, column=1, padx=(0, 70))
        
        label_BCdni = Label(self.frameBC_1, bg="white", text="DNI")
        label_BCdni.grid(row=1, column=2, padx=(0,5))
        self.entry_BCdni = Entry(self.frameBC_1, bg="#D9D9D9", width=20)
        self.entry_BCdni.grid(row=1, column=3, padx=(0,40))
        
        label_BCuenta = Label(self.frameBC_1, bg="white", text="Cuenta:")
        label_BCuenta.grid(row=1, column=4, padx=(0,5))
        cuentas=["FACEBOOK", "GOOGLE"]
        self.entry_BCuenta = ttk.Combobox(self.frameBC_1, width=30, values=cuentas)
        self.entry_BCuenta.grid(row=1, column=5, padx=(0,20))
        
        self.btn_BCuenta = Button(self.frameBC_1, bg="#DDE11A", text="Buscar", width=10)
        self.btn_BCuenta.grid(row=1, column=6, sticky="n")
        
        # FRAMEBC_2 - TABLA DE DATOS DE BUSQUEDA DE CUENTA
        self.frameBC_2 = Frame(self.masterB, bg="white")
        self.frameBC_2.pack(padx=(70,70), pady=(0,60), fill="both")
        
        self.tbl_BCuenta = ttk.Treeview(self.frameBC_2, columns=("n°", "user", "contra", "cuenta"), show="headings", height=6)
        
        self.tbl_BCuenta.heading("n°", text="N°")
        self.tbl_BCuenta.heading("user", text="USUARIO")
        self.tbl_BCuenta.heading("contra", text="CONTRASEÑA")
        self.tbl_BCuenta.heading("cuenta", text="CUENTA")
        
        self.tbl_BCuenta.column("n°", width=100)
        self.tbl_BCuenta.column("user", width=200)
        self.tbl_BCuenta.column("contra", width=200)
        self.tbl_BCuenta.column("cuenta", width=300)
        self.tbl_BCuenta.pack()
        
    # BUSQUEDA DE USUARIOS
        # FRAMEBU_1 - TITULO, DNI, TIPO DE USUARIO
        self.frameBU_1 = Frame(self.masterB, bg="white")
        self.frameBU_1.pack(padx=(70,70), pady=(0,20), fill="both")
        
        label_TitUsuario = Label(self.frameBU_1, bg="white", fg="#2F80D8", text="BUSCAR USUARIO", font=("Arial", 15, "bold"))
        label_TitUsuario.grid(row=1, column=1, padx=(0, 70))
        
        label_BUdni = Label(self.frameBU_1, bg="white", text="DNI")
        label_BUdni.grid(row=1, column=2, padx=(0,5))
        self.entry_BUdni = Entry(self.frameBU_1, bg="#D9D9D9", width=20)
        self.entry_BUdni.grid(row=1, column=3, padx=(0,40))
        
        label_BUsuario = Label(self.frameBU_1, bg="white", text="Usuario:")
        label_BUsuario.grid(row=1, column=4, padx=(0,5))
        usuario=["FACEBOOK", "GOOGLE"]
        self.entry_BUsuario = ttk.Combobox(self.frameBU_1, width=30, values=usuario)
        self.entry_BUsuario.grid(row=1, column=5, padx=(0,20))
        
        self.btn_BUsuario= Button(self.frameBU_1, bg="#DDE11A", text="Buscar", width=10)
        self.btn_BUsuario.grid(row=1, column=6, sticky="n")
        
        # FRAMEBU_2 - TABLA DE DATOS DE BUSQUEDA DE USUARIO
        self.frameBU_2 = Frame(self.masterB, bg="white")
        self.frameBU_2.pack(padx=(70,70), fill="both")
        
        self.tbl_BUsuario = ttk.Treeview(self.frameBU_2, columns=("n°", "user", "contra", "nombre"), show="headings", height=6)
        
        self.tbl_BUsuario.heading("n°", text="N°")
        self.tbl_BUsuario.heading("user", text="USUARIO")
        self.tbl_BUsuario.heading("contra", text="CONTRASEÑA")
        self.tbl_BUsuario.heading("nombre", text="NOMBRE")
        
        self.tbl_BUsuario.column("n°", width=100)
        self.tbl_BUsuario.column("user", width=200)
        self.tbl_BUsuario.column("contra", width=200)
        self.tbl_BUsuario.column("nombre", width=300)
        self.tbl_BUsuario.pack()
        
    # FRAMEBUS_3 - BOTON (SALIR)
        self.frameBU_3 = Frame(self.masterB, bg="white")
        self.frameBU_3.pack(padx=(70,70), pady=(0,30), side="bottom", fill="x" )
        
        self.btn_Salir = Button(self.frameBU_3, text="Salir", command=self.Salir, bg="black", fg="white", width=10)
        self.btn_Salir.pack(side="right")
    
    def Salir(self):
        # Ocultar la ventana actual
        self.masterB.withdraw()
        
        # Mostrar la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior.deiconify()