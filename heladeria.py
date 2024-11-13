from copa import Copa
import ingredientes

class Heladeria():
    def __init__(self, productos):
        self.productos = productos
    
    
    def vender(self,producto):
        if producto in self.productos:
            producto.calcular_inventario()
            if producto.inventario is True:
               print(f"Se realizo la venda de un@ {producto.nombre}")
               producto.descontar_inventario() 
                               
            else:
                print('falta inventario')
        else:
            print('producto no existe')
    
    def encontrar_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None





                