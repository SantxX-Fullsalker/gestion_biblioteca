class Articulo:
    def __init__(self, codigo, titulo, autor, categoria, disponible=True):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = disponible

    def registrar_articulo(self):
        from bdd_articulo import registrar_articulo_bd
        registrar_articulo_bd(self.codigo, self.titulo, self.autor, self.categoria, self.disponible)
        return f"Artículo '{self.titulo}' registrado exitosamente."

    def verificar_disponibilidad(self):
        """
        Método para verificar si el artículo está disponible.
        """
        # Lógica para verificar disponibilidad
        return self.disponible

    def seguimiento_articulo(self):
        """
        Método para hacer seguimiento de un artículo.
        """
        # Lógica para hacer seguimiento de un artículo
        return f"Seguimiento realizado para el artículo '{self.titulo}'."

    def reportar_articulo(self):
        """
        Método para reportar un problema con el artículo.
        """
        # Actualizar la disponibilidad a False o eliminar el artículo de la base de datos
        self.disponible = False
        return f"Problema reportado para el artículo '{self.titulo}'."
