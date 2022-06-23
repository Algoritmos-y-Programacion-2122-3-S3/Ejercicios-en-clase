def main():
     lista = [3,5,7,1,4,8,9,2,6]
     number_to_search = int(input("Enter the number that you want: "))
     if lineal_search(lista,number_to_search) != -1:
        print("The number",number_to_search,"was found")
     else:
        print("The number",number_to_search,"was not found")

def lineal_search(lista,number_to_search):
    for number in lista:
        if number == number_to_search:
            return number
    return -1


main()