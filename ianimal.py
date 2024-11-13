from abc import abstractmethod, ABC

class IAnimal(ABC):

    @abstractmethod
    def comer(self, kilos):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass
    
    @abstractmethod
    def calcular_calorias(self):
        pass
    
    

    