

class MiExcepcionPersonalizada(Exception):
    def __init__(self, numero, minimo, maximo):
        self.numero = numero
        self.minimo = minimo
        self.maximo = maximo
        super().__init__(f'El número {self.numero} no está entre {self.minimo} y {self.maximo}.')
    
    