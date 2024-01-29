from tkinter import Tk, Frame, Label, Button, Entry, ttk
from tkinter.ttk import Combobox

from Cuenta.Controlador import Cuenta

class CUENTA:
    
    def __init__(self, master, ventana_anterior, usuario): # ventana_anterior
        self.masterC = master
        self.masterC.title("Gestion de Cuentas")
        self.masterC.minsize(850,550)
        
        # Guardar una referencia a la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior = ventana_anterior
        
        self.controladorC = Cuenta(self, usuario)
        
    # FRAMEC_1 - LABEL (TIPO DE USURAIO)
        self.frameC_1 = Frame(self.masterC, bg="white")
        self.frameC_1.pack(pady=(10,0), padx=(40,190), side="top", fill="both")
        
        self.labe_user = Label(self.frameC_1, bg="white", text=f"USUARIO: {usuario}", fg="#2F80D8")
        self.labe_user.pack(side="right")
        
    # FRAMEC_8 - TABLA DE DATOS DEL USUARIO
        self.frameC_8 = Frame(self.masterC, bg="white")
        self.frameC_8.pack(padx=(70,70), pady=(20,50), fill="x", side="bottom")
        
        # Crear TreeView
        self.tbl_cuenta = ttk.Treeview(self.frameC_8, columns=("n°", "usuario", "tipo_cuenta", "descripcion"), show="headings", height=4)
        self.tbl_cuenta.heading("n°", text="N°")
        self.tbl_cuenta.heading("usuario", text="USUARIO")
        self.tbl_cuenta.heading("tipo_cuenta", text="TIPO DE CUENTA")
        self.tbl_cuenta.heading("descripcion", text="DESCRIPCION")
        
        self.tbl_cuenta.column("n°", width=50)  # Ancho personalizado para la columna "ID"
        self.tbl_cuenta.column("usuario", width=150)
        self.tbl_cuenta.column("tipo_cuenta", width=200)  # Ancho personalizado para la columna "DNI"
        self.tbl_cuenta.column("descripcion", width=305)  # Ancho personalizado para la columna "Nombre"
        self.tbl_cuenta.pack()
        
    # FRAMEC_7 - MENSAJE, SUB_FRAME (BOTONES) y SALIR
        self.frameC_7 = Frame(self.masterC, bg="white")
        self.frameC_7.pack(padx=(70,70), pady=(5,15), fill="x", side="bottom")
        
        self.label_Cmensaje = Label(self.frameC_7, bg="white")
        self.label_Cmensaje.grid(row=1, column=1, padx=(155,0), sticky="we")
        
        self.btn_Csalir = Button(self.frameC_7, text="Salir", command=self.Salir, bg="black", fg="white", width=10)
        self.btn_Csalir.grid(row=2, column=2, pady=(5,0), padx=(195,0))
        
        # SUB_FRAME - BOTONES (EDITAR, CREAR y CANCELAR)
        
        self.subFrameC_7 = Frame(self.frameC_7, bg="white")
        self.subFrameC_7.grid(row=2, column=1, pady=(5,0), padx=(155,0), sticky="we")
        
        self.btn_Ceditar = Button(self.subFrameC_7, bg="#E129FF", text="Editar", command=self.controladorC.update, width=10)
        self.btn_Ceditar.grid(row=1, column=1)     
        
        self.btn_Ccrear = Button(self.subFrameC_7, bg="#62D739", text="Crear", command=self.controladorC.create, width=10)
        self.btn_Ccrear.grid(row=1, column=2, padx=(20,20))    
        
        self.btn_Ccancelar = Button(self.subFrameC_7, bg="#AFACAB", text="Cancelar", command=self.controladorC.cancelar, width=10)
        self.btn_Ccancelar.grid(row=1, column=3)
        
    # FRAMEC_6 - SITIO WEB
        self.frameC_6 = Frame(self.masterC, bg="white")
        self.frameC_6.pack(padx=(70,0), fill="both", side="bottom")
        
        label_Clink = Label(self.frameC_6, bg="white", text="Sitio Web:")
        label_Clink.grid(row=1, column=1, pady=(10,0), padx=(0,40), sticky="w")
        self.entry_Clink = Entry(self.frameC_6, width=98)
        self.entry_Clink.grid(row=2, column=1, padx=(0,40),sticky="w")
        
    # FRAMEC_5 - TELEFONO, DESCRIPCION y BOTONES (ELIMINAR)
        self.frameC_5 = Frame(self.masterC, bg="white")
        self.frameC_5.pack(padx=(70,70), pady=(0,0), fill="x", side="bottom")
        
        label_Ctelefono = Label(self.frameC_5, bg="white", text="Telefono:")
        label_Ctelefono.grid(row=1, column=1, padx=(0,40), sticky="w")
        self.entry_Ctelefono = Entry(self.frameC_5, width=30)
        self.entry_Ctelefono.grid(row=2, column=1, padx=(0,40),sticky="w")
        
        label_Cdescripcion = Label(self.frameC_5, bg="white", text="Descripcion:")
        label_Cdescripcion.grid(row=1, column=2, sticky="w")
        self.entry_Cdescripcion = Entry(self.frameC_5, width=61)
        self.entry_Cdescripcion.grid(row=2, column=2, sticky="w")
        
        self.btn_Celiminar = Button(self.frameC_5, text="Eliminar", command=self.controladorC.delete, bg="#FF5A36", width=10)
        self.btn_Celiminar.grid(row=1, column=3, sticky="w", padx=(35,0))
        
    # FRAMEC_2 - TITULO, ALIAS y TIPO_CUENTA
        self.frameC_2 = Frame(self.masterC, bg="white")
        self.frameC_2.pack(padx=(70,0), pady=(20,0), side="left", fill="x")
        
        labe_titulo = Label(self.frameC_2, bg="white", text="CUENTA", fg="#2F80D8", font=("Arial", 20, "bold"))
        labe_titulo.grid(row=1, column= 1, sticky="w") 
        
        label_Calias = Label(self.frameC_2, bg="white", text="Alias:")
        label_Calias.grid(row=2, column=1, pady=(20,0), sticky="w")
        self.entry_Calias = Entry(self.frameC_2, width=45)
        self.entry_Calias.grid(row=3, column=1, sticky="w")
        
        label_Ctipo= Label(self.frameC_2, bg="white", text="Tipo de Cuenta:")
        label_Ctipo.grid(row=4, column=1, pady=(10,0), sticky="w")
        opciones_cuenta=["FACEBOOK", "MERCADO LIBRE", "YAPE", "AMAZON COMPRAS", "MOBILE LEGENDS", "TIKTOK", "CUENTAS DE GOOGLE", "SAMSUNG"]
        self.comob_Ctipo= Combobox(self.frameC_2, values=opciones_cuenta, width=40)
        self.comob_Ctipo.grid(row=5, column=1, sticky="w")
        
    # FRAMEC_3 - BOTONES (BUSCAR y GUARDAR)
        self.frameC_3 = Frame(self.masterC, bg="white")
        self.frameC_3.pack(padx=(0,70), fill="x", side="right")
        
        self.btn_Cbuscar = Button(self.frameC_3, text="Buscar", command=self.controladorC.read, bg="#DDE11A", width=10)
        self.btn_Cbuscar.grid(row=1, column=1, pady=(0,40), sticky="we")
        
        self.btn_Cguardar = Button(self.frameC_3, text="Guardar", command=self.controladorC.guardar, bg="#4A92FF", width=10)
        self.btn_Cguardar.grid(row=2, column=1, pady=(50,0), sticky="we")
        
    # FRAMEC_4 - N°, USUARIO, CONTRASEÑA
        self.frameC_4 = Frame(self.masterC, bg="white")
        self.frameC_4.pack(padx=(20,20), pady=(20,0), fill="y")
        
        label_Cn = Label(self.frameC_4, bg="white", text="N°:")
        label_Cn.grid(row=1, column=1, pady=(7,0), sticky="we", padx=(40,0))
        self.entry_Cn = Entry(self.frameC_4, width=15)
        self.entry_Cn.grid(row=1, column=1, pady=(7,0), sticky="e")
        
        label_Cusuario = Label(self.frameC_4, bg="white", text="Usuario:")
        label_Cusuario.grid(row=3, column=1, pady=(30,0), sticky="w")
        self.entry_Cusuario= Entry(self.frameC_4, width=45)
        self.entry_Cusuario.grid(row=4, column=1, sticky="w")
        
        label_Ccontra = Label(self.frameC_4, bg="white", text="Contraseña:")
        label_Ccontra.grid(row=5, column=1, pady=(10,0), sticky="w")
        self.entry_Ccontra = Entry(self.frameC_4, width=45)
        self.entry_Ccontra.grid(row=6, column=1, sticky="w")
        
        self.controladorC.desactivar_campos()
        self.controladorC.obtener_dato()
        
    def Salir(self):
        # Ocultar la ventana actual
        self.masterC.withdraw()
        
        # Mostrar la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior.deiconify()