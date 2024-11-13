class Perro:
    def __init__(self, nombre, raza, peso, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad
        
    
    def ladrar(self):
        return '!Guau, guau'
    
    def modificar_peso(self, nuevo_peso):
        self.peso = nuevo_peso

    def dar_nombre(self):
        return self.__nombre