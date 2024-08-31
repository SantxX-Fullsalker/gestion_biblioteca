import sqlite3
import os

DB_NAME = "bdd_usuarios.db"

def crear_base_datos_usuario():
    """Crea la base de datos y la tabla de usuarios si no existen."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        identificacion TEXT NOT NULL,
                        nombre TEXT NOT NULL,
                        direccion TEXT,
                        celular TEXT,
                        correo TEXT,
                        nacimiento TEXT,
                        ocupacion TEXT,
                        estudia TEXT
                      )''')
    conn.commit()
    conn.close()

def registrar_usuario_bd(identificacion, nombre, direccion, celular, correo, nacimiento, ocupacion, estudia):
    """Registra un nuevo usuario en la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO usuarios (identificacion, nombre, direccion, celular, correo, nacimiento, ocupacion, estudia)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (identificacion, nombre, direccion, celular, correo, nacimiento, ocupacion, estudia))
    conn.commit()
    conn.close()

def mostrar_usuarios_registrados():
    """Devuelve una lista de todos los usuarios registrados."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def eliminar_base_datos_usuarios():
    """Elimina la base de datos al detener el programa."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)