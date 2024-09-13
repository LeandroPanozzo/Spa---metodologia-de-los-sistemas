import tkinter as tk
import time

def mostrar_reloj(ventana):
    ventana = tk.Tk()
    ventana.title('Reloj simple')
    ventana.geometry('400x200')

    reloj = tk.Label(ventana, font =
    ('Arial', 60), bg = '#20f', fg = 'white', pady="50", padx="40")
    def hora():
        tiempo_actual = time.strftime('%H:%M:%S')
        reloj.config(text = tiempo_actual)
        ventana.after(1000, hora)
    reloj.place(anchor = 'center', relx=0.5, rely=0.5)
    hora()
    ventana.mainloop()