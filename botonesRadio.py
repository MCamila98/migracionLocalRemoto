import tkinter as tk

# Función para manejar el evento de selección de botones de radio
def on_radio_button_click():
    etiqueta.config(text="Opción seleccionada: " + opcion_seleccionada.get())

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Botones de Radio")

# Variable de control para los botones de radio
opcion_seleccionada = tk.StringVar()

# Crear botones de radio
radio_button1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion_seleccionada, value="Opción 1", command=on_radio_button_click)
radio_button1.pack()
radio_button2 = tk.Radiobutton(ventana, text="Opción 2", variable=opcion_seleccionada, value="Opción 2", command=on_radio_button_click)
radio_button2.pack()
radio_button3 = tk.Radiobutton(ventana, text="Opción 3", variable=opcion_seleccionada, value="Opción 3", command=on_radio_button_click)
radio_button3.pack()

# Crear una etiqueta para mostrar la opción seleccionada
etiqueta = tk.Label(ventana, text="Opción seleccionada: ")
etiqueta.pack()

# Mostrar la ventana
ventana.mainloop()
