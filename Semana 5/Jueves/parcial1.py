def main():
    study_prices = {"U": 8900, "T":12640, "R":15600}
    study_names = {"U": "Ultrasound", "T":"Tomography", "R":"Resonance"}
    customer_counter = 0
    customer_counter_u = 0
    customer_counter_t = 0
    customer_counter_r = 0
    customer_amount_u = 0
    customer_amount_t = 0
    customer_amount_r = 0
    acum_discount = 0
    acum_total = 0

    while (True):
        customer_counter += 1
        dni = input("Please enter your dni: ")
        age = int(input("Please enter your age: "))
        gender = input("Please enter your gender: \n M- Male\n F- Female\n ->").upper()
        study_type = input("Please enter the type of study the you want: \n U- Ultrasound\n T- Tomography\n R- Resonance\n ->").upper()
        amount = study_prices.get(study_type)
        discount_value = discount(is_third_age(age, gender),customer_counter, amount)
        total = amount - discount_value
        acum_discount += discount_value
        acum_total += total
        
        if study_type == "U":
            customer_counter_u += 1
            customer_amount_u += total
        elif study_type == "T":
            customer_counter_t += 1
            customer_amount_t += total
        elif study_type == "R":
            customer_counter_r += 1
            customer_amount_r += total

        print("**** RECEIPT ****")
        print("DNI:",dni)
        print("Age:",age)
        print("Gender:",gender)
        print("Study Type:", study_names.get(study_type))
        print("Total:", total)
        exit = input("Do you want to exit?\n Y- Yes\n N- No\n ->").upper()
        if exit == "Y":
            break
    print("Ultrasound customers:", customer_counter_u)
    print("Tomography customers:", customer_counter_t)
    print("Resonance customers:", customer_counter_r)
    print("Discounts:", acum_discount)
    print("Net Total:", acum_total)
    if customer_counter > 0:
        print("Average:", acum_total/customer_counter)
    if customer_counter_u > 0:
        print("Ultrasound customers:", customer_amount_u/customer_counter_u)
    if customer_counter_t > 0:
        print("Tomography customers:", customer_amount_t/customer_counter_t)
    if customer_counter_r > 0:
        print("Resonance customers:", customer_amount_r/customer_counter_r)



def is_third_age(age, gender):
    return (gender == 'F' and age >= 55) or (gender == 'M' and age >= 65)

def discount(is_third_age,customer_counter,amount):
    discount_value = 0
    if is_third_age:
        discount_value += amount * 0.25
    if customer_counter % 2 != 0:
        discount_value += amount * 0.02
    return discount_value

main()