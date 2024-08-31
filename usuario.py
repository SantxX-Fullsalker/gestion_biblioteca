import re

class Usuario:
    def __init__(self, identificacion, nombre, direccion, celular, correo, nacimiento, ocupacion, estudia):
        self.identificacion = identificacion
        self.nombre = nombre
        self.direccion = direccion
        self.celular = celular
        self.correo = correo
        self.nacimiento = nacimiento
        self.ocupacion = ocupacion
        self.estudia = estudia

    def validar_correo(self):
        # Validación del formato de correo usando expresiones regulares
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron_correo, self.correo) is not None

    def validar_celular(self):
        # Validación de celular (ejemplo: 10 dígitos numéricos)
        patron_celular = r"^\d{10}$"
        return re.match(patron_celular, self.celular) is not None

    def validar_identificacion(self):
        # Validación de identificación (ejemplo: longitud fija de 10 dígitos)
        return len(self.identificacion) == 10 and self.identificacion.isdigit()

    def registrar_usuario(self):
        # Método para registrar un usuario (simplificado para este ejemplo)
        if not self.validar_correo():
            return "Correo inválido"
        if not self.validar_celular():
            return "Celular inválido"
        if not self.validar_identificacion():
            return "Identificación inválida"
        # Simular registro exitoso
        return f"Usuario {self.nombre} registrado exitosamente"