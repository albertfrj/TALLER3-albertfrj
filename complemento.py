from ingredientes import Ingredientes

"""Construya las clases Base y Complemento que heredan de la clase abstracta
Ingrediente. Recuerde que en este caso la base tendrá el atributo extra sabor,
mientras que los complementos tendrán la función extra renovar_inventario. Para las
bases la función abastecer sumará 5 en el inventario, mientras que para los
complementos se aumentará en 10. No olvide colocar el getter y el setter para el
atributo sabor."""

class Complemento(Ingredientes):
    def __init__(self, precio, calorias, nombre, inventario, es_vegetariano):
        super().__init__(precio, calorias, nombre, inventario, es_vegetariano)
        
    def renovar_inventario(self)->None:
        self.inventario = 0
        
    def abastecer(self):
        self.inventario += 10