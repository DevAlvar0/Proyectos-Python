from Pedido import Pedido


class Cafeteria:
    nombre = ''
    inventario = {}
    pedidos = {}

    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.pedidos = []
    
    def registrarProducto(self, producto):
        for p in self.inventario:
            if p.sku == producto.sku:
                print(f"Error: Ya existe un producto con el SKU '{producto.sku}'.")
                return False
        self.inventario.append(producto)
        print(f"Producto '{producto.nombre}' registrado correctamente.")
        return True
    
    def catalogoActivo(self):
        listaActivos = []
        for p in self.inventario:
            if p.activo:
                listaActivos.append(p)
        return listaActivos
    
    def crearPedido(self, codigo):
        # Verificar si ya existe un pedido con el mismo código
        for p in self.pedidos:
            if p.codigo == codigo:
                print(f"Error: Ya existe un pedido con el código '{codigo}'.")
                return None
        nuevo_pedido = Pedido(codigo, [], "pendiente")
        self.pedidos.append(nuevo_pedido)
        return nuevo_pedido
    
    def buscarPedido(self, codigo):
        for p in self.pedidos:
            if p.codigo == codigo:
                return p
        return None
    
    def resumenPedidos(self):
        for p in self.pedidos:
            if p.estado == None:
                print(f'Código: {p.codigo}, Estado: {p.estado}')
    
    def ingresosEstimados(self):
        total_ingresos = 0
        for p in self.pedidos:
            if p.estado == 'listo' or p.estado == 'en_preparacion':
                total_ingresos += p.importe_total()
        return total_ingresos
