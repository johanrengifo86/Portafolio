from msilib.schema import File
from tkinter import *
from tkinter import filedialog as FileDialog
from io import open


# Archivo Nuevo o existente
ruta = "" # Se utiliza para almacenar la ruta del fichero
#============Lógica=============
def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Editor de Texto")

def abrir():
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = FileDialog.askopenfilename(initialdir='.', 
                                      filetypes=(("Ficheros de Texto", "*.txt"),),
                                      title="Abrir fichero de texto")
    
    if ruta !="":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta +  " - Editor de Texto")


def guardar():
    mensaje.set("Guardar Fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    
    else:
        guardar_como()
        



def guardar_como():
    global ruta
    mensaje.set("Guardar Fichero Como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente") 
    else:
        mensaje.set("Guardado Cancelado")
        ruta = ""



#=================Configuracion Interfaz=================
# Configuración de la Raiz
root = Tk()
root.title("Editor de Texto")

# Menú Superior
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)  #tearoff desaparece linea 
#Comandos del menu
file_menu.add_command(label="Nuevo", command = nuevo )
file_menu.add_command(label="Abrir", command = abrir)
file_menu.add_command(label="Guardar", command = guardar)
file_menu.add_command(label="Guardar Como", command= guardar_como)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)
menu_bar.add_cascade(menu=file_menu, label="Archivo")

# Caja de Texto Central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

#Monitor inferior 
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor_inferior = Label(root, textvariable=mensaje, justify='left')
monitor_inferior.pack(side="left")

# Se añade el menu a la raiz
root.config(menu=menu_bar)






# Finalización bucle de la aplicación
root.mainloop()

