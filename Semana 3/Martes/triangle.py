rows = int(input("Please enter rows you want: "))

first = 1
current_row = 0

while current_row < rows:
    value_to_add = current_row * 2
    current_value = first + value_to_add

    aux = current_value
    while aux > 0:
        if aux == 1:
            print(aux)
        else:
            print(aux,end="  ")
        aux -= 2
    
    current_row += 1
