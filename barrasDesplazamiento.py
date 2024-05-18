import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Barra de Desplazamiento")

# Crear un frame para contener el contenido
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

# Crear un cuadro de texto
texto = tk.Text(frame, wrap="word")
texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear una barra de desplazamiento vertical y vincularla al cuadro de texto
scrollbar_vertical = tk.Scrollbar(frame, command=texto.yview)
scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
texto.config(yscrollcommand=scrollbar_vertical.set)

# Crear una barra de desplazamiento horizontal y vincularla al cuadro de texto
scrollbar_horizontal = tk.Scrollbar(ventana, command=texto.xview, orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
texto.config(xscrollcommand=scrollbar_horizontal.set)

# Mostrar la ventana
ventana.mainloop()
