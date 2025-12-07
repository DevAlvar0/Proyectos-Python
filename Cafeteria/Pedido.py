from Producto import Producto
from typing import List, Tuple

class Pedido:
    generados = 0
    entregados = 0

    def __init__(self, codigo: str, lineas: List[{Producto, int}], estado: str):
        self.codigo = codigo
        self.lineas = lineas
        self.estado = estado
        Pedido.generados += 1
    
    def agregar_item(self, producto: Producto, cantidad: int):
        if producto.activo and producto.stock >= cantidad:
            self.lineas.append((producto, cantidad))
            return True
        else:
            return False
    
    def importe_total(self):
        total = 0
        for producto, cantidad in self.lineas:
            total += producto.precio_con_iva() * cantidad
        return total
    
    def iniciar_preparacion(self):
        self.estado = "en_preparacion"
        try:
            for producto, cantidad in self.lineas:
                if producto.stock >= cantidad:
                    producto.descontar_stock(cantidad)
        except Exception as e:
            print(f"Error al descontar stock: {e}")
            self.estado = "pendiente"

    def marcar_listo(self):
        self.estado = "listo"
    
    def entregar(self):
        self.estado = "Entregado"
        Pedido.entregados += 1
    
    def cancelar(self):
        if self.estado == "pendiente" or self.estado == "en_preparacion":
            self.estado = "cancelado"
            return True
        else:
            print("No se puede cancelar este pedido.")
            return False