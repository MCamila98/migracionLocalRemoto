import tkinter as tk

# Función para manejar el evento de movimiento de ratón
def on_mouse_motion(event):
    print("Ratón moviéndose en la posición (x={}, y={})".format(event.x, event.y))

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Manejo de Eventos")

# Asociar la función on_mouse_motion con el evento de movimiento de ratón
ventana.bind("<Motion>", on_mouse_motion)

# Mostrar la ventana
ventana.mainloop()
