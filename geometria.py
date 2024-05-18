import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Cambio de Posición con pack")
# Crear un frame
frame = tk.Frame(ventana)
frame.pack()
# Crear botones dentro del frame
boton1 = tk.Button(frame, text="Botón 1")
boton1.pack(side="left")  # Colocar a la izquierda dentro del frame
boton2 = tk.Button(frame, text="Botón 2")
boton2.pack(side="right")  # Colocar a la derecha dentro del frame
 #Crear un frame
# Mostrar la ventana
ventana.mainloop()
