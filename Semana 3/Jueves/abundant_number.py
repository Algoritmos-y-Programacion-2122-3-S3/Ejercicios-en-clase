number = int(input("Please enter a number to verify: "))
acum = 0
aux = 1

while aux < number:
    if number % aux == 0:
        acum += aux
    aux += 1

if acum > number:
    print("The number",number,"is abundant")
else:
    print("The number",number,"is not abundant")