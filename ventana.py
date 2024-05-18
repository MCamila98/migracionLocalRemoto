import tkinter as tk
# crear ventana
ventana= tk.Tk()
# configuraciones
ventana.title("Mi ventana")
ventana.geometry("500x400")# anchura  por altura
ventana.config(bg="white")

#crear frame
frame= tk.Frame(ventana,bd=2, relief=tk.SOLID)
frame.pack(padx=10,pady=10)
# mostrar la ventana

label= tk.Label(frame, text="label dentro de la interfaz")
label.pack()

ventana.mainloop()