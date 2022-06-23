from selection import selection

def main():
     lista = [3,5,7,1,4,8,9,2,6]
     lista = selection(lista)
     print(lista)
     number_to_search = int(input("Enter the number that you want: "))
     if binary_search(lista,number_to_search) != -1:
        print("The number",number_to_search,"was found")
     else:
        print("The number",number_to_search,"was not found")

def binary_search(lista,number_to_search):
    start = 0
    final = len(lista) - 1
    middle = (start + final) // 2
    if len(lista)==1:
        if lista[0] == number_to_search:
            return lista[0]
        else:
            return -1
    if number_to_search > lista[middle]:
        return binary_search(lista[middle:final],number_to_search)
    elif number_to_search < lista[middle]:
        return binary_search(lista[start:middle],number_to_search)
    else:
        return lista[middle]

    
main()