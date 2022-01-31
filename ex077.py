"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número 
já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
"""

valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print(f'{num} já existe, não será adicionado. ')
    continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continua in 'Nn':
        break
valores.sort()
#print(f'Você adicionou os números {valores}')
print(f'Você adicionou os números', end=' ')
for valor in valores:
    print(f'{valor:^5}', end=' ')