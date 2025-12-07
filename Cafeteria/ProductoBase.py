from abc import abstractmethod, ABCMeta

class ProductoBase(metaclass=ABCMeta):
    def __init__(self, sku: str, nombre: str, precio_base: float, stock: int, activo: bool = True):
        self.sku = sku
        self.nombre = nombre
        self.__precio_base = precio_base
        self.__stock = stock
        self.__activo = activo
    
    @property
    def precio_base(self):
        return self.__precio_base
    @precio_base.setter
    def precio_base(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio_base = nuevo_precio
            print(f"Precio base actualizado a {nuevo_precio}€")
        else:
            print("Error: El precio base debe ser un valor numérico mayor que cero.")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if isinstance(nuevo_stock, int) and nuevo_stock >= 0:
            self.__stock = nuevo_stock
            print(f"Stock actualizado a {nuevo_stock}")
        else:
            print("Error: El stock debe ser un valor entero no negativo.")

    @property
    def activo(self):
        return self.__activo
    @activo.setter
    def activo(self, nuevo_activo):
        if isinstance(nuevo_activo, bool):
            self.__activo = nuevo_activo
            print(f"Estado de activo actualizado a {nuevo_activo}")
        else:
            print("Error: El estado activo debe ser un valor booleano (True o False).")


    @abstractmethod
    def precio_con_iva(self):
        pass

    @abstractmethod
    def descontar_stock(self, cantidad):
        pass

    @abstractmethod
    def reponer_stock(self, cantidad):
        pass
    
    @abstractmethod
    def desactivar(self):
        pass

    @abstractmethod
    def ficha(self):
        pass
    
    @classmethod
    @abstractmethod
    def actualizar_iva(cls, nuevo_iva):
        pass

    @abstractmethod
    def sku_valido(self, sku):
        pass