import tkinter as tk
"""
# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("División de la ventana en tres frames")

# Crear los tres frames
frame1 = tk.Frame(ventana, bg="red", width=200, height=100)
frame1.pack(fill="both", expand=True)

frame2 = tk.Frame(ventana, bg="green", width=200, height=100)
frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(ventana, bg="blue", width=200, height=100)
frame3.pack(fill="both", expand=True)

# Mostrar la ventana
ventana.mainloop()
"""
import tkinter as tk

# Crear una instancia de la clase Tk para crear una ventana
ventana = tk.Tk()
ventana.title("División de la ventana en tres frames")

# Crear los tres frames
frame1 = tk.Frame(ventana, bg="red", width=200, height=100)
frame1.grid(row=0, column=0, sticky="nsew")

frame2 = tk.Frame(ventana, bg="green", width=200, height=100)
frame2.grid(row=1, column=0, sticky="nsew")

frame3 = tk.Frame(ventana, bg="blue", width=200, height=100)
frame3.grid(row=2, column=0, sticky="nsew")

# Configurar la expansión de los frames
ventana.grid_rowconfigure(0, weight=2)
ventana.grid_rowconfigure(1, weight=2)
ventana.grid_rowconfigure(2, weight=2)

# Mostrar la ventana
ventana.mainloop()
