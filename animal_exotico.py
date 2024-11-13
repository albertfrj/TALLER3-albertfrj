from animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def calcular_flete(self) -> float:
        return self.impuestos * self.peso

    @property
    def pais_origen(self) -> str:
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, value: str) -> None:
        if isinstance(value, str):
            self._pais_origen = value
        else:
            raise ValueError('Expected str')

    @property
    def impuestos(self) -> float:
        return self._impuestos

    @impuestos.setter
    def impuestos(self, value: float) -> None:
        if isinstance(value, float):
            self._impuestos = value
        else:
            raise ValueError('Expected float')