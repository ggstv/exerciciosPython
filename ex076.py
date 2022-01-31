valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
maior = max(valores)
menor = min(valores)

for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}', end =' ')
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi o {maior} na posição {valores.index(maior)}')
print(f'O menor valor foi o {menor} na posição {valores.index(menor)}')
