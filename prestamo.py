class Prestamo:
    def __init__(self, tipo_prestamo, fecha_inicio, fecha_limite, id_prestamo):
        self.tipo_prestamo = tipo_prestamo
        self.fecha_inicio = fecha_inicio
        self.fecha_limite = fecha_limite
        self.id_prestamo = id_prestamo

    def registrar_prestamo(self, identificacion, titulo, autor, nombre, numero_ejemplar, fecha_inicio, fecha_limite):
        # Lógica para registrar un préstamo
        return self.id_prestamo
