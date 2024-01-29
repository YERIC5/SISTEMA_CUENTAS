from tkcalendar import Calendar
from tkinter import END, Tk, Frame, Label, ttk, Button, Entry
import tkinter as tk
from Reporte.Controlador import Reporte

class REPORTE:
    def __init__(self, master, ventana_anterior, usuario): # , ventana_anterior, usuario) implementar como parametro
        
        self.masterR = master
        self.masterR.title("Reportes")
        self.masterR.minsize(1200,680)
        
        # Guardar una referencia a la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior = ventana_anterior
        #usuario = "LUIS FLORES LAPA"
        self.controladorR = Reporte(self, usuario)
        
    # FRAMER_1 - TIPO DE USUARIO y BOTON (SALIR) 
        
        self.frameR_1 = Frame(self.masterR, bg="white")
        self.frameR_1.pack(padx=(70,70), pady=(20,30), side="top", fill="both")
        
        self.label_Ruser = Label(self.frameR_1, bg="white", text=f"USURAIO: {usuario}", fg="#2F80D8")
        self.label_Ruser.pack(side="right")
        
        self.btn_Rsalir = Button(self.frameR_1, text="Salir", command=self.Salir, bg="black", fg="white", width=10)
        self.btn_Rsalir.pack(side="left")
        
    # REPORTES DE CUENTA    
        # FRAMER_2 - TITULO (REPORTES CUENTAS) y BOTON BUSCAR
        self.frameRC_2 = Frame(self.masterR, bg="white")
        self.frameRC_2.pack(padx=(70,70), fill="both")
        
        labe_titulo = Label(self.frameRC_2, bg="white", text="REPORTE CUENTAS", fg="#2F80D8", font=("Arial", 15, "bold"))
        labe_titulo.grid(row=1, column=1, sticky="w", padx=(0,70))
        
        label_1 = Label(self.frameRC_2, bg="white", text="Fecha Inicio:")
        label_1.grid(row=1, column=2, sticky="w")
        self.entry_Cfecha_inicio = Entry(self.frameRC_2, bg="white", width=20)
        self.entry_Cfecha_inicio.grid(row=1, column=4, padx=(0,10))
        self.btn_Rcalendario = Button(self.frameRC_2, width=2, bg="#750505", command=lambda: self.calender_inicio(self.entry_Cfecha_inicio))
        self.btn_Rcalendario.grid(row=1, column=3)
        
        label_2 = Label(self.frameRC_2, bg="white", text="Fecha Final:")
        label_2.grid(row=1, column=5, sticky="w")
        self.entry_Cfecha_final = Entry(self.frameRC_2, bg="white", width=20)
        self.entry_Cfecha_final.grid(row=1, column=7, padx=(0,10))
        self.btn_Rcalendario = Button(self.frameRC_2, width=2, bg="#750505", command=lambda: self.calender_fin(self.entry_Cfecha_final))
        self.btn_Rcalendario.grid(row=1, column=6)
        
        
        label_Bdni = Label(self.frameRC_2, bg="white", text="DNI:")
        label_Bdni.grid(row=1, column=8, sticky="w")
        self.entry_Cdni = Entry(self.frameRC_2, bg="white", width=20)
        self.entry_Cdni.grid(row=1, column=9, padx=(0,10))
        
        self.btn_RCbuscar = Button(self.frameRC_2, text="Buscar", command=self.controladorR.Reporte_Cuenta, bg="#DDE11A", fg="black", width=10)
        self.btn_RCbuscar.grid(row=1, column=10, sticky="w", padx=(10,0))
        
        # FRAMER_3 - TABLA DE REPORTES DE CUENTA
        self.frameRC_3 = Frame(self.masterR, bg="black")
        self.frameRC_3.pack(padx=(70,70), pady=(20,0), fill="y")
        
        self.tbl_reportCuenta = ttk.Treeview(self.frameRC_3, columns=("n°", "user", "contra", "tipo_cuenta", "dueño", "descrip", "url"), show="headings", height=7)
        
        self.tbl_reportCuenta.heading("n°", text="N°")
        self.tbl_reportCuenta.heading("dueño", text="DUEÑO")
        self.tbl_reportCuenta.heading("user", text="USUARIO")
        self.tbl_reportCuenta.heading("contra", text="CONTRASEÑA")
        self.tbl_reportCuenta.heading("tipo_cuenta", text="TIPO DE CUENTA")
        self.tbl_reportCuenta.heading("descrip", text="DESCRIPCION")
        self.tbl_reportCuenta.heading("url", text="LINK")
        
        self.tbl_reportCuenta.column("n°", width=50)
        self.tbl_reportCuenta.column("dueño", width=180)
        self.tbl_reportCuenta.column("user", width=100)
        self.tbl_reportCuenta.column("contra", width=150)
        self.tbl_reportCuenta.column("tipo_cuenta", width=150)
        self.tbl_reportCuenta.column("descrip", width=220)
        self.tbl_reportCuenta.column("url", width=200)
        self.tbl_reportCuenta.pack()
        
        # FRAMER_4 - BOTONES (EXCEL y PDF)
        self.frameRC_4 = Frame(self.masterR, bg="white")
        self.frameRC_4.pack(padx=(70,70), pady=(20,20), fill="both")
        
        self.subFrameRC_4 = Frame(self.frameRC_4, bg="white")
        self.subFrameRC_4.pack(padx=(0,80), side="right", fill="both")
        
        label_RCexporte = Label(self.subFrameRC_4, text="Exportar:", bg="white")
        label_RCexporte.grid(row=1, column=1, sticky="w")
        
        self.btn_ExcelRC = Button(self.subFrameRC_4, text="EXCEL", bg="#11BD02", command=self.controladorR.Exportar_Cuenta_Excel, width=10)
        self.btn_ExcelRC.grid(row=1, column=2, sticky="w", padx=(10,10))
        
        self.btn_PdfRC= Button(self.subFrameRC_4, text="PDF", bg="#FF0000", command=self.controladorR.Exportar_Cuenta_Pdf, width=10)
        self.btn_PdfRC.grid(row=1, column=3, sticky="w")
        
    # REPORTES DE USUARIO    
        # FRAMER_2 - TITULO (REPORTES USUARIOS) y BOTON (SALIR) 
        self.frameRU_2 = Frame(self.masterR, bg="white")
        self.frameRU_2.pack(padx=(70,70), pady=(20,20),fill="both")
        
        labe_tituloU = Label(self.frameRU_2, bg="white", text="REPORTE USUARIOS", fg="#2F80D8", font=("Arial", 15, "bold"))
        labe_tituloU.grid(row=1, column=1, sticky="w", padx=(0,60))
        
        label_1 = Label(self.frameRU_2, bg="white", text="Fecha Inicio:")
        label_1.grid(row=1, column=2, sticky="w")
        self.entry_Ufecha_inicio = Entry(self.frameRU_2, bg="white", width=20)
        self.entry_Ufecha_inicio.grid(row=1, column=4, padx=(0,10))
        self.btn_Rcalendario = Button(self.frameRU_2, width=2, bg="#750505", command=lambda: self.calender_inicio(self.entry_Ufecha_inicio))
        self.btn_Rcalendario.grid(row=1, column=3)        
        
        label_2 = Label(self.frameRU_2, bg="white", text="Fecha Final:")
        label_2.grid(row=1, column=5, sticky="w")
        self.entry_Ufecha_final = Entry(self.frameRU_2, bg="white", width=20)
        self.entry_Ufecha_final.grid(row=1, column=7, padx=(0,10))
        self.btn_Rcalendario = Button(self.frameRU_2, width=2, bg="#750505", command=lambda: self.calender_fin(self.entry_Ufecha_final))
        self.btn_Rcalendario.grid(row=1, column=6)        
        
        label_Bdni = Label(self.frameRU_2, bg="white", text="DNI:")
        label_Bdni.grid(row=1, column=8, sticky="w")
        self.entry_Udni = Entry(self.frameRU_2, bg="white", width=20)
        self.entry_Udni.grid(row=1, column=9, padx=(0,10))
        
        self.btn_RUbuscar = Button(self.frameRU_2, text="Buscar", command=self.controladorR.Reporte_Usuario, bg="#DDE11A", fg="black", width=10)
        self.btn_RUbuscar.grid(row=1, column=10, sticky="w", padx=(10,0))
        
        # FRAMER_3 - TABLA DE REPORTES DE USUARIO
        self.frameRU_3 = Frame(self.masterR, bg="black")
        self.frameRU_3.pack(padx=(70,70), fill="y")
        
        self.tbl_reportUsuario= ttk.Treeview(self.frameRU_3, columns=("n°", "dni", "nombre_completo", "email", "telef", "rol", "edad", "fecha_naci", "user", "contra"), show="headings", height=7)
        
        self.tbl_reportUsuario.heading("n°", text="N°")
        self.tbl_reportUsuario.heading("dni", text="DNI")
        self.tbl_reportUsuario.heading("nombre_completo", text="NOMBRE COMPLETO")
        self.tbl_reportUsuario.heading("email", text="EMAIL")
        self.tbl_reportUsuario.heading("telef", text="TELEFONO")
        self.tbl_reportUsuario.heading("rol", text="ROL")
        self.tbl_reportUsuario.heading("edad", text="EDAD")
        self.tbl_reportUsuario.heading("fecha_naci", text="FECHA NACIMIENTO")
        self.tbl_reportUsuario.heading("user", text="USUARIO")
        self.tbl_reportUsuario.heading("contra", text="CONTRASEÑA")
        
        self.tbl_reportUsuario.column("n°", width=40)
        self.tbl_reportUsuario.column("dni", width=70)
        self.tbl_reportUsuario.column("nombre_completo", width=200)
        self.tbl_reportUsuario.column("email", width=200)
        self.tbl_reportUsuario.column("telef", width=80)
        self.tbl_reportUsuario.column("rol", width=110)
        self.tbl_reportUsuario.column("edad", width=50)
        self.tbl_reportUsuario.column("fecha_naci", width=130)
        self.tbl_reportUsuario.column("user", width=70)
        self.tbl_reportUsuario.column("contra", width=100)
        self.tbl_reportUsuario.pack()
        
        # FRAMER_4 - BOTONES (EXCEL y PDF)
        self.frameRU_4 = Frame(self.masterR, bg="white")
        self.frameRU_4.pack(padx=(70,150), pady=(20,20), fill="both", side="right")
        
        label_RCexporte = Label(self.frameRU_4, text="Exportar:", bg="white")
        label_RCexporte.grid(row=1, column=1, sticky="w")
        
        self.btn_ExcelRU = Button(self.frameRU_4, text="EXCEL", bg="#11BD02", command=self.controladorR.Exportar_Usuario_Excel, width=10)
        self.btn_ExcelRU.grid(row=1, column=2, sticky="w", padx=(10,10))
        
        self.btn_PdfRU= Button(self.frameRU_4, text="PDF", bg="#FF0000", command=self.controladorR.Exportar_Usuario_Pdf, width=10)
        self.btn_PdfRU.grid(row=1, column=3, sticky="w")
        
        self.controladorR.Reporte_Cuenta()
        self.controladorR.Reporte_Usuario()
        
    def calender_fin(self, entry_fecha_fin):
        def obtener_fecha():
            fecha_seleccionada = cal.get_date()
            entry_fecha_fin.delete(0, END)
            entry_fecha_fin.insert(0,fecha_seleccionada)
            top.destroy()
            
        top = tk.Toplevel(self.masterR)
        cal = Calendar(top, selectmode='day', year=2024, month=1, day=1, date_pattern='yyyy-mm-dd')
        cal.pack(padx=10, pady=10)
        
        button_obtener_fecha = tk.Button(top, text="Seleccionar fecha", command=obtener_fecha)
        button_obtener_fecha.pack(pady=10)
    
    def calender_inicio(self, entry_fecha_inicio):
        def obtener_fecha():
            fecha_seleccionada = cal.get_date()
            entry_fecha_inicio.delete(0, END)
            entry_fecha_inicio.insert(0,fecha_seleccionada)
            top.destroy()
            
        top = tk.Toplevel(self.masterR)
        cal = Calendar(top, selectmode='day', year=2024, month=1, day=1, date_pattern='yyyy-mm-dd')
        cal.pack(padx=10, pady=10)
        
        button_obtener_fecha = tk.Button(top, text="Seleccionar fecha", command=obtener_fecha)
        button_obtener_fecha.pack(pady=10)
    
    def Salir(self):
        # Ocultar la ventana actual
        self.masterR.withdraw()
        
        # Mostrar la ventana anterior (MENU_OPCIONES)
        self.ventana_anterior.deiconify()