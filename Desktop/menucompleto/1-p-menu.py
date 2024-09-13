import tkinter as tk
import threading
import subprocess
import os
from proyecto import *
from PIL import Image, ImageTk 

# Obtener la ruta del directorio del proyecto
directorio_proyecto = os.path.dirname(os.path.abspath(__file__))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x300')  # Ajustado a 400x300 para que coincida con el tamaño de la imagen de fondo

def abrir_documento_word():
    # Reemplaza 'ruta/al/documento.docx' con la ruta real de tu archivo de Word
    ruta_documento = os.path.join(directorio_proyecto, 'doc1.docx')
    subprocess.Popen(['start', 'winword', ruta_documento], shell=True)

def run_in_thread(target):
    thread = threading.Thread(target=target)
    thread.start()

def mostrarproyecto_con_fondo(ventana):
    # Ruta de la imagen dentro del proyecto
    ruta_imagen = os.path.join(directorio_proyecto, "imagen_fondo.jpeg")
    
    # Cargar la imagen de fondo y redimensionarla a 400x300 píxeles
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((400, 300))
    imagen_fondo = ImageTk.PhotoImage(imagen)

    # Crear un Canvas para mostrar la imagen de fondo
    canvas = tk.Canvas(ventana, width=400, height=300)
    canvas.pack(fill='both', expand=True)
    
    # Mostrar la imagen de fondo en el Canvas
    canvas.create_image(0, 0, image=imagen_fondo, anchor='nw')
    
    # Mantener una referencia de la imagen para evitar que se recoja basura
    ventana.imagen_fondo = imagen_fondo

# Mostrar la imagen de fondo al crear la ventana principal
mostrarproyecto_con_fondo(ventana)

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear un menú desplegable
menu_archivo = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Archivo', menu=menu_archivo)
submenua = tk.Menu(menu_archivo)
submenua1 = tk.Menu(menu_archivo)
menu_archivo.add_cascade(label='Abrir', menu=submenua)
submenua.add_command(label = 'Proyecto', command=lambda: mostrarproyecto(ventana))
submenua.add_command(label=' Archivo', command=lambda: run_in_thread(abrir_documento_word))
menu_archivo.add_cascade(label='Guardar', menu=submenua1)
submenua1.add_command(label='Guardar')
submenua1.add_command(label='Guardar Como')
menu_archivo.add_separator()
menu_archivo.add_cascade(label='Salir', command=ventana.destroy)

# Crear otro menú desplegable
menu_editar = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Editar', menu=menu_editar)
menu_editar.add_cascade(label='Cortar')
menu_editar.add_cascade(label='Copiar')
menu_editar.add_cascade(label='Pegar')

# Crear otro menú desplegable
menu_seleccion = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Seleccion', menu=menu_seleccion)
menu_seleccion.add_cascade(label='Seleccionar Todo')

# Crear otro menú desplegable
menu_ayuda = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)
menu_ayuda.add_cascade(label='Acerca de')

ventana.mainloop()

