print("***** Welcome to the Bakery *****")
quantity = int(input("Please enter the quantity of breads: "))
price = 3.49
discount = 0.60
net_discount = price*discount
total = price - net_discount

total_without_discount = quantity * price
print("*** BY UNIT ***")
print("The price of bread is:", price)
print("The discount of bread is:", net_discount)
print("The total amount is:", total)

print("*** BY ORDER ***")
print("The total amount is:", total*quantity)

