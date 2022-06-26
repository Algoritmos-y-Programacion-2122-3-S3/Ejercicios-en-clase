from drinks import DrinkAlcohol, DrinkNoAlcohol
from customer import Customer

def main():
    customers = []
    drinks_alcohol = []
    drinks_no_alcohol = []
    tables = {}

    while True:
        print("*** Welcome to Saman Bar ***")
        print("Enter a valid option")
        option = int(input("1- Add new drink\n2-Add new customer\n3-Purchase\n4-Pay\n5-Exit->"))
        if option == 1:
            option_drink = int(input("1-With Alcohol\n2-No Alcohol\n->"))
            print("ADD DRINK")
            if option_drink == 1:
                drink_alcohol = add_drink_alcohol()
                drinks_alcohol.append(drink_alcohol)
            else:
                drink_no_alcohol = add_drink_no_alcohol()
                drinks_no_alcohol.append(drink_no_alcohol)

        elif option == 2:
            print("ADD CUSTOMER")
            customer = add_customer()
            customers.append(customer)
        elif option == 3:
            print("PURCHASE")
            if len(customers) > 0:
                for i in range(len(customers)):
                    print("index",i,"Name",customers[i].name,"id",customers[i].id,sep=" - ")
                customer_index = int(input("Please enter the customer index for the purchase: "))
                customer = customers[customer_index]
                print("Available Drinks")
                if customer.age >= 18:
                    drink_type = int(input("Please enter drink type that you want:\n1-Alcohol\n2-No Alcohol\n->"))
                    if drink_type == 1:
                        for i in range(len(drinks_alcohol)):
                            print("index",i,"Name",drinks_alcohol[i].name,"Price",drinks_alcohol[i].price,sep=" - ")
                        drink_index = int(input("Please enter the drink index for the purchase: "))
                        drink = drinks_alcohol[drink_index] 
                    else:
                        for i in range(len(drinks_no_alcohol)):
                            print("index",i,"Name",drinks_no_alcohol[i].name,"Price",drinks_no_alcohol[i].price,sep=" - ")
                        drink_index = int(input("Please enter the drink index for the purchase: "))
                        drink = drinks_no_alcohol[drink_index]
                    customer.drink_list.append(drink)
                else:
                    for i in range(len(drinks_no_alcohol)):
                            print("index",i,"Name",drinks_no_alcohol[i].name,"Price",drinks_no_alcohol[i].price,sep=" - ")
                    drink_index = int(input("Please enter the drink index for the purchase: "))
                    drink = drinks_no_alcohol[drink_index]
                    customer.drink_list.append(drink)

            else:
                print("You must to register at least one customer")
        elif option == 4:
            for i in range(len(customers)):
                    print("index",i,"Name",customers[i].name,"id",customers[i].id,sep=" - ")
            customer_index = int(input("Please enter the customer index for the payment: "))
            customer = customers[customer_index]
            print("*** RECEIPT ***")
            print("Name", customer.name)
            print("id", customer.id)
            print("Age", customer.age)
            total = 0
            
            for product in customer.drink_list:
                print(product.name, end="-")
                print(product.price)
                total +=product.price
            print("Total:",total)
        else:
            break
    
    #Fin del dia

    
            
def add_customer():
    name= input("Please enter the name: ")
    age= input("Please enter the age: ")
    id= input("Please enter the id: ")

    return Customer(name,age,id)

def add_drink_alcohol():
    name= input("Please enter the name: ")
    price= input("Please enter the price: ")
    grade= input("Please enter the alcohol grade: ")

    return DrinkAlcohol(name,price,grade)

def add_drink_no_alcohol():
    name= input("Please enter the name: ")
    price= input("Please enter the price: ")
    temperature= input("Please enter the temperature: ")

    return DrinkNoAlcohol(name,price,temperature)


    


main()