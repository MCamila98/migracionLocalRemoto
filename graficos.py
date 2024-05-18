import tkinter as tk

# Función para dibujar un círculo en el canvas
def dibujar_circulo(event):
    x, y = event.x, event.y
    radio = 20
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue")

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Área de Dibujo")

# Crear un canvas (área de dibujo)
canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack()

# Vincular el evento de clic del mouse al dibujo de un círculo
canvas.bind("<Button-1>", dibujar_circulo)

# Mostrar la ventana
ventana.mainloop()
