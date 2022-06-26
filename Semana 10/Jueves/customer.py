class Customer:
    def __init__(self,name,age,id):
        self.name = name
        self.age = int(age)
        self.id = int(id)
        self.drink_list = list()