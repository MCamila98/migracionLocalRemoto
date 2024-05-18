import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("400x600")

# Crear un frame para el display
display_frame = tk.Frame(root, height=100, bg="grey")
display_frame.pack(expand=True, fill="both")

# Crear una variable StringVar para el display de la calculadora
input_text = tk.StringVar()

# Crear el display de la calculadora
display_label = tk.Label(display_frame, textvariable=input_text, font=('Arial', 24), bg="grey", fg="white")
display_label.pack(expand=True, fill='both')

# Crear un frame para los botones
buttons_frame = tk.Frame(root)
buttons_frame.pack(expand=True, fill="both")

# Crear los botones
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(buttons_frame, text=button, font=('Arial', 18), borderwidth=0)
    btn.grid(row=row, column=col, sticky=tk.NSEW)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configurar el tamaño de las columnas y filas del frame de botones
for i in range(4):
    buttons_frame.grid_columnconfigure(i, weight=1)
    buttons_frame.grid_rowconfigure(i, weight=1)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
