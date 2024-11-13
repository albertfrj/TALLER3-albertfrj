from ingredientes import Ingredientes
"""Construya las clases Base y Complemento que heredan de la clase abstracta
Ingrediente. Recuerde que en este caso la base tendrá el atributo extra sabor,
mientras que los complementos tendrán la función extra renovar_inventario. Para las
bases la función abastecer sumará 5 en el inventario, mientras que para los
complementos se aumentará en 10. No olvide colocar el getter y el setter para el
atributo sabor."""
class Base(Ingredientes):
    def __init__(self, precio, calorias, nombre, inventario, es_vegetariano, sabor):
        super().__init__(precio, calorias, nombre, inventario, es_vegetariano)
        self.sabor = sabor

    def abastecer(self):
        self.inventario += 5
        
    # getters and setters

    @property
    def sabor(self)->str:
        return self.__sabor
    @sabor.setter
    def sabor(self, value):
        if isinstance (value, str):
            self.__sabor = value