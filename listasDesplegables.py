import tkinter as tk
from tkinter import ttk

# Función para manejar el evento de selección en la lista desplegable
def on_combobox_select(event):
    seleccion = combobox.get()
    etiqueta.config(text="Opción seleccionada: " + seleccion)

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Lista Desplegable")

# Crear una lista de opciones
opciones = ["Opción 1", "Opción 2", "Opción 3"]
# Crear una variable de control para la lista desplegable
opcion_seleccionada = tk.StringVar()
# Crear una lista desplegable (Combobox)
combobox = ttk.Combobox(ventana, values=opciones, textvariable=opcion_seleccionada)
combobox.pack()
combobox.bind("<<ComboboxSelected>>", on_combobox_select)  # Vincular el evento de selección al manejo de la función on_combobox_select
# Crear una etiqueta para mostrar la opción seleccionada
etiqueta = tk.Label(ventana, text="Opción seleccionada: ")
etiqueta.pack()
# Mostrar la ventana
ventana.mainloop()
