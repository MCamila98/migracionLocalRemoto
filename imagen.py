import tkinter as tk
from PIL import ImageTk, Image

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Imagen")
# Cargar una imagen
imagen = Image.open("imagen.jpg")
# Crear un objeto PhotoImage a partir de la imagen
imagen_tk = ImageTk.PhotoImage(imagen)
# Mostrar la imagen en un widget Label
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack()
# Mostrar la ventana
ventana.mainloop()
