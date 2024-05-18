import tkinter as tk
import mysql.connector
from mysql.connector import Error


def insertar_paciente ():
    
   
    nombreI = nombre.get()
    edadI = edad.get()
    
    try:
        # Conexión a la base de datos
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="basedatos"
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            sql = """
                INSERT INTO usuarios (nombre, apellidos, edad_alumno, email)
                VALUES (%s, %s, %s, %s)
            """
            val = (nombreI, "ghj", edadI, "dddd@example.com")  # Asegúrate de ajustar estos valores según tu esquema
            
            cursor.execute(sql, val)
            conn.commit()
            print("Registro insertado correctamente")
        else:
            print("Error al conectar a la base de datos")
    
    except Error as e:
        print(f"Error al interactuar con MySQL: {e}")
    
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            
            
ventana=tk.Tk()
ventana.title("formulario paciente")
ventana.geometry("400x600")

label= tk.Label(ventana, text="formulario paciente")
label.pack(padx=10, pady=10)

label1= tk.Label(ventana, text="Nombre")
label1.pack(padx=10, pady=10)
nombre=tk.Entry(ventana)
nombre.pack(padx=10,pady=10)
label2= tk.Label(ventana, text="edad")
label2.pack(padx=10, pady=10)
edad=tk.Entry(ventana)
edad.pack(padx=10,pady=10)

boton=tk.Button(ventana,text="insertar",command=insertar_paciente)
boton.pack(padx=10, pady=10)

ventana.mainloop()