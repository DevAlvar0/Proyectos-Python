from Producto import Producto
from Cafeteria import Cafeteria
from Pedido import Pedido
from ProductoComida import ProductoComida
from ProductoBebida import ProductoBebida
from ProductoBase import ProductoBase


# 1. Crea al menos 3 productos (bebida caliente, bebida fría, bollería) con
# distintos precios y stock.

bebida_caliente = ProductoBebida("BCA001", "Café Latte", 2.75, 50, "Mediano", "Caliente")
bebida_fria = ProductoBebida("BFR001", "Zumo de Naranja Natural", 3.50, 40, "Mediano", "Fría")
bolleria = ProductoComida("BOL001", "Croissant de Almendras", 1.80, 60)

# 2. Regístralos en una Cafeteria.
cafeteria = Cafeteria("Cafeteria")

print("--- Registro de productos en la cafetería ---")
cafeteria.registrarProducto(bebida_caliente)
cafeteria.registrarProducto(bebida_fria)
cafeteria.registrarProducto(bolleria)

print("\n--- Catálogo activo de la cafetería ---")

# 3. Muestra el catálogo activo.
for p in cafeteria.catalogoActivo():
    print(p.ficha())

print("\n--- Creación y gestión de un pedido ---")

# 4. Crea un Pedido, añade 2–3 líneas y calcula el importe total.
pedido1 = cafeteria.crearPedido("PED001")
pedido1.agregar_item(bebida_caliente, 2)
pedido1.agregar_item(bebida_fria, 1)
pedido1.agregar_item(bolleria, 3)
print(f'Importe total del pedido: {pedido1.importe_total():.2f}')

print("\n--- Proceso del pedido ---")

# 5. Llama a iniciar_preparacion(), luego marcar_listo() y entregar().
pedido1.iniciar_preparacion()
print(f'Estado del pedido: {pedido1.estado}')
pedido1.marcar_listo()
print(f'Estado del pedido: {pedido1.estado}')
pedido1.entregar()
print(f'Estado del pedido: {pedido1.estado}')

print("\n--- Resumen de pedidos ---")

# 6. Muestra:
# Producto.total_referencias
# Pedido.generados y Pedido.entregados
# cafeteria.resumen_pedidos()
print(f'Productos creados: {Producto.total_referencias}')
print(f'Pedidos generados: {Pedido.generados}')
print(f'Pedidos entregados: {Pedido.entregados}')
cafeteria.resumenPedidos()

print("\n--- Actualización del IVA y comprobación del precio con IVA ---")

# 7. Cambia el IVA con Producto.actualizar_iva(...) y comprueba el nuevo
# precio con IVA de algún producto.
Producto.actualizar_iva(15)
print(bebida_caliente.precio_con_iva())

print("\n--- Extensión con herencia ---")

coca_cola = ProductoBebida('COC001', 'Coca-Cola', 2.00, 100, 'Grande', 'Fría')
croissant = ProductoComida('CRO001', 'Croissant', 1.50, 50)
print(coca_cola.precio_base) # Accede al precio base mediante el getter

print("\n--- Registro de nuevos productos en la cafetería ---")

cafeteria.registrarProducto(coca_cola)
cafeteria.registrarProducto(croissant)

print("\n--- Catálogo activo de la cafetería ---")

for p in cafeteria.catalogoActivo():
    print(p.ficha())

print("\n--- Creación y gestión de otro pedido ---")

pedido2 = cafeteria.crearPedido('PED002')
pedido2.agregar_item(coca_cola, 1)
pedido2.agregar_item(croissant, 1)

print(f'Importe total del pedido: {pedido2.importe_total():.2f}')

print("--- 1. Intentar instanciar ProductoBase (clase abstracta) ---")
try:
    # Esto debería fallar porque ProductoBase es una clase abstracta y no se puede instanciar directamente.
    producto_abstracto = ProductoBase("ABS001", "Producto Abstracto", 10.0, 100)
    print("Se ha podido instanciar ProductoBase, lo cual no debería ocurrir.")
except Exception as e:
    print("ERROR: no se pudo crear un objeto de tipo ProductoBase", e)

print("--- 2. Instanciar clases concretas: ProductoBebida y ProductoComida ---")
# Instanciamos objetos de las clases hijas (concretas) que heredan de ProductoBase.
bebida_test = ProductoBebida("B-TEST", "Té Verde", 2.20, 30, "Mediano", "Caliente")
comida_test = ProductoComida("C-TEST", "Muffin de Chocolate", 2.50, 45, es_vegano=False, es_sin_gluten=False)

print("--- 3. Verificar polimorfismo con una lista común de tipo ProductoBase ---")
# Creamos una lista y añadimos objetos de diferentes clases hijas.
# Gracias al polimorfismo, todos pueden ser tratados como 'ProductoBase'.
try:
    lista_productos: list[ProductoBase] = [bebida_test, comida_test]
    print("Se han añadido los objetos a una lista común.\n")
except Exception as e:
    print("Error al añadir los objetos a la lista común. ", e)

print("--- 4. Recorrer la lista y llamar a métodos comunes ---")
for producto in lista_productos:
    print(f"Ficha del producto: {producto.ficha()}")
    print(f"Precio con IVA: {producto.precio_con_iva()}€")