from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, peso, raza):
        #Aca se inicializan los atributos de la clase padre
        super().__init__(nombre, edad, peso)
        #Atributos de la instancia 
        self.raza = raza

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, value):
        if isinstance(value, str):
            self.__raza = value
        else:
            raise ValueError('Expected str')
        
    def hacer_sonido(self):
        return 'Miau, miau'
    

gato1  = Gato('Pancho',3,12.3,'pincher')

print(gato1.__dict__)
print(gato1.hacer_sonido())