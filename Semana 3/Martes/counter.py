number = int(input("Please enter a number: "))
aux = number

if number > -1:
    while aux > -1:
        if aux == 0:
            print(aux)
        else:
            print(aux,end=",")
        aux -= 1

else: 
    print("Number not valid")
    