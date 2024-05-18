import tkinter as tk
from PIL import ImageTk, Image

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Personalización de la Interfaz")

# Cargar una imagen utilizando PIL
imagen = Image.open("imagen.jpg")
imagen = ImageTk.PhotoImage(imagen)
"""
# Mostrar la imagen en un widget Label
label_imagen = tk.Label(ventana, image=imagen)
label_imagen.pack(padx=10, pady=10)
label2_imagen = tk.Label(ventana, text="mi bebe")
label2_imagen.pack(padx=10, pady=10)
"""
boton=tk.Button(ventana, image=imagen)
boton.pack(padx=10, pady=10)

# Mostrar la ventana
ventana.mainloop()
