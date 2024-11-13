
class Funciones:
    
    def is_healthy(calories: int, vegetarian: bool):
        if calories < 100 or vegetarian == True:
            return True
        else:
            return False
    
    def calorie_count(calorie_list: list):
        if isinstance(calorie_list, list):
            count = 0
            for i in calorie_list:
                count += i
            result = count * 0.95
            return result
        else: print("Lista de calorias incorrecta")
        
    def costs (ingredient1:dict, ingredient2:dict, ingredient3:dict):
        product_list = [ingredient1, ingredient2, ingredient3]
        total = 0
        for product in product_list:
            total += product["precio"]
        return total 
        
    def profitability(price: float, ingredient1, ingredient2, ingredient3) -> float:
        subtotal = ingredient1.precio + ingredient2.precio + ingredient3.precio
        profit = price - subtotal
        return profit

    def best_ptroduct(product1:dict, product2:dict, product3:dict, product4:dict): 
         
        if product1["rentabilidad"] > product2["rentabilidad"] and product1["rentabilidad"] > product3["rentabilidad"] and product1["rentabilidad"] > product4["rentabilidad"]:
            return product1["nombre"]
        elif product2["rentabilidad"] > product1["rentabilidad"] and product2["rentabilidad"] > product3["rentabilidad"] and product2["rentabilidad"] > product4["rentabilidad"]:
            return product2["nombre"]
        elif product3["rentabilidad"] > product1["rentabilidad"] and product3["rentabilidad"] > product2["rentabilidad"] and product3["rentabilidad"] > product4["rentabilidad"]:
            return product3["nombre"]
        else:
            return product4["nombre"]

 
        
        
        
        
    
    
    

        
            
        