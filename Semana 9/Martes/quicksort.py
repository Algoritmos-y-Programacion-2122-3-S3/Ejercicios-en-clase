def main():
    lista = [3,5,7,1,4,8,9,2,6]
    print(lista)
    lista2 = quicksort(lista)
    print(lista2)

def quicksort(lista):
    if len(lista) < 2:
        return lista
    menor, pivote, mayor = particion(lista)
    return quicksort(menor) + [pivote] + quicksort(mayor)

def particion(lista):
    menor = []
    mayor = []
    pivote = lista[0]
    for i in range(len(lista)):
        if lista[i] < pivote:
            menor.append(lista[i])
        elif lista[i] > pivote:          
            mayor.append(lista[i])
    return menor, pivote, mayor
    

main()