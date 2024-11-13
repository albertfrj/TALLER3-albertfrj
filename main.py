from animal import Animal
from animal_exotico import Animal_Exotico
from huron import Huron
from boa_constrictor import Boa_Constrictor



animal_comun = Animal("Perro", 5, 20.5)
animal_exotico = Animal_Exotico("Tigre", 7, 150.0, "India", 0.15)
huron = Huron("Furrby", 2, 1.5, "Estados Unidos", 0.05)
boa = Boa_Constrictor("Kaa", 10, 30.0, "Brasil", 0.1)
print(f"{animal_comun.nombre} hace: {animal_comun.hacer_sonido()}")
animal_comun.comer(0.5)
print(f"{animal_comun.nombre} ha comido {animal_comun.obtener_kilos_comidos()} kilos")

print(f"\nEl costo de importar a {animal_exotico.nombre} es: ${animal_exotico.calcular_flete():.2f}")
print(f"\n{huron.nombre} hace: {huron.hacer_sonido()}")
print(f"El costo de importar a {huron.nombre} es: ${huron.calcular_flete():.2f}")
print(f"\n{boa.nombre} hace: {boa.hacer_sonido()}")
print(f"El costo de importar a {boa.nombre} es: ${boa.calcular_flete():.2f}")

boa.comer_raton()
boa.comer_raton()
print(f"{boa.nombre} ha comido {boa.ratones_comidos} ratones")
animales = [animal_comun, animal_exotico, huron, boa]
print("\nTodos los animales hacen sonidos:")
for animal in animales:
    print(f"{animal.nombre}: {animal.hacer_sonido()}")

