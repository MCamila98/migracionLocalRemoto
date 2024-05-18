import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Frame")

# Crear un frame
frame = tk.Frame(ventana, bd=2, relief=tk.SOLID)
frame.pack(padx=10, pady=10)

# Crear un label dentro del frame
label = tk.Label(frame, text="Este es un label dentro del frame")
label.pack()

# Crear un botón dentro del frame
boton = tk.Button(frame, text="Este es un botón dentro del frame")
boton.pack()

# Mostrar la ventana
ventana.mainloop()
