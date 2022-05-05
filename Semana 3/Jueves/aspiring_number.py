number = int(input("Please enter a number to verify: "))
initial_result = 0
aux = 1

while aux < number:
    if number % aux == 0:
        initial_result += aux
    aux += 1

print(initial_result)
perfect_result = 0
aux_perfect = 1

while aux_perfect < initial_result:
    if initial_result % aux_perfect == 0:
        perfect_result += aux_perfect
    aux_perfect += 1

if perfect_result == initial_result:
    print("The number",number,"is aspiring")
else:
    print("The number",number,"is not aspiring")