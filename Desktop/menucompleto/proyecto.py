import tkinter as tk


def mostrarproyecto(root):    
    root = tk.Tk()
    root.title("Menu principal")
    root.geometry("300x300")
    import threading
    import subprocess
    def ListaTareas_app():
        subprocess.run(["python", r"D:\informatorio parte2\ventanasgraficasPython\ListaTareas.py"])

    def listaDeTareasConRelojYbarra_app():
        subprocess.run(["python", r"D:\informatorio parte2\ventanasgraficasPython\listaDeTareasConRelojYbarra.py"])

    def PanelDeControlinteractivo_app():
        subprocess.run(["python", r"D:\informatorio parte2\ventanasgraficasPython\PanelDeControlinteractivo.py"])

    def Reloj_app():

        import tkinter as tk
        from time import strftime

        my_window = tk.Tk()
        my_window.title('Reloj Digital')
        my_window.geometry('250x100')

        def time_clock():
            display_time = strftime('%H:%M:%S %p')
            label.config(text = display_time)
            label.after(1000, time_clock)

        label = tk.Label(my_window, font=('Calibri', 24), foreground = 'blue')
        label.pack(anchor = 'center', pady = 30)

        time_clock()
        my_window.mainloop()

    def RelojConBarra_app():
        subprocess.run(["python", r"D:\informatorio parte2\ventanasgraficasPython\relojConBarra.py"])

    def run_in_thread(target):
        thread = threading.Thread(target=target)
        thread.start()

    

    task_list_button = tk.Button(root, text="lista de tareas con categorias", command=lambda: run_in_thread(ListaTareas_app))
    task_list_button.pack(pady=10)

    home_page_button = tk.Button(root, text="pagina de inicio con barra de desplazamiento", command=lambda: run_in_thread(listaDeTareasConRelojYbarra_app))
    home_page_button.pack(pady=10)

    control_panel_button = tk.Button(root, text="panel de control ", command=lambda: run_in_thread(PanelDeControlinteractivo_app))
    control_panel_button.pack(pady=10)

    clock_button = tk.Button(root, text="reloj simple", command=lambda: run_in_thread(Reloj_app))
    clock_button.pack(pady=10)

    clock_scroll_button = tk.Button(root, text="reloj con barra de desplazamiento", command=lambda: run_in_thread(RelojConBarra_app))
    clock_scroll_button.pack(pady=10)
    
    clock_scroll_button = tk.Button(root, text="Volver", command=root.destroy)
    clock_scroll_button.pack(pady=10)
    root.mainloop()
