output = []
print("A")
a = str(input("Enter a Phenotype (AaBb): "))

print("B")
b = str(input("Enter a Phenotype (AaBb): "))

al = []
al2 = []
al3 = []

bl = []
bl2 = []
bl3 = []

x = 0
for i in a:
    if x < (len(a) / 2):
        al.append(i)
    else:
        al2.append(i)
    x += 1

x = 0
for i in b:
    if x < (len(b) / 2):
        bl.append(i)
    else:
        bl2.append(i)
    x += 1

for i in al:
    for i2 in al2:
        al3.append(i + i2)

for i in bl:
    for i2 in bl2:
        bl3.append(i + i2)

print(al3)
print(bl3)

for i in al3:
    for i2 in bl3:
        output.append(i + i2)

print(output)

input("\n\npress any key to exit")
