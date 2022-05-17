def main():
    meat_types = {"L": 15, "P":8, "M":5}
    print("*** WELCOME ***")
    name = input("Please enter your name: ")
    dni = input("Please enter your dni: ")
    type = input("Please enter your the type of the you want: \n L- Lomito\n P- Punta\n M- Molida\n ->")
    kg = int(input("Please enter kg: "))

    total = get_total(meat_types,type,kg)

    net_total = discount(total)

    print_recipe(name,dni,type.upper(),kg,net_total)

def discount(total):
    discount = 0
    if total > 30:
        discount += total * 0.05
    if is_prime(total):
        discount += total * 0.15
    return total - discount

def is_prime(total):
    is_prime = True
    aux = total - 1
    while aux > 1:
        if total % aux == 0:
            is_prime = False
            break 
        aux -= 1
    return is_prime

def get_total(meat_types,type,kg):
    return float(meat_types.get(type) * kg)

def print_recipe(name,dni,type,kg, net_total):
    print("*** RECIPE ***")
    print("Name:",name)
    print("DNI:",dni)
    print("Meat Type:",type)
    print("kg:",kg)
    print("Total:",net_total)

main()