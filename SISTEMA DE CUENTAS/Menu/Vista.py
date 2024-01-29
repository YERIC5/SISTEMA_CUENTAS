from tkinter import Tk, Frame, Label, Button
from PIL import Image, ImageTk

from Usuario.Vista import USUARIO
from Cuenta.Vista import CUENTA
from Reporte.Vista import REPORTE
from Busqueda.Vista import BUSQUEDA
from Cambio_Contraseña.Vista import VALIDACION_IDENTIDAD

from Menu.Controlador import Menu_Opciones

class MENU_OPCIONES():
    def __init__(self, master, usuario, tipo_usuario):
        self.masterM = master
        self.masterM.title("Menu de Opciones")
        self.masterM.minsize(750, 480)
        
        img_user = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\user.png")  # Ruta de tu imagen
        img_user = img_user.resize((100, 100))  
        img_user = ImageTk.PhotoImage(img_user)
        
        img_cuenta = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\cuenta.png")  # Ruta de tu imagen
        img_cuenta = img_cuenta.resize((100, 100))  
        img_cuenta = ImageTk.PhotoImage(img_cuenta)
        
        img_reporte = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\reporte.png")  # Ruta de tu imagen
        img_reporte = img_reporte.resize((100, 100))  
        img_reporte = ImageTk.PhotoImage(img_reporte)
        
        img_busqueda = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\busqueda.png")  # Ruta de tu imagen
        img_busqueda = img_busqueda.resize((100, 100))  
        img_busqueda = ImageTk.PhotoImage(img_busqueda)
        
        img_auditoria = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\auditoria.png")  # Ruta de tu imagen
        img_auditoria = img_auditoria.resize((100, 100))  
        img_auditoria = ImageTk.PhotoImage(img_auditoria)
        
        img_restaura = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\restaurar_contra.png")  # Ruta de tu imagen
        img_restaura = img_restaura.resize((100, 100))  
        img_restaura = ImageTk.PhotoImage(img_restaura)
        
        img_salir = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\salir.png")  # Ruta de tu imagen
        img_salir = img_salir.resize((100, 100))  
        img_salir = ImageTk.PhotoImage(img_salir)
        
        self.controlador = Menu_Opciones(self, usuario, tipo_usuario)  # Instanciamos el controlador
        
    # FrameM - LABEL (USUARIO y TIPO DE USUARIO)        
        self.frameM = Frame(self.masterM, bg="white")
        self.frameM.pack(pady=(30,0), padx=(50,50), fill="both", side="top")
        
        # FRAME 1
        self.frameM_1 = Frame(self.frameM, bg="white")
        self.frameM_1.pack(side="left")
        
        self.label_usuario = Label(self.frameM_1, bg="white", fg="#2F80D8")
        self.label_usuario.grid()
        
        # FRAME 2
        self.frameM_2 = Frame(self.frameM, bg="white")
        self.frameM_2.pack(side="right")
        
        self.label_tipo_usuario = Label(self.frameM_2, bg="white", text="", fg="#2F80D8")
        self.label_tipo_usuario.grid()
        
    # FrameM - BOTONES (USUARIO)   
        self.frameM_1 = Frame(self.masterM, bg="#2DB4A3")
        self.frameM_1.pack(fill="y", pady=(20,30), padx=(50,50))
        
        self.btn_usuario = Button(self.frameM_1, command=lambda: self.Usuario(self.masterM, usuario), image=img_user)
        self.btn_usuario.grid(row=1, column=1, pady=(40,0), padx=(50,0))
        self.btn_usuario.img_user = img_user
        label_usuario = Label(self.frameM_1, text="USUARIO", bg="#2DB4A3")
        label_usuario.grid(row=2, column=1, padx=(50,0))
        
        self.btn_cuenta = Button(self.frameM_1, command=lambda: self.Cuenta(self.masterM, usuario), image=img_cuenta)
        self.btn_cuenta.grid(row=1, column=2, pady=(40,0), padx=(40,0))
        self.btn_cuenta.img_cuenta = img_cuenta
        label_cuenta = Label(self.frameM_1, text="CUENTA", bg="#2DB4A3")
        label_cuenta.grid(row=2, column=2, padx=(40,0))
        
        self.btn_reporte = Button(self.frameM_1, command=lambda: self.Reporte(self.masterM, usuario), image=img_reporte)
        self.btn_reporte.grid(row=1, column=3, pady=(40,0), padx=(40,0))
        self.btn_reporte.img_reporte = img_reporte
        label_reporte = Label(self.frameM_1, text="REPORTE", bg="#2DB4A3")
        label_reporte.grid(row=2, column=3, padx=(40,0))
        
        self.btn_busqueda = Button(self.frameM_1, command=lambda: self.Busqueda(self.masterM, usuario), image=img_busqueda)
        self.btn_busqueda.grid(row=3, column=1, pady=(40,0), padx=(50,0))
        self.btn_busqueda.img_busqueda = img_busqueda
        label_busqueda = Label(self.frameM_1, text="BUSQUEDA", bg="#2DB4A3")
        label_busqueda.grid(row=4, column=1, pady=(0,30), padx=(50,0))  
        
        self.btn_auditoria = Button(self.frameM_1, image=img_auditoria)
        self.btn_auditoria.grid(row=3, column=2, pady=(40,0), padx=(40,0))
        self.btn_auditoria.img_auditoria = img_auditoria
        label_auditoria = Label(self.frameM_1, text="AUDITORIA", bg="#2DB4A3")
        label_auditoria.grid(row=4, column=2, pady=(0,30), padx=(40,0))
        
        self.btn_restaurar = Button(self.frameM_1, command=lambda: self.Validacion_User(self.masterM, usuario), image=img_restaura)
        self.btn_restaurar.grid(row=3, column=3, pady=(40,0), padx=(40,0))
        self.btn_restaurar.img_restaura = img_restaura
        label_auditoria = Label(self.frameM_1, text="CONTRASEÑA", bg="#2DB4A3")
        label_auditoria.grid(row=4, column=3, pady=(0,30), padx=(40,0)) 
        
        self.btn_salir = Button(self.frameM_1, image=img_salir)
        self.btn_salir.grid(row=3, column=4, pady=(40,0), padx=(40,50))
        self.btn_salir.img_salir = img_salir
        label_auditoria = Label(self.frameM_1, text="SALIR", bg="#2DB4A3")
        label_auditoria.grid(row=4, column=4, pady=(0,30), padx=(40,50)) 
        
        self.controlador.Usuario()
        
    def Usuario(self, ventana_anterior, usuario):
        
        self.masterM.withdraw()  # Ocultar la ventana actual
        ventana_usuario = Tk()
        ventana = USUARIO(ventana_usuario, ventana_anterior, usuario)
        ventana_usuario.configure(bg="white")
        ventana_usuario.mainloop()
        
    def Cuenta(self, ventana_anterior, usuario):
        self.masterM.withdraw()
        venta_Cuenta = Tk()
        ventana = CUENTA(venta_Cuenta, ventana_anterior, usuario)
        venta_Cuenta.configure(bg="white")
        venta_Cuenta.mainloop()
        
    def Reporte(self, ventana_anterior, usuario):
        self.masterM.withdraw()
        venta_Reporte = Tk()
        ventana = REPORTE(venta_Reporte, ventana_anterior, usuario)
        venta_Reporte.configure(bg="white")
        venta_Reporte.mainloop()
        
    def Busqueda(self, ventana_anterior, usuario):
        self.masterM.withdraw()
        venta_Busqueda = Tk()
        ventana = BUSQUEDA(venta_Busqueda, ventana_anterior, usuario)
        venta_Busqueda.configure(bg="white")
        venta_Busqueda.mainloop()
        
    def Validacion_User(self, ventana_anterior, usuario):
        self.masterM.withdraw()
        venta_Validamos_Usuario = Tk()
        ventana = VALIDACION_IDENTIDAD(venta_Validamos_Usuario, ventana_anterior, usuario)
        venta_Validamos_Usuario.configure(bg="white")
        venta_Validamos_Usuario.mainloop()
