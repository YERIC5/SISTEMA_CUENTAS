from Inicio_Sesion.Modelo import inicio_sesion
from Inicio_Sesion.Modelo import autenticacion
import smtplib
from email.mime.text import MIMEText
import secrets
import string

class InicioSesion:
    def __init__(self, vista):
        self.vista = vista
        self.ventana_login = vista.masterL  # Accede a la ventana principal
        
    def iniciar_sesion(self):
        usuario = self.vista.entry_dni.get()
        contrasena = self.vista.entry_contra.get()
        resultado = inicio_sesion(usuario, contrasena)
        
        if resultado and resultado[0] > 0:
            mensaje = "Accediendo a la Authenticacion".upper()
            self.vista.label_accion.config(text=mensaje, fg="#2F80DF")
            self.ventana_login.after(2000, self.ocultar_mensaje)  # Ocultar mensaje después de 2 segundos
            self.ventana_login.after(2000, self.abrir_autenticacion)  # Abrir ventana de autenticación después de 3 segundos
            
        else:
            mensaje = "Usuario no Encontrado".upper()
            self.vista.label_accion.config(text=mensaje, fg="#FF0000")
            self.ventana_login.after(2000, self.ocultar_mensaje)  # Ocultar mensaje después de 2 segundos
            
    def ocultar_mensaje(self):
        self.vista.label_accion.config(text="")  # Vaciar el mensaje después del tiempo especificado
        
    def abrir_autenticacion(self):
        usuario = self.vista.entry_dni.get()
        contrasena = self.vista.entry_contra.get()
        self.vista.Autenticacion(usuario, contrasena)
        
class Authenticacion:
    def __init__(self, vistA, usuario, contrasena):
        self.vistA = vistA
        self.ventana_Authenticacion = vistA.masterA  # Accede a la ventana principal
        
        user = usuario
        contraseña = contrasena
        
        resultados = autenticacion(user, contraseña)
        
        for fila in resultados:
            self.Uid_user = fila[0]
            self.Udni = fila[1]
            self.Unombre = fila[2]
            self.Ucorreo = fila[3]
            self.Utelefono = fila[4]
            self.Urol = fila[5]
            self.Uedad = fila[6]
            self.Ufecha_nacimiento = [7]
        
    def datos_autenticacion (self):
        self.vistA.entry_nombre.insert(0, self.Unombre)
        self.vistA.entry_nombre.config(state="disabled")
        
        self.vistA.entry_email.insert(0, self.Ucorreo)
        self.vistA.entry_email.config(state="disabled")
        
        self.vistA.entry_codigo.config(state="disabled")
        
    def generar_codigo(self, longitud):
        caracteres = string.ascii_letters + string.digits
        codigo = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        return codigo
    
    def enviar_codigo_correo(self):
        
        self.vistA.entry_codigo.config(state="normal")
        # Credenciales del remitente
        remitente = "yericflores10@gmail.com"
        password = 'elue fsli zzyd mebe'
        
        self.codigo_Envio = self.generar_codigo(8) 
        mensaje = f"Codigo de Verificacion: {self.codigo_Envio}"
        asunto = "CODIGO DE AUTHENTICACION"
        destinatario = self.Ucorreo
        
        # Crear el mensaje
        msg = MIMEText(mensaje)
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = destinatario
        
        # Conexión al servidor SMTP de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Iniciar conexión segura
        server.login(remitente, password)  # Autenticación
        
        try:
            server.sendmail(remitente, destinatario, msg.as_string())
            server.quit()
            self.vistA.labelA_mensaje3.config(text="Código Enviado", fg="#18B93C")
            self.ventana_Authenticacion.after(2000, self.ocultar_mensaje)  # Ocultar mensaje después de 2 segundos
        except Exception:
            self.vistA.labelA_mensaje3.config(text="Error al enviar el código", fg="#FF0000")
            self.ventana_Authenticacion.after(2000, self.ocultar_mensaje)  # Ocultar mensaje después de 2 segundos
            
    def ocultar_mensaje(self):
        self.vistA.labelA_mensaje3.config(text="")  # Vaciar el mensaje después del tiempo especificado
        self.vistA.labelA_mensaje4.config(text="")  # Vaciar el mensaje después del tiempo especificado
        
    def Verificacion_codigo (self):
        codgio_generado = self.codigo_Envio
        codigo_usuario = self.vistA.entry_codigo.get()
        
        if codgio_generado == codigo_usuario:
            self.vistA.labelA_mensaje4.config(text="Correcto", fg="#2F80DF")
            self.ventana_Authenticacion.after(2000, self.ocultar_mensaje)  # Ocultar mensaje después de 2 segundos
            self.ventana_Authenticacion.after(2000, self.abrir_menu)
            
        else:
            self.vistA.labelA_mensaje4.config(text="Codigo Incorrecto", fg="#FF0000")
            self.ventana_Authenticacion.after(2000, self.ocultar_mensaje)  # Ocultar mensaje después de 2 segundos
            
    def abrir_menu(self):
        usuario = self.Unombre
        rolUser = self.Urol
        
        self.vistA.Menu_Opciones(usuario, rolUser)
        