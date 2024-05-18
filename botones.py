import tkinter as tk
# Función para manejar el clic del botón
def on_button_click():
    etiqueta.config(text="boton clickeado")
    
ventana= tk.Tk()
ventana.title("ejemplo botton")

etiqueta=tk.Label(ventana, text="haz clic en el botton")
etiqueta.pack(padx=10, pady=10)
boton=tk.Button(ventana,text="haz clic aqui", command=on_button_click)
boton.pack(padx=10, pady=10)

ventana.mainloop()