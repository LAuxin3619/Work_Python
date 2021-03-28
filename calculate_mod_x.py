a = int(input('>'))
a_1 = int(input('>'))
b = int(input('>'))
c = a ** a_1
while c > b:
    c -= b
print(c)
