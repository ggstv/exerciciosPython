"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0, 3):
        matrix[c][l] = int(input(f'Insira um valor na posição {c, l}: '))

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matrix[c][l]:^4}] ', end='')
    print()
pares = 0
somasc3 = 0
maior3l = max(matrix[2])
for x in range(0, 3):
    for y in range(0, 3):
        if matrix[x][y] % 2 == 0:
            pares += matrix[x][y]
        if y == 2:
            somasc3 += matrix[x][2]
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos números na 3º coluna é {somasc3}.')
print(f'O maior número da 3º linha é {maior3l}.')
