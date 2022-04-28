print("***** Welcome to prime validator *****")

number = int(input("Please enter a number to verify: "))
aux = number - 1
is_prime = True

if number < 0:
    print("Invalid number")
elif number < 2:
    print("The number",number,"is not prime")
else:
    while aux > 1:
        if number % aux == 0:
            is_prime = False
        aux -= 1

    if is_prime:
        print("The number",number,"is prime")
    else:
        print("The number",number,"is not prime")

