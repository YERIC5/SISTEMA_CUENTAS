from tkinter import *   
    
from Inicio_Sesion.Vista import LOGIN
from Usuario.Vista import USUARIO
from Reporte.Vista import REPORTE
from Cuenta.Vista import CUENTA

if __name__ == "__main__":
    root = Tk()
    app = LOGIN(root)  # Utiliza la clase Login que has importado
    root.configure(bg="white")
    root.mainloop()