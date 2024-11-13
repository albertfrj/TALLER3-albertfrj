from animal_exotico import Animal_Exotico


class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    def comer_raton(self) -> None:
        self.ratones_comidos += 1

    @property
    def ratones_comidos(self) -> int:
        return self._ratones_comidos

    @ratones_comidos.setter
    def ratones_comidos(self, value: int) -> None:
        if isinstance(value, int):
            self._ratones_comidos = value
        else:
            raise ValueError('Expected int')
        
        
        
        
        