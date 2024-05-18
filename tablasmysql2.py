import tkinter as tk
from tkinter import ttk
import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
       host="localhost",
    user="root",
    password="12345678",
    database="basedatos"
)
cursor = conn.cursor()

def update_data():
    # Limpiar la tabla antes de actualizar
    for record in treeview.get_children():
        treeview.delete(record)

    # Obtener los datos de la base de datos y mostrarlos en el Treeview
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        treeview.insert("", "end", values=row)

root = tk.Tk()
root.title("Database App")



# Crear los widgets
label = ttk.Label(root, text="Datos de la base de datos:")
label.grid(row=0, column=0, padx=10, pady=10)

treeview = ttk.Treeview(root, columns=( " ","ID","Nombre","apellidos" "Edad","email"))
treeview.grid(row=1, column=0, padx=10, pady=10)
treeview.heading("#0", text=" ")
treeview.heading("#1", text="ID")
treeview.heading("#2", text="Nombre")
treeview.heading("#3", text="apellidos")
treeview.heading("#4", text="Edad")
treeview.heading("#5", text="email")

update_button = ttk.Button(root, text="Actualizar", command=update_data)
update_button.grid(row=2, column=0, padx=10, pady=10)

update_button = ttk.Button(root, text="Actualizar", command=update_data)
update_button.grid(row=2, column=0, padx=10, pady=10)

# Actualizar los datos al iniciar la aplicación
update_data()

root.mainloop()
