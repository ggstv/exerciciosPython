def leiaInt(msg):
        n = input(msg)
        if n.isnumeric():
            ok = True
        else:
            print(f'Digite um número.')
        if ok:
            return n

n = leiaInt('Digite um número: ')
print(f'você digitou o número {n}.') 