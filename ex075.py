valores = [1, 3, 5, 8, 4, 2]

for c, valor in enumerate(valores):
    print(c, end=' ')
    print(valor)
valores.sort()
print()
for c, valor in enumerate(valores):
    print(c, end=' ')
    print(valor)
