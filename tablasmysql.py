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

# Crear la tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        edad INT
    )
""")
conn.commit()

def update_data():
    # Limpiar la tabla antes de actualizar
    for record in treeview.get_children():
        treeview.delete(record)

    # Obtener los datos de la base de datos y mostrarlos en el Treeview
    cursor.execute("SELECT * FROM personas")
    for row in cursor.fetchall():
        treeview.insert("", "end", values=row)

root = tk.Tk()
root.title("Database App")

# Crear los widgets
label = ttk.Label(root, text="Datos de la base de datos:")
label.grid(row=0, column=0, padx=10, pady=10)

treeview = ttk.Treeview(root, columns=("ID", "Nombre", "Edad"))
treeview.grid(row=1, column=0, padx=10, pady=10)
treeview.heading("#0", text="ID")
treeview.heading("#1", text="Nombre")
treeview.heading("#2", text="Edad")

update_button = ttk.Button(root, text="Actualizar", command=update_data)
update_button.grid(row=2, column=0, padx=10, pady=10)

# Actualizar los datos al iniciar la aplicación
update_data()

root.mainloop()
