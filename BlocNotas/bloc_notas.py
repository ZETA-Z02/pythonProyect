import tkinter as tk 
from tkinter import filedialog
# prueba para hacer el commit 

# funciones 
ruta_archivo = ""
def nuevo_archivo():
    area_texto.delete(1.0, tk.END)
def abrir_archivo():
    global ruta_archivo
    ruta_archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Todos los Archivos","*.*"),("Archivos de Texto", "*.txt"),("Archivos de Python","*.py")])
    if ruta_archivo != "":
        area_texto.delete(1.0, tk.END)
        with open(ruta_archivo, "r", encoding="utf8") as archivo:
            area_texto.insert(1.0, archivo.read())
            
        
def guardar_archivo():
    global ruta_archivo
    if ruta_archivo:
        contenido = area_texto.get(1.0, tk.END)
        try:
            with open(ruta_archivo, "w", encoding="utf8") as archivo:
                archivo.write(contenido)
        except Exception as e:
            print(f"No se peude guardar el archivo: {e}")
def guardar_como():
    nueva_ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Todos los Archivos","*.*"),("Archivos de Texto", "*.txt"),("Archivos de Python","*.py")])
    if nueva_ruta:
        try:
            with open(nueva_ruta,'w', encoding="utf8") as archivo:
                contenido = area_texto.get(1.0, tk.END)
                archivo.write(contenido)
        except Exception as e:
            print(f"No se peude guardar el archivo: {e}")
def copiar():
    area_texto.event_generate("<<Copy>>")
def pegar():
    area_texto.event_generate("<<Paste>>")
def cortar():
    area_texto.event_generate("<<Cut>>")
# -*-*-*-*-*-*-*-*-*-*-*-

window = tk.Tk()
window.title("Block de Notas")
window.geometry("700x600+500+200")
window.resizable(False, False)
window.minsize(700,600)
window.maxsize(700,600)

menu = tk.Menu(window, tearoff=0)
window.config(menu=menu)

archivo = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="archivo", menu=archivo)
edicion = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="edicion", menu=edicion)

area_texto = tk.Text(window, font=("Arial", 12), bd=0, wrap="word", undo=True)
area_texto.pack(fill="both", expand=True)
# Menu Archivo
archivo.add_command(label='Nuevo', command=nuevo_archivo)
archivo.add_command(label='Abrir', command=abrir_archivo)
archivo.add_command(label='Guardar', command=guardar_archivo)
archivo.add_command(label='Guardar como', command=guardar_como)
# Menu Edicion
edicion.add_command(label='Copiar', command=copiar)
edicion.add_command(label='Pegar', command=pegar)
edicion.add_command(label='Cortar', command=cortar)
window.mainloop()

