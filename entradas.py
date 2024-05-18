import tkinter as tk

# Función para manejar el evento de presionar Enter
def on_enter(event):
    texto = entry.get()
    etiqueta.config(text="Texto ingresado: " + texto)

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Cuadro de Entrada")

# Crear un cuadro de entrada
entry=tk.Entry(ventana)
entry.pack(padx=10,pady=10)
entry.bind("<Return>", on_enter)

etiqueta=tk.Label(ventana, text="ingrese texto y presione enter")
etiqueta.pack(padx=10,pady=10)
# Mostrar la ventana
ventana.mainloop()
