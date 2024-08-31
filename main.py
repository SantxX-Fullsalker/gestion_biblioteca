from flask import Flask, render_template, request, jsonify  # Importa jsonify para uso en la conversión a JSON
from usuario import Usuario
from articulo import Articulo
from prestamo import Prestamo
from devolucion import Devolucion
from categoria import Categoria
from bdd_usuario import crear_base_datos_usuario, registrar_usuario_bd, eliminar_base_datos_usuarios, mostrar_usuarios_registrados
from bdd_articulo import crear_base_datos_articulo, registrar_categoria_bd, registrar_articulo_bd, eliminar_base_datos_articulo, obtener_categorias_bd, obtener_articulos_bd

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Crear la base de datos al iniciar la aplicación
crear_base_datos_usuario()
crear_base_datos_articulo()

# Ruta de la página principal
@app.route('/')
def index():
    return render_template('index.html')

# **CLASE USUARIO**
@app.route('/registrar_usuario', methods=['GET', 'POST'])
def registrar_usuario():
    mensaje = ""
    if request.method == 'POST':
        # Captura de datos del formulario
        identificacion = request.form['identificacion']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        celular = request.form['celular']
        correo = request.form['correo']
        nacimiento = request.form['nacimiento']
        ocupacion = request.form['ocupacion']
        estudia = request.form.get('estudia')

        # Crear una instancia de Usuario y validar datos
        usuario = Usuario(identificacion, nombre, direccion, celular, correo, nacimiento, ocupacion, estudia)
        mensaje = usuario.registrar_usuario()

        # Si el usuario es válido, se registra en la base de datos
        if "registrado exitosamente" in mensaje:
            registrar_usuario_bd(identificacion, nombre, direccion, celular, correo, nacimiento, ocupacion, estudia)

    return render_template('registrar_usuario.html', mensaje=mensaje)

# *MOSTRAR USUARIOS*
@app.route('/mostrar_usuarios', methods=['GET'])
def mostrar_usuarios():
    usuarios = mostrar_usuarios_registrados()
    return jsonify([{'id': u[0], 'identificacion': u[1], 'nombre': u[2], 'direccion': u[3], 'celular': u[4], 
                     'correo': u[5], 'nacimiento': u[6], 'ocupacion': u[7], 'estudia': u[8]} for u in usuarios])


#            *ARTICULO Y CATEGORIA*

@app.route('/gestionar_articulos')
def gestionar_articulos():
    return render_template('gestionar_articulos.html')

# Rutas para manejar categorías y artículos
@app.route('/agregar_categoria', methods=['GET', 'POST'])
def agregar_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        categoria = Categoria(nombre, descripcion)
        mensaje = categoria.agregar_categoria()
        return render_template('gestionar_articulos.html', mensaje=mensaje)
    return render_template('agregar_categoria.html')

# Ruta para registrar un artículo con categorías
@app.route('/registrar_articulo', methods=['GET', 'POST'])
def registrar_articulo():
    mensaje = ""
    categorias = obtener_categorias_bd()  # Obtener todas las categorías

    if request.method == 'POST':
        codigo = request.form['codigo']
        titulo = request.form['titulo']
        autor = request.form['autor']
        categoria_id = request.form['categoria_id']
        
        articulo = Articulo(codigo, titulo, autor, categoria_id)
        mensaje = articulo.registrar_articulo()

    return render_template('registrar_articulo.html', mensaje=mensaje, categorias=categorias)

@app.route('/mostrar_articulos', methods=['GET'])
def mostrar_articulos():
    articulos = obtener_articulos_bd()
    return jsonify([{'id': a[0], 'codigo': a[1], 'titulo': a[2], 'autor': a[3], 
                     'categoria_id': a[4], 'disponible': 'Sí' if a[5] else 'No'} for a in articulos])

# Rutas para otras funcionalidades
@app.route('/verificar_disponibilidad')
def verificar_disponibilidad():
    return "Verificar disponibilidad - por implementar"

@app.route('/seguimiento_articulo')
def seguimiento_articulo():
    return "Seguimiento de artículo - por implementar"

@app.route('/reportar_articulo')
def reportar_articulo():
    return "Reportar artículo - por implementar"

# Iniciar la aplicación
if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        # Eliminar la base de datos al finalizar el programa
        eliminar_base_datos_usuarios()
        eliminar_base_datos_articulo()
