import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Cambio de Posición con grid")
# Crear un frame
frame = tk.Frame(ventana)
frame.pack()
# Crear botones dentro del frame
boton1 = tk.Button(frame, text="Botón 1")
boton1.grid(row=0, column=0)  # Colocar en la fila 0 y columna 0 dentro del frame
boton2 = tk.Button(frame, text="Botón 2")
boton2.grid(row=1, column=2)  # Colocar en la fila 1 y columna 1 dentro del frame
boton3 = tk.Button(frame, text="Botón 3")
boton3.grid(row=1, column=1)  # Colocar en la fila 1 y columna 1 dentro del frame
# Mostrar la ventana
ventana.mainloop()
