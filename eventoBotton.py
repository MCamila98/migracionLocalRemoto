import tkinter as tk

# Función para manejar el evento de clic del botón
def on_button_click():
    print("¡Botón clickeado!")

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Manejo de Eventos")

# Crear un botón
boton = tk.Button(ventana, text="Clic aquí")
boton.pack()
# Asociar la función on_button_click con el evento de clic del botón
boton.bind("<Button-1>", lambda event: on_button_click())

#boton = tk.Button(ventana, text="Haz clic aquí", command=on_button_click)
#boton.pack(padx=10, pady=10)
# Mostrar la ventana
ventana.mainloop()




