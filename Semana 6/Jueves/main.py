from vehicle import Vehicle

def main():
    print("WELCOME")
    car = Vehicle("Honda","Camry","Azul","2020")
    car.set_brand("Hyundai", car.get_brand())
    print(car.get_brand())
    

main()