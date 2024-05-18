import tkinter as tk
# Función para manejar el evento de clic en las casillas de verificación
def on_checkbox_click():
    seleccion = ""
    if var1.get() == 1:
        seleccion += "Opción 1 "
    if var2.get() == 1:
        seleccion += "Opción 2 "
    if var3.get() == 1:
        seleccion += "Opción 3 "
    etiqueta.config(text="Selección: " + seleccion)

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Casillas de Verificación")

# Variables de control para las casillas de verificación
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Crear casillas de verificación
checkbox1 = tk.Checkbutton(ventana, text="Opción 1", variable=var1, command=on_checkbox_click)
checkbox1.pack()
checkbox2 = tk.Checkbutton(ventana, text="Opción 2", variable=var2, command=on_checkbox_click)
checkbox2.pack()
checkbox3 = tk.Checkbutton(ventana, text="Opción 3", variable=var3, command=on_checkbox_click)
checkbox3.pack()

# Crear una etiqueta para mostrar la selección
etiqueta = tk.Label(ventana, text="Selección: ")
etiqueta.pack()

# Mostrar la ventana
ventana.mainloop()
