texto = str(input(f'Digite o texto: '))
texto_invertido = []
for c in range(0, len(texto)):
    if texto[c] != ' ':
        print(f'{texto[c]*2}', end='')
        texto_invertido.append(texto[c])
    else:
        print(f'{texto[c]}', end='')
        texto_invertido.append(texto[c])
print()
texto_invertido.reverse()
print(*texto_invertido, sep='')

