import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Personalización de la Interfaz")

# Personalizar el estilo del borde de un botón
boton = tk.Button(ventana, text="Botón", relief="sunken")
boton.pack()

# Mostrar la ventana
ventana.mainloop()
