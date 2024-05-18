import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Personalización de la Interfaz")

# Personalizar la fuente del texto de una etiqueta
etiqueta = tk.Label(ventana, text="Texto con Fuente Personalizada", font=("Arial", 12))
etiqueta.pack()

# Mostrar la ventana
ventana.mainloop()
