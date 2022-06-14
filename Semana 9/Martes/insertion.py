def main():
    lista = [1,3,5,7,4,8,9,2,6]
    print(lista)
    for i in range(len(lista)):#4
        temp = i#1
        valor = lista[i]#1
        j = i - 1#-1
        while j>=0 and valor < lista[j]:
            lista[temp] = lista[j] 
            lista[j] = valor
            temp -= 1
            j-= 1

    print(lista)

main()