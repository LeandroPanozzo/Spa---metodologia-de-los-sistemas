#Crear un boton 4 para que se muestre en la posicion de abajo
import tkinter as tki

ventana= tki.Tk()
ventana.title("Ahora tenemos ventanas!")
ventana.geometry("480x200")

boton1 = tki.Button(ventana, text="Boton 1")
boton2 = tki.Button(ventana, text="Boton 2")
boton3 = tki.Button(ventana, text="Boton 3")
boton4 = tki.Button(ventana, text="Boton 4")

boton1.pack(side= "top")
boton2.pack(side= "left")
boton3.pack(side= "right")
boton4.pack(side= "bottom")

ventana.mainloop()