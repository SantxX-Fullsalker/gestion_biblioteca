class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def agregar_categoria(self):
        # Lógica para agregar una categoría
        from bdd_articulo import registrar_categoria_bd
        registrar_categoria_bd(self.nombre, self.descripcion)
        return f"Categoría '{self.nombre}' agregada exitosamente."

    def eliminar_categoria(self):
        """
        Método para eliminar una categoría existente.
        """
        # Lógica para eliminar una categoría
        return f"Categoría '{self.nombre}' eliminada exitosamente."
