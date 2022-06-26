class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

class DrinkAlcohol(Drink):
    def __init__(self, name, price, grade):
        super().__init__(name,price)
        self.grade=grade 

class DrinkNoAlcohol(Drink):
    def __init__(self, name, price, temperature):
        super().__init__(name,price)
        self.temperature=temperature 