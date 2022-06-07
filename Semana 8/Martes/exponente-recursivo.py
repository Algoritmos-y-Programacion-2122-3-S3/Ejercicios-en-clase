def main():
    base = int(input("Please enter the base number:"))
    exp = int(input("Please enter the exponential number:"))
    result = exponential(base,exp)
    print(result)

def exponential(base, exp):# base = 2 - exp = 1
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    
    return base * exponential(base, exp - 1)
    # return 2 * 2 * 2 * 2 * 2
    # return 2 * 2 * 2 * 2
    # return 2 * 2 * 2
    # return 2 * 2
    #return 2

main()