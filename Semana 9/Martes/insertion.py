def main():
    lista = [1,3,5,7,4,8,9,2,6] # 1
    for i in range(len(lista)): #n
        temp = i#n
        valor = lista[i]#n
        j = i - 1#n
        while j>=0 and valor < lista[j]:#n2
            lista[temp] = lista[j] #n2
            lista[j] = valor#n2
            temp -= 1#n2
            j-= 1#n2

    print(lista)#1

    #2+4n+5n2 = O(n2)

main()