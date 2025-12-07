from Producto import Producto

class ProductoComida(Producto):
    def __init__(self, sku: str, nombre: str, precio_base: float, stock: int, activo: bool = True, es_vegano: bool = False, es_sin_gluten: bool = False):
        super().__init__(sku, nombre, precio_base, stock, activo)
        self.es_vegano = es_vegano
        self.es_sin_gluten = es_sin_gluten
    
    def ficha(self):
        return super().ficha() + f" | Es vegano: {self.es_vegano} | Es sin gluten: {self.es_sin_gluten}"