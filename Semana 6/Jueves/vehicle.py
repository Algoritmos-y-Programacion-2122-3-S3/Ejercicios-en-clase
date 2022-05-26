class Vehicle:

    seller = "Makinas"

    def __init__(self, brand_parameter, model_parameter, color_parameter,year):
        self.__brand = brand_parameter
        self.model= model_parameter
        self.color = color_parameter
        self.year = year
    
    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand, old_brand):
        if old_brand == "Toyota":
            print("erroor")
        else:
            self.__brand = new_brand

    def show_car(self):
        print(f"Brand{self.__brand} Color{self.color}")