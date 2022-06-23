def main():
    lista = [3,5,7,1,4,8,9,2,6]
    lista_secondary = []

    lista = order_list(lista,lista_secondary)

def order_list(lista,lista_secondary):
    if (len(lista)==0):
        return lista_secondary.append(lista[0])
    minor_index = 0
    minor = lista[0]
    for i in range(len(lista)):
        if lista[i] < minor:
            minor = lista[i]
            minor_index = i



main()