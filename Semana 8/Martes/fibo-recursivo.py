def main():
    limit = int(input("Please enter the limit: "))
    num1 = 0
    num2 = 1
    fibo(num1,num2,limit)


def fibo(num1,num2,limit): # num1 = 3, num2=5, limit=0
    print(num1, end=" ") # 0 1 1 2 3
    if limit == 0:
        return num2
    
    return fibo(num2,num1+num2,limit - 1)
     # num1 = 1, num2=0+1, limit=3
     # num1 = 1, num2=1+1, limit=2
     # num1 = 2, num2=1+2, limit=1
     # num1 = 3, num2=2+3, limit=0

main()