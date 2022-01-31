
while True:
    num = input(f'Sequência de até 8 dígitos 0s e 1s \n')
    while not num.isnumeric():
        print(f'Digite apenas números, por favor.')
        num = input(f'Sequência de até 8 dígitos 0s e 1s \n')
        continue
    else:
        break
bin = int(num, 2) # converte o binário em inteiro
print(f'Binário: {num} \nInteiro: {bin}') # mostra o número convertido.
