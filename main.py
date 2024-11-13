from copa import Copa
from base import Base
from complemento import Complemento
from heladeria import Heladeria
from funciones import Funciones
from malteada import Malteada

    
helado_fresa = Base(precio=500, calorias= 23.2, nombre="helado de fresa", es_vegetariano=True, inventario=7, sabor="fresa")
chispas_chocolate = Base(precio=1000, calorias= 12.2, nombre="chispas de chocolate", es_vegetariano=True, inventario=4, sabor="chocolate")
galletas = Complemento(precio=700, calorias= 3.2, nombre="galletas", es_vegetariano=True, inventario=8)
banano = Complemento(precio=200, calorias= 4.2, nombre="banano", es_vegetariano=True, inventario=5)
durazno = Complemento(precio=400, calorias= 1.2, nombre="durazno", es_vegetariano=True, inventario=15)

copa_helado = Copa("Copa de Helado", 5000, "vaso normal", helado_fresa, chispas_chocolate,galletas)
banana_split = Copa("Banana Split", 10000, "vaso normal", banano, durazno, galletas)
tiramisu = Malteada("Tiramisu", 12000, 250, chispas_chocolate, banano, galletas)
malteada_durazno = Malteada("Tiramisu", 12000, 250, chispas_chocolate, durazno, helado_fresa)


copa_helado.calcular_inventario()

ice_dreams = Heladeria([copa_helado, banana_split, tiramisu, malteada_durazno])

def encontrar_producto_por_nombre(self, nombre):
    for producto in self.productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None


while True:
    print("""
        Heladeria ICE DREAMS
        1. Vender
        2. Ver inventario
        3. Verificar Producto mas rentable
        4. Salir
        """)
    opcion = int(input("Elija una opcion: "))
    
    if opcion == 1:
        print((f"""
                * Copa de Helado
                * Banana Split
                * Tiramisu
                * Malteada Durazno
              
              """))
        producto_nombre = input("Elige un producto a vender: ")
        producto = ice_dreams.encontrar_producto_por_nombre(producto_nombre)
        ice_dreams.vender(producto)
    
    if opcion == 2:
        print(f"""
                {galletas.inventario} Galletas
                {chispas_chocolate.inventario} chispas_chocolate
                {helado_fresa.inventario} helado_fresa
                {banano.inventario} Bananos
                {durazno.inventario} Duraznos
              
              """)
    
    if opcion == 3:
        producto1 = {'nombre': copa_helado.nombre, "rentabilidad": copa_helado.calcular_rentabilidad()}
        producto2 = {'nombre': banana_split.nombre, "rentabilidad": banana_split.calcular_rentabilidad()}
        producto3 = {'nombre': tiramisu.nombre, "rentabilidad": tiramisu.calcular_rentabilidad()}
        producto4 = {'nombre': malteada_durazno.nombre, "rentabilidad": malteada_durazno.calcular_rentabilidad()}
        print(Funciones.best_ptroduct(producto1, producto2, producto3, producto4))
        
        
    
    
    if opcion == 4:
        break

    
    
    
    