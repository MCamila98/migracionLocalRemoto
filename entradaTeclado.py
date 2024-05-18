import tkinter as tk

# Función para manejar el evento de entrada de teclado
def on_key_press(event):
    print("Tecla presionada:", event.char)

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Manejo de Eventos")

# Asociar la función on_key_press con el evento de presionar una tecla
ventana.bind("<Key>", on_key_press)

# Mostrar la ventana
ventana.mainloop()
