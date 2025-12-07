import math
from ProductoBase import ProductoBase
class Producto (ProductoBase):
    # Atributos de clase
    iva_porcentaje = 10.0
    total_referencias = 0

    def __init__(self, sku: str, nombre: str, precio_base: float, stock: int, activo: bool = True):
        super().__init__(sku, nombre, precio_base, stock, activo)
        Producto.total_referencias += 1  # Incrementa el contador global de productos

    def precio_con_iva(self):
        return round(self.precio_base * (1 + self.iva_porcentaje / 100), 2)  # Llama al getter

    def descontar_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        else:
            return False

    def reponer_stock(self, cantidad):
        self.stock += cantidad

    def desactivar(self):
        self.activo = False

    def ficha(self):
        estado = "Activo" if self.activo else "Inactivo"
        return (f"SKU: {self.sku} | Nombre: {self.nombre} | "
                f"Precio (IVA incl.): {self.precio_con_iva():.2f}€ | "
                f"Stock: {self.stock} | Estado: {estado}")
    
    @classmethod
    def actualizar_iva(cls, nuevo_iva):
        cls.iva_porcentaje = nuevo_iva
        return nuevo_iva

    def sku_valido(self, sku):
        for position, c in sku:
            if position >= 0 and position <= 2:
                if not c.isalpha():
                    return False
            else:
                if not c.isdigit():
                    return False
        return True