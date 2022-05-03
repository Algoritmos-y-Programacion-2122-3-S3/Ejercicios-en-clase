want_to_exit = False


while(not want_to_exit):
    table = int(input("Please enter the table you want: "))
    until = int(input("Please enter the limit: "))

    for n in range(1, until+1):
        print(table,n,sep= " x ",end=" = ")
        print(table*n)
    option = int(input("Do you want to continue? \n 1- Yes \n 2- No \n -->"))

    if option == 2:
        want_to_exit = True
        print("Good bye.")