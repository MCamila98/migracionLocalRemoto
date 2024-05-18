import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Etiqueta")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Mundo!")
etiqueta.pack(padx=10, pady=10)

# Mostrar la ventana
ventana.mainloop()
