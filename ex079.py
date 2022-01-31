"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'Quantidade de valores digitados: {len(valores)}')
print(f'A lista de valores em ordem decrescente: {sorted(valores, reverse=True)}')
print(f'O número 5 aparece na lista' if 5 in valores else 'O número 5 não está na lista!')