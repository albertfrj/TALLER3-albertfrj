
from funciones import Funciones
from iproducto import IProducto
class Malteada(IProducto):
    def __init__(self, nombre:str, precio_publico:float, volumen:int, ing1, ing2, ing3):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.volumen = volumen
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.inventario = False
        
    def calcular_inventario(self):
        if self.ing1.inventario == 0 or self.ing2.inventario == 0 or self.ing3.inventario == 0:
            self.inventario = False
        else:
            self.inventario = True
    
    def  descontar_inventario(self):
        self.ing1.inventario = self.ing1.inventario - 1
        self.ing2.inventario -=  1
        self.ing3.inventario -=  1
        
        print(self.ing1.inventario)
        
    
    
    def calcular_costo(self):
        costo_ingr = Funciones.costs(self.ing1, self.ing2, self.ing3)
        return costo_ingr
    
    def calcular_calorias(self):
        ingredientes = [self.ing1, self.ing2, self.ing3]
        calorias_ingredientes = []
        for cal in ingredientes:
            calorias_ingredientes.append(cal["calorias"])
        
        calorias = Funciones.calorie_count(calorias_ingredientes)/0.95
        return calorias
    
    def calcular_rentabilidad(self):
        return Funciones.profitability(self.precio_publico, self.ing1, self.ing2, self.ing3)
        
    
    