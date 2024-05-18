import tkinter as tk
# Función para manejar el evento de presionar Enter en el cuadro de texto
def on_enter(event):
    texto = texto_entrada.get("1.0", "end-1c")
    etiqueta.config(text="Texto ingresado:\n" + texto)
# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Cuadro de Texto")
# Crear un cuadro de texto
texto_entrada = tk.Text(ventana, height=5, width=40)
texto_entrada.pack(padx=10, pady=10)
texto_entrada.bind("<Return>", on_enter)  # Vincular el evento "Return" (Enter) al manejo de la función on_enter
# Crear una etiqueta para mostrar el texto ingresado
etiqueta = tk.Label(ventana, text="Ingrese texto y presione Enter")
etiqueta.pack(padx=10, pady=10)
# Mostrar la ventana
ventana.mainloop()
