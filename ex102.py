

def fatorial(num, show=False):
    """Fatora um número inserido e mostra ou não na tela.

    Args:
        num (int): Recebe o número.
        show (bool, optional): [Opção de mostrar.]. Defaults to False.

    Returns:
        int: Retorna os valores calculados.
    """

    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

    
        
         
        
                

num = int(input(f'Insira o número para calcular a fatorial: '))
print(fatorial(5, show=True))
help(fatorial)