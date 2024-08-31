from datetime import datetime

class Devolucion:
    def __init__(self, fecha_entrega, fecha_actual, plazo_devolucion):
        self.fecha_entrega = fecha_entrega
        self.fecha_actual = fecha_actual
        self.plazo_devolucion = plazo_devolucion

    def multa(self, fecha_limite, fecha_entrega):
        # Cálculo de multas por día de retraso
        monto_fijo_por_dia = 5  # Monto fijo por día de retraso
        dias_retraso = (fecha_entrega - fecha_limite).days
        if dias_retraso > 0:
            return dias_retraso * monto_fijo_por_dia
        return 0
