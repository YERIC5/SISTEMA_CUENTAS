from tkinter import Tk, Frame, Label, Button, Entry, ttk
from PIL import Image, ImageTk  # Necesitarás instalar el módulo Pillow para trabajar con imágenes

from Inicio_Sesion.Controlador import InicioSesion, Authenticacion
from Menu.Vista import MENU_OPCIONES

class LOGIN():
    def __init__(self, master):
        self.masterL = master
        self.masterL.title("Inicio de Sesion")
        self.masterL.minsize(500, 300)
        
        # Carga la imagen desde una direccion
        imagen = Image.open("D:\\CURSOS\\PROGRAMACION\\Python\\SISTEMA DE CUENTAS\\Icons\\user.png") 
        imagen = imagen.resize((70, 70))  # Redimensiona la imagen
        self.imagen = ImageTk.PhotoImage(imagen)
        
        self.controlador = InicioSesion(self)  # Instanciamos el controlador
        
    # FrameL_1 - TITULO
        self.frameL_1 = Frame(self.masterL, bg="white")
        self.frameL_1.pack(side="top", fill="x", pady=(30,0))
        
        label_titulo = Label(self.frameL_1, text='INCIO SESION', font=("Franklin Gothic Demi Cond", 25), fg="#A80202", bg="white")
        label_titulo.pack()
        
    # FrameL_2 - BOTON (INGRESAR) y TEXTO ACCION
        self.frameL_2 = Frame(self.masterL, bg="white")
        self.frameL_2.pack(side="bottom", fill="y", pady=(00,50), padx=(70,70))
        
        self.label_accion = Label(self.frameL_2, text='', bg="white")
        self.label_accion.grid(row=1, column=1, pady=(0,5), sticky="we")
        
        btn_ingreso = Button(self.frameL_2, text='Ingresar', command=self.controlador.iniciar_sesion, bg="#DDE11A", width=10)
        btn_ingreso.grid(row=2, column=1)
        
    # FrameL_3 - DNI y CONTRASEÑA
        self.frameL_3 = Frame(self.masterL, bg="white")
        self.frameL_3.pack(side="left", fill="both", padx=(90,0), pady=(20,5))
        
        label_dni = Label(self.frameL_3, text='DNI:', bg="white")
        label_dni.grid(row=2, column=1, sticky="w")
        self.entry_dni = Entry(self.frameL_3, width=35)
        self.entry_dni.grid(row=3, column=1, pady=(0, 5))
        
        label_contra = Label(self.frameL_3, text='Contraseña:', bg="white")
        label_contra.grid(row=4, column=1, sticky="w", pady=(5,0))
        self.entry_contra = Entry(self.frameL_3, width=35)
        self.entry_contra.grid(row=5, column=1)
        
    # FrameL_4 - IMAGEN
        self.frameL_4 = Frame(self.masterL, bg="white")
        self.frameL_4.pack(side="right", fill="both", padx=(0,80), pady=(30,0))
        
        self.label_imagen = Label(self.frameL_4, image=self.imagen, bg="white")
        self.label_imagen.grid(row=1, column=2)
        
    def Autenticacion(self, usuario, contrasena):
        self.masterL.destroy()
        ventana_authe = Tk()
        ventana = AUTHENTICACION(ventana_authe, usuario, contrasena)
        ventana_authe.configure(bg="white")
        ventana_authe.mainloop()

class AUTHENTICACION():
    def __init__(self, master, usuario, contrasena):
        self.masterA = master
        self.masterA.title("Autenticacion")
        self.masterA.minsize(500, 300)
        
        self.controladorA = Authenticacion(self, usuario, contrasena)  # Instanciamos el controlador
        
    # FrameA_1 - TITULO
        self.frameA_1 = Frame(self.masterA, bg="white")
        self.frameA_1.pack(side="top", fill="x", pady=(30, 20))
        
        label_titulo = Label(self.frameA_1, text='BIENVENIDO', font=("Franklin Gothic Demi Cond", 25), fg="#A80202", bg="white")
        label_titulo.pack()
        
    # FrameA_2 - BOTON (VALIDAR)
        self.frameA_2 = Frame(self.masterA, bg="white")
        self.frameA_2.pack(side="bottom", fill="both", pady=(0,40))
        
        self.btn_validar = Button(self.frameA_2, text="Validar", command=self.controladorA.Verificacion_codigo, bg="#DDE11A", width=10)
        self.btn_validar.pack()
        
    # FrameA_3 - ENTRY (NOMBRE, EMAIL y CODIGO)
        self.frameA_3 = Frame(self.masterA, bg="white")
        self.frameA_3.pack(side="left", fill="both", padx=(80,0))
        
        self.entry_nombre = Entry(self.frameA_3, width=40)
        self.entry_nombre.grid(row=1, column=1, sticky="w")
        
        labelA_mensaje = Label(self.frameA_3, text='Enviar codigo de verificacion al', bg="white")
        labelA_mensaje.grid(row=2, column=1, sticky="w")
        labelA_mensaje2 = Label(self.frameA_3, text='correo electronico:', bg="white")
        labelA_mensaje2.grid(row=3, column=1, sticky="w")
        
        self.entry_email= Entry(self.frameA_3, width=40)
        self.entry_email.grid(row=4, column=1,sticky="w")
        
        labelA_mensaje = Label(self.frameA_3, text='Ingrese el Codigo:', bg="white")
        labelA_mensaje.grid(row=5, column=1, sticky="w", pady=(20,20))
        self.entry_codigo= Entry(self.frameA_3, width=15)
        self.entry_codigo.grid(row=5, column=1, sticky="w", padx=(105,0))
        
    # FrameA_4 - BOTON (ENVIAR) y LABEL (MENSAJES DE CONFIRMACION)
        self.frameA_4 = Frame(self.masterA, bg="white")
        self.frameA_4.pack(side="right", padx=(0,90))
        
        self.labelA_mensaje3 = Label(self.frameA_4, text="" , bg="white")
        self.labelA_mensaje3.grid(row=0, column=1, pady=(5,0))
        
        self.btn_enviar = Button(self.frameA_4, text="Enviar", command=self.controladorA.enviar_codigo_correo, bg="#DDE11A", width=7)
        self.btn_enviar.grid(row=1, column=1, pady=(5,17))
        
        self.labelA_mensaje4 = Label(self.frameA_4, text="" , bg="white")
        self.labelA_mensaje4.grid(row=2, column=1)
        
        self.controladorA.datos_autenticacion()
        
    def Menu_Opciones(self, usuario, tipo_usuario, ):
        self.masterA.destroy()
        ventana_opciones = Tk()
        ventana = MENU_OPCIONES(ventana_opciones, usuario, tipo_usuario)
        ventana_opciones.configure(bg="white")
        ventana_opciones.mainloop()
        