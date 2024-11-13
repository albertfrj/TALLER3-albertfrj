from abc import ABC, abstractmethod
class Ingredientes(ABC):
    def __init__(self, precio: float, calorias: float, nombre: str, inventario: int, es_vegetariano: bool):
        self._precio = precio
        self._calorias = calorias
        self._nombre = nombre
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano

    @abstractmethod
    def abastecer(self, cantidad: int):
        pass

    # Getters y setters
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, value):
        if isinstance(value, float):
            self._precio = value

    @property
    def calorias(self):
        return self._calorias
    @calorias.setter
    def calorias(self, value):
        if isinstance(value, float):
            self._calorias = value

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str):
            self._nombre = value

    @property
    def inventario(self):
        return self._inventario
    @inventario.setter
    def inventario(self, value):
        if isinstance(value, int):
            self._inventario = value

    @property
    def es_vegetariano(self):
        return self._es_vegetariano
    @es_vegetariano.setter
    def es_vegetariano(self, value):
        if isinstance(value, bool):
            self._es_vegetariano = value