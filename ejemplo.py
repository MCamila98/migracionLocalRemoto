import tkinter as tk

def mostrar_mensaje():
    label.config(text="¡Hola, Mundo!")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Tkinter")

# Crear un frame
frame = tk.Frame(ventana)
frame.pack(padx=10, pady=10)

# Crear una etiqueta
label = tk.Label(frame, text="¡Hola!")
label.pack(padx=10, pady=10)

# Crear un botón
boton = tk.Button(frame, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
