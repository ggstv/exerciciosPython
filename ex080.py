"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas."""

valores = []
while True:
    valores.append(int(input('Insira um valor: ')))
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua in 'Nn':
        break
pares = []
impares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'Lista de valores: {valores} \n Lista de pares: {pares} \n Lista de ímpares: {impares}')

