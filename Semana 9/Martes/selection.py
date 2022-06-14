def main():
    lista = [3,5,7,1,4,8,9,2,6,3]
    print(lista)
    for i in range(len(lista)): #1
        menor = i #7
        for j in range(i+1,len(lista)): #2
            if lista[j] < lista[menor]:
                menor = j 
        temp = lista[i] #5
        lista[i] = lista[menor] #
        lista[menor] = temp 

    print(lista)

main()