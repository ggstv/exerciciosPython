""""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range (0, 3):
    for l in range(0, 3):
        matrix[c][l]= int(input(f'Insira um valor na posição {c, l}: '))

for c in range (0, 3):
    for l in range(0, 3):
        print(f'[{matrix[c][l]:^4}] ', end='')
    print()
