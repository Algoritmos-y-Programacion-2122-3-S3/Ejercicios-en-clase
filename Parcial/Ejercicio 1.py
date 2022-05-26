def main():
    option = input("Please enter a option:\n 1- Part A \n 2- Part B\n")
    if option == "1":
        command = input("Please enter a command")
        goal = goal_parser(command)
        print(goal)
    else:
        value = richest_value()
        print(value)

def richest_value():
    accounts = [[1,2,34],[3,2,1]]
    max_amount = 0
    for customer in accounts:
        total = 0
        for bank in customer:
            total += bank
        if total > max_amount:
            max_amount = total
    return max_amount

def goal_parser(command):
    return str(command).replace("()","o").replace("(al)","al")

main()