import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Cambio de Posición con place")
# Crear un frame
frame = tk.Frame(ventana,width=200, height=200, bd=2, relief=tk.SOLID)
frame.pack()
# Crear botones dentro del frame
boton1 = tk.Button(frame, text="Botón 1")
boton1.place(x=10, y=10)  # Colocar en la posición (50, 50) dentro del frame
boton2 = tk.Button(frame, text="Botón 2")
boton2.place(x=50, y=50)  # Colocar en la posición (100, 100) dentro del frame
boton3 = tk.Button(frame, text="Botón 3")
boton3.place(x=190, y=50)
# Mostrar la ventana
ventana.mainloop()
