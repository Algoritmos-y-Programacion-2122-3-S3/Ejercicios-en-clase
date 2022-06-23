def selection(lista):
    for i in range(len(lista)): #1
        menor = i #7
        for j in range(i+1,len(lista)): #2
            if lista[j] < lista[menor]:
                menor = j 
        temp = lista[i] #5
        lista[i] = lista[menor] #
        lista[menor] = temp 

    return lista
