def main():
    number = input("Enter the number to verify")

    is_incremental = incremental_number(number)

    if is_incremental:
        print("The number",number,"is incremental")
    else:
        print("The number",number,"is not incremental")

def incremental_number(number):
    if(len(number) == 2):
        if number[0] <= number[1]:
            return True
        else:
            return False
    if number[0] <= number[1]:
        return incremental_number(number[1:])
    else:
        return False



main()