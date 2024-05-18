import tkinter as tk

# Función para manejar el evento de clic en el botón dentro del marco
def on_button_click():
    etiqueta.config(text="¡Botón clickeado!")

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Marco con Etiqueta")

# Crear un marco con etiqueta
marco_con_etiqueta = tk.LabelFrame(ventana, text="Marco con Botón")
marco_con_etiqueta.pack(padx=10, pady=10)

# Crear un botón dentro del marco
boton = tk.Button(marco_con_etiqueta, text="Clic aquí", command=on_button_click)
boton.pack(padx=10, pady=10)

# Crear una etiqueta para mostrar mensajes
etiqueta = tk.Label(ventana, text="Esperando clic en el botón...")
etiqueta.pack(padx=10, pady=10)

# Mostrar la ventana
ventana.mainloop()
