import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Personalización de la Interfaz")

# Personalizar colores de fondo, texto y borde de un botón
boton = tk.Button(ventana, text="Botón", bg="blue", fg="white", bd=2)
boton.pack()
#boton1 = tk.Button(ventana, text="Botón1", bg="yellow", fg="white", bd=4)
#boton1.pack()

# Mostrar la ventana##
ventana.mainloop()
