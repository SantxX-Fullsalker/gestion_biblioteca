import sqlite3
import os

DB_NAME = "bdd_articulos.db"

def crear_base_datos_articulo():
    """Crea la base de datos y las tablas de artículos y categorías si no existen."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Crear tabla de categorías
    cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        descripcion TEXT
                      )''')

    # Crear tabla de artículos
    cursor.execute('''CREATE TABLE IF NOT EXISTS articulos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        codigo TEXT NOT NULL,
                        titulo TEXT NOT NULL,
                        autor TEXT,
                        categoria_id INTEGER,
                        disponible BOOLEAN,
                        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                      )''')

    conn.commit()
    conn.close()

def registrar_categoria_bd(nombre, descripcion):
    """Registra una nueva categoría en la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)''', (nombre, descripcion))
    conn.commit()
    conn.close()

def obtener_categorias_bd():
    """Obtiene todas las categorías de la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM categorias')
    categorias = cursor.fetchall()
    conn.close()
    return categorias

def registrar_articulo_bd(codigo, titulo, autor, categoria_id, disponible=True):
    """Registra un nuevo artículo en la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO articulos (codigo, titulo, autor, categoria_id, disponible) 
                      VALUES (?, ?, ?, ?, ?)''', (codigo, titulo, autor, categoria_id, disponible))
    conn.commit()
    conn.close()

def obtener_articulos_bd():
    """Obtiene todos los artículos registrados en la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, codigo, titulo, autor, categoria_id, disponible FROM articulos')
    articulos = cursor.fetchall()
    conn.close()
    return articulos

def actualizar_disponibilidad_articulo(codigo, disponible):
    """Actualiza la disponibilidad de un artículo en la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''UPDATE articulos SET disponible = ? WHERE codigo = ?''', (disponible, codigo))
    conn.commit()
    conn.close()

def eliminar_base_datos_articulo():
    """Elimina la base de datos de artículos y categorías."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
