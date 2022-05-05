import string

abc = list(string.ascii_lowercase)
print(abc)

for i in range(len(abc)):
    if i >= len(abc):
        break
    if i != 0 and i % 3 == 0:
            abc.pop(i)

print(abc)