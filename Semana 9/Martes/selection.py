def main():
    lista = [3,5,7,1,4,8,9,2,6,3]#1
    for i in range(len(lista)): # n
        menor = i #n
        for j in range(i+1,len(lista)): #n2
            if lista[j] < lista[menor]:#n2
                menor = j #n2
        temp = lista[i] #n
        lista[i] = lista[menor] #n
        lista[menor] = temp#n 

    print(lista)#1

    #2+5n+3n2 = O(n2)

main()