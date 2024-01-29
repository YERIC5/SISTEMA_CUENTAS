from tkinter import Frame, Label, Button, Entry, PhotoImage, ttk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import tkinter as tk
from tkcalendar import Calendar

from Usuario.Controlador import Usuario

class USUARIO:
    def __init__(self, master, ventana_anterior, usuario): #ventana_anterior va como parametro , ventana_anterior, usuario
        self.masterU = master
        self.masterU.title("Gestion de Usuario")
        self.masterU.minsize(850,550)
        
        # Guardar una referencia a la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior = ventana_anterior
        self.controladorU = Usuario(self, usuario)
        
    # FRAMEU_1 - LABEL (TIPO DE USURAIO)
        self.frameU_1 = Frame(self.masterU, bg="white")
        self.frameU_1.pack(pady=(10,0), padx=(40,190), side="top", fill="both")
        
        self.labe_user = Label(self.frameU_1, bg="white", text=f"USUARIO: {usuario}", fg="#2F80D8")
        self.labe_user.pack(side="right")
        
    # FRAMEU_6 - TABLA DE DATOS DEL USUARIO
        self.frameU_6 = Frame(self.masterU, bg="white")
        self.frameU_6.pack(padx=(70,70), pady=(20,50), fill="x", side="bottom")
        
        # Crear TABLA DE USUARIO
        self.tbl_usuario = ttk.Treeview(self.frameU_6, columns=("n°", "dni", "nombre", "email"), show="headings", height=4)
        self.tbl_usuario.heading("n°", text="N°")
        self.tbl_usuario.heading("dni", text="DNI")
        self.tbl_usuario.heading("nombre", text="NOMBRES")
        self.tbl_usuario.heading("email", text="EMAIL")
        
        self.tbl_usuario.column("n°", width=50)  # Ancho personalizado para la columna "ID"
        self.tbl_usuario.column("dni", width=170)  # Ancho personalizado para la columna "DNI"
        self.tbl_usuario.column("nombre", width=240)  # Ancho personalizado para la columna "Nombre"
        self.tbl_usuario.column("email", width=245)  # Ancho personalizado para la columna "Nombre"
        self.tbl_usuario.pack()
        
    # FRAMEU_5 - MENSAJE, SALIR y SUB_FRAME (BOTONES)
        self.frameU_5 = Frame(self.masterU, bg="white")
        self.frameU_5.pack(padx=(70,70), pady=(5,15), fill="x", side="bottom")
        
        self.label_Umensaje = Label(self.frameU_5, bg="white")
        self.label_Umensaje.grid(row=1, column=1, padx=(155,0), sticky="we")
        
        self.btn_Usalir = Button(self.frameU_5, text="Salir", bg="black", command=self.Salir, fg="white", width=10)
        self.btn_Usalir.grid(row=2, column=2, pady=(5,0), padx=(190,0))
        
        # SUB_FRAME - BOTONES (EDITAR, CREAR y CANCELAR)
        
        self.subFrameU_5 = Frame(self.frameU_5, bg="white")
        self.subFrameU_5.grid(row=2, column=1, pady=(5,0), padx=(155,0), sticky="we")
        
        self.btn_Ueditar = Button(self.subFrameU_5, bg="#E129FF", command=self.controladorU.update, text="Editar", width=10)
        self.btn_Ueditar.grid(row=1, column=1)     
        self.btn_Ueditar.config(state="disabled")
        
        self.btn_Ucrear = Button(self.subFrameU_5, bg="#62D739",command=self.controladorU.create,  text="Crear", width=10)
        self.btn_Ucrear.grid(row=1, column=2, padx=(20,20))    
        self.btn_Ucrear.config(state="normal")
        
        self.btn_Ucancelar = Button(self.subFrameU_5, bg="#AFACAB", command=self.controladorU.cancelar, text="Cancelar", width=10)
        self.btn_Ucancelar.grid(row=1, column=3)
        self.btn_Ucancelar.config(state="disabled")
        
    # FRAMEU_2 - TITULO, NOMBRE, USUARIO, CORREO y SUBFRAME (frame_Rol_Edad ) ROL y EDAD
        self.frameU_2 = Frame(self.masterU, bg="white")
        self.frameU_2.pack(padx=(70,0), pady=(20,0), side="left", fill="both")
        
        labe_titulo = Label(self.frameU_2, bg="white", text="USUARIO", fg="#2F80D8", font=("Arial", 20, "bold"))
        labe_titulo.grid(row=1, column= 1, sticky="w") 
        
        label_Unombre = Label(self.frameU_2, bg="white", text="Nombre:")
        label_Unombre.grid(row=2, column=1, pady=(20,0), sticky="w")
        self.entry_Unombre = Entry(self.frameU_2, width=45)
        self.entry_Unombre.grid(row=3, column=1, sticky="w")
        
        label_Uusuario = Label(self.frameU_2, bg="white", text="Usuario:")
        label_Uusuario.grid(row=4, column=1, pady=(10,0), sticky="w")
        self.entry_Uusuario= Entry(self.frameU_2, width=45)
        self.entry_Uusuario.grid(row=5, column=1, sticky="w")
        
        label_Uemail = Label(self.frameU_2, bg="white", text="Correo Electronico:")
        label_Uemail.grid(row=6, column=1, pady=(10,0), sticky="w")
        self.entry_Uemail = Entry(self.frameU_2, width=45)
        self.entry_Uemail.grid(row=7, column=1, sticky="w")
        
        # SUB_FRAME - ROL y EDAD
        self.subFrameU_2 = Frame(self.frameU_2, bg="white")
        self.subFrameU_2.grid(row=8, column=1, pady=(10,0), sticky="we")
        
        label_Urol = Label(self.subFrameU_2, bg="white", text="Rol:")
        label_Urol.grid(row=1, column=1, sticky="w")
        opciones_rol=["ADMINISTRADOR", "ESTANDAR"]
        self.combox_Urol= Combobox(self.subFrameU_2, values=opciones_rol, width=25)
        self.combox_Urol.grid(row=2, column=1, sticky="w", padx=(0,20))
        
        label_Uedad = Label(self.subFrameU_2, bg="white", text="Edad:")
        label_Uedad.grid(row=1, column=2, sticky="w", padx=(20,0))
        opciones_edad=[1,2,3,4,5,6,7,8,9,10]
        self.combox_Uedad = Combobox(self.subFrameU_2, values=opciones_edad, width=6)
        self.combox_Uedad.grid(row=2, column=2, sticky="e", padx=(20,0))
        
    # FRAMEU_3 - BOTONES (BUSCAR, GUARDAR y ELIMINAR )
        self.frameU_3 = Frame(self.masterU, bg="white")
        self.frameU_3.pack(padx=(0,70), pady=(20,0), fill="both", side="right")
        
        self.btn_Ubuscar = Button(self.frameU_3, text="Buscar", command=self.controladorU.read , bg="#DDE11A", width=10)
        self.btn_Ubuscar.grid(row=1, column=1, pady=(0,40), sticky="we")
        self.btn_Ubuscar.config(state="normal")
        
        self.btn_Uguardar = Button(self.frameU_3, text="Guardar", command=self.controladorU.guardar, bg="#4A92FF", width=10)
        self.btn_Uguardar.grid(row=2, column=1, pady=(50,0), sticky="we")
        self.btn_Uguardar.config(state="disabled")
        
        self.btn_Ueliminar = Button(self.frameU_3, text="Eliminar", command=self.controladorU.delete, bg="#FF5A36", width=10)
        self.btn_Ueliminar.grid(row=3, column=1, pady=(10,60), sticky="we")
        self.btn_Ueliminar.config(state="disabled")
        
    # FRAMEU_4 - DNI, APELLIDOS, CONTRA, TELEFONO, FECHA DE NACIMIENTO y BOTON (CALENDARIO)
        self.frameU_4 = Frame(self.masterU, bg="white")
        self.frameU_4.pack(padx=(20,20), pady=(20,0), fill="y")
        
        label_Udni = Label(self.frameU_4, bg="white", text="DNI:")
        label_Udni.grid(row=1, column=1, pady=(7,0), sticky="we", padx=(0,40))
        self.entry_Udni = Entry(self.frameU_4, width=20)
        self.entry_Udni.grid(row=1, column=1, pady=(7,0), sticky="e")
        
        label_Uapellido = Label(self.frameU_4, bg="white", text="Apellidos:")
        label_Uapellido.grid(row=3, column=1, pady=(30,0), sticky="w")
        self.entry_Uapellido= Entry(self.frameU_4, width=45)
        self.entry_Uapellido.grid(row=4, column=1, sticky="w")
        
        label_Ucontra = Label(self.frameU_4, bg="white", text="Contraseña:")
        label_Ucontra.grid(row=5, column=1, pady=(10,0), sticky="w")
        self.entry_Ucontra = Entry(self.frameU_4,width=45, show="*")
        self.entry_Ucontra.grid(row=6, column=1, sticky="w")
        
        label_Utelefono = Label(self.frameU_4, bg="white", text="Telefono:")
        label_Utelefono.grid(row=7, column=1, pady=(10,0), sticky="w")
        self.entry_Utelefono= Entry(self.frameU_4, width=45)
        self.entry_Utelefono.grid(row=8, column=1, sticky="w")
        
        label_Ufech_naci= Label(self.frameU_4, bg="white", text="Fecha de Nacimiento:")
        label_Ufech_naci.grid(row=9, column=1, pady=(10,0), sticky="w")
        
        # SUB_FRAME - CALENDATIO - BOTON (CALENDARIO)
        self.subFrameU_4 = Frame(self.frameU_4, bg="white")
        self.subFrameU_4.grid(row=10, column=1, sticky="w")
        
        self.entry_Ufech_naci= Entry(self.subFrameU_4, width=30)
        self.entry_Ufech_naci.grid(row=1, column=1, sticky="w", padx=(0,5))
        
        self.btn_Ucalendario = Button(self.subFrameU_4, width=4, bg="white", command=self.calender)
        self.btn_Ucalendario.grid(row=1, column=2, sticky="w")
        self.btn_Ucalendario.config(state="disabled")
        
        self.controladorU.desactivar_campos()
        self.controladorU.obtener_dato()
        
    def calender(self):
        def obtener_fecha():
            fecha_seleccionada = cal.get_date()
            self.entry_Ufech_naci.insert(0, fecha_seleccionada)
            top.destroy()
            
        top = tk.Toplevel(self.masterU)
        cal = Calendar(top, selectmode='day', year=2024, month=1, day=1, date_pattern='yyyy-mm-dd')
        cal.pack(padx=10, pady=10)
        
        button_obtener_fecha = tk.Button(top, text="Seleccionar fecha", command=obtener_fecha)
        button_obtener_fecha.pack(pady=10)
        
    def Salir(self):
        # Ocultar la ventana actual
        self.masterU.withdraw()
        
        # Mostrar la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior.deiconify()