from Producto import Producto

class ProductoBebida(Producto):
    def __init__(self, sku: str, nombre: str, precio_base: float, stock: int, tamanio: str, temperatura: str, activo: bool = True):
        super().__init__(sku, nombre, precio_base, stock, activo)
        self.tamanio = tamanio
        self.temperatura = temperatura
    
    def ficha(self):
        return super().ficha() + f" | Tamaño: {self.tamanio} | Temperatura: {self.temperatura}"