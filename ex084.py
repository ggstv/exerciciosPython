"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Qual o nome: ')))
    dados.append(float(input('Qual o peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continua = str(input('Quer continuar? Digite N para parar.')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi: {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'Menor peso foi: {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
