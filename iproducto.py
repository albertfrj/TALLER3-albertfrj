from abc import ABC, abstractmethod

"""Construya la interfaz Producto según la especificación del enunciado. En este caso la
interfaz solamente tendrá las funciones abstractas calcular_costo,
calcular_rentabilidad y calcular_calorias. """

class IProducto(ABC):
    @abstractmethod
    def calcular_costo(self):
        pass
    
    @abstractmethod
    def calcular_rentabilidad(self):
        pass
    
    @abstractmethod
    def calcular_calorias(self):
        pass